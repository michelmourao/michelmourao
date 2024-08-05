using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);
builder.Services.addDbContext<AppDbContext>();

var app = builder.Build();

app.MapGet("/v1/todos", (AppDbContext context) => {
    var todos = context.Todos.ToList();
    return Results.Ok(todo);
});

app.Run();
