namespace FirstAPI.Models
{
    public class Hello
    {
        public string Name { get; set; }

        public void SayHello()
        {
            Console.WriteLine($"New name consult: {Name}!");
        }
    }
}