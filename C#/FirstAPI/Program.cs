var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

var summaries = new[]
{
    "Frio pra kct", "Friozinho", "Confortável", "Quente", "Quente pra kct"
};

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
});

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
});

app.MapGet("/Validate/{code}", (string code) =>
{
    bool accept = false;

    if (code == "A123")
    {
        accept = true;
    }

    return Results.Ok(accept);
});

app.MapGet("/CurrentDateTime", () =>
{
    var currentDateTime = DateTime.Now;
    return currentDateTime;
})

.WithName("First API")
.WithOpenApi();

app.Run();

record WeatherForecast(DateOnly Date, int TemperatureC, string? Summary)
{
    public int TemperatureF => 32 + (int)(TemperatureC / 0.5556);
}