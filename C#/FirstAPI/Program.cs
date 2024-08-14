
using FirstAPI.Models;
using System;
using System.Linq;
using System.Text;
using System.IdentityModel.Tokens.Jwt;
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.IdentityModel.Tokens;
using Microsoft.OpenApi.Models;
using System.Security.Claims;

namespace FirstAPI
{
    class Program
    {
        static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);

            // Chave gerada
            var key = Encoding.ASCII.GetBytes("OyQ1QU4oRUxQODE1WE1wck0+JTM9QikovNkhqcUwqLDs/");

            // Adicione serviços ao contêiner.
            builder.Services.AddEndpointsApiExplorer();
            builder.Services.AddSwaggerGen(c =>
            {
                c.SwaggerDoc("v1", new OpenApiInfo { Title = "FirstAPI", Version = "v1" });

                // Definição de segurança para JWT
                c.AddSecurityDefinition("Bearer", new OpenApiSecurityScheme
                {
                    Description = "JWT Authorization header usando o esquema Bearer.\n\nDigite 'Bearer' [espaço] e então seu token na entrada de texto abaixo.\n\nExemplo: 'Bearer 12345abcdef'\n\n",
                    Name = "Authorization",
                    In = ParameterLocation.Header,
                    Type = SecuritySchemeType.ApiKey,
                    Scheme = "Bearer"
                });

                c.AddSecurityRequirement(new OpenApiSecurityRequirement()
                {
                    {
                        new OpenApiSecurityScheme
                        {
                            Reference = new OpenApiReference
                            {
                                Type = ReferenceType.SecurityScheme,
                                Id = "Bearer"
                            },
                            Scheme = "oauth2",
                            Name = "Bearer",
                            In = ParameterLocation.Header,

                        },
                        new List<string>()
                    }
                });
            });

            // Adicione serviços de autenticação e autorização
            builder.Services.AddAuthentication(options =>
            {
                options.DefaultAuthenticateScheme = JwtBearerDefaults.AuthenticationScheme;
                options.DefaultChallengeScheme = JwtBearerDefaults.AuthenticationScheme;
            }).AddJwtBearer(options =>
            {
                options.TokenValidationParameters = new TokenValidationParameters
                {
                    ValidateIssuerSigningKey = true,
                    IssuerSigningKey = new SymmetricSecurityKey(key),
                    ValidateIssuer = false,
                    ValidateAudience = false
                };
            });

            builder.Services.AddAuthorization(); // Adicione esta linha para adicionar serviços de autorização

            var app = builder.Build();

            // Configure o pipeline de solicitação HTTP.
            if (app.Environment.IsDevelopment())
            {
                app.UseSwagger();
                app.UseSwaggerUI(c =>
                {
                    c.SwaggerEndpoint("/swagger/v1/swagger.json", "FirstAPI v1");
                });
            }

            app.UseHttpsRedirection();

            app.UseAuthentication(); // Adicione a autenticação ao pipeline
            app.UseAuthorization();  // Adicione a autorização ao pipeline

            var summaries = new[]
            {
                "Frio pra kct", "Friozinho", "Confortável", "Quente", "Quente pra kct"
            };

            // Endpoint para autenticação
            app.MapPost("/authenticate", (UserCredential user) =>
            {
                if (user.Username == "admin" && user.Password == "admin")
                {
                    var tokenHandler = new JwtSecurityTokenHandler();
                    var tokenDescriptor = new SecurityTokenDescriptor
                    {
                        Subject = new ClaimsIdentity(new Claim[]
                        {
                            new Claim(ClaimTypes.Name, user.Username)
                        }),
                        Expires = DateTime.UtcNow.AddHours(1),
                        SigningCredentials = new SigningCredentials(new SymmetricSecurityKey(key), SecurityAlgorithms.HmacSha256Signature)
                    };
                    var token = tokenHandler.CreateToken(tokenDescriptor);
                    var tokenString = tokenHandler.WriteToken(token);

                    return Results.Ok(new { Token = tokenString });
                }
                return Results.Unauthorized();
            });

            app.MapGet("/weatherforecast", () =>
            {
                var forecast = Enumerable.Range(1, 3).Select(index =>
                    new WeatherForecast
                    (
                        DateOnly.FromDateTime(DateTime.Now.AddDays(index)),
                        Random.Shared.Next(-20, 55),
                        summaries[Random.Shared.Next(summaries.Length)]
                    ))
                    .ToArray();
                return forecast;
            }).RequireAuthorization();

            app.MapGet("/weatherforecast/days/{days}", (int days) =>
            {
                var forecast = Enumerable.Range(1, days).Select(index =>
                    new WeatherForecast
                    (
                        DateOnly.FromDateTime(DateTime.Now.AddDays(index)),
                        Random.Shared.Next(-20, 55),
                        summaries[Random.Shared.Next(summaries.Length)]
                    ))
                    .ToArray();
                return forecast;
            }).RequireAuthorization();

            app.MapGet("/Validate/{code}", (string code) =>
            {
                bool accept = false;

                if (code == "A123")
                {
                    accept = true;
                }

                return Results.Ok(accept);
            }).RequireAuthorization();

            app.MapGet("/CurrentDateTime", () =>
            {
                var currentDateTime = DateTime.Now;
                return Results.Ok(currentDateTime);
            }).RequireAuthorization();

            app.MapGet("/Hello/{name}", (string name) =>
            {
                Hello newName = new Hello();
                newName.Name = name;
                newName.SayHello();
                return Results.Ok($"Hello, {name}!");
            }).RequireAuthorization();

            app.Run();
        }

        // Definição de record fora do método Main
        public record WeatherForecast(DateOnly Date, int TemperatureC, string? Summary)
        {
            public int TemperatureF => 32 + (int)(TemperatureC / 0.5556);
        }
    }

    // Classe Hello, por exemplo
    public class Hello
    {
        public string Name { get; set; }

        public void SayHello()
        {
            Console.WriteLine($"Hello, {Name}!");
        }
    }

    public class UserCredential
    {
        public string Username { get; set; }
        public string Password { get; set; }
    }
}
