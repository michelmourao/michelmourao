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

    public class UserCredential
    {
        public string Username { get; set; }
        public string Password { get; set; }
    }
}