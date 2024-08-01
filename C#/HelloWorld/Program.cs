using System;

namespace Examples{
    class program{
        static void Main(string[] args){
            Console.WriteLine("Testando 1,2,3...");
            Console.WriteLine("");

            // Exemplos de variáveis
            int numero = 10; // Variável do tipo inteiro
            double preco = 9.99; // Variável do tipo double
            string mensagem = "Olá, Mundo!"; // Variável do tipo string
            bool status = true; // Variável do tipo booleano
            

            // Imprime as variáveis no console
            Console.WriteLine("Número: " + numero);
            Console.WriteLine("Preço: " + preco);
            Console.WriteLine("Mensagem: " + mensagem);
            Console.WriteLine("Status: " + status);
            Console.WriteLine("");

            // Exemplo de array
            int[] numeros = { 1, 2, 3, 4, 5 };
            Console.WriteLine("Primeiro número no array: " + numeros[0]);
            Console.WriteLine("Segundo número no array: " + numeros[1]);
            Console.WriteLine("Terceiro número no array: " + numeros[2]);
            Console.WriteLine("");

            // Exemplo de lista genérica
            List<string> listaNomes = new List<string> { "Alice", "Bob", "Carlos" };
            listaNomes.Add("Diana");
            Console.WriteLine("Nomes na lista:");
            foreach (string nome in listaNomes)
            {
                Console.WriteLine(nome);
            }
            Console.WriteLine("");

            // Exemplo de estrutura de controle if-else
            if (status)
            {
                Console.WriteLine("Status é verdadeiro.");
                Console.WriteLine("");
            }
            else
            {
                Console.WriteLine("Status é falso.");
                Console.WriteLine("");
            }

            // Exemplo de estrutura de controle switch-case
            numero = 15;
            switch (numero)
            {
                case 10:
                    Console.WriteLine("Número é 10.");
                    Console.WriteLine("");
                    break;
                case 20:
                    Console.WriteLine("Número é 20.");
                    Console.WriteLine("");
                    break;
                default:
                    Console.WriteLine("Número não é 10 nem 20.");
                    Console.WriteLine("");
                    break;
            }

            // Exemplo de laço for
            Console.WriteLine("Laço for:");
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine("Valor de i: " + i);
            }
            Console.WriteLine("");

            // Exemplo de laço while
            Console.WriteLine("Laço while:");
            int contador = 0;
            while (contador < 5)
            {
                Console.WriteLine("Contador: " + contador);
                contador++;
            }
            Console.WriteLine("");

            // Exemplo de função
            double resultadoSoma = Soma(5.2, 7.5);
            Console.WriteLine("Resultado da soma: " + resultadoSoma);
            Console.WriteLine("");

            //Exemplo de Objeto
            Pessoa pessoa1 = new Pessoa("Michel", 25);
            Pessoa pessoa2 = new Pessoa("Tatiana", 26);

            Console.WriteLine("Dados da pessoa 1:");
            pessoa1.ExibirInformacoes();

            Console.WriteLine(pessoa1.ObterInformacoes());

            Console.WriteLine($"Nome: {pessoa1.Nome}");
            Console.WriteLine($"Idade: {pessoa1.Idade}");
            
            pessoa1.AlterarNome("Michel 2");
            pessoa1.Idade += 1;
            var (nome_r, idade_r) = pessoa1.ObterValores();
            Console.WriteLine($"Nome: {nome_r}\nIdade: {idade_r}");



            Console.WriteLine("Dados da pessoa 2:");
            pessoa2.ExibirInformacoes();

            Console.WriteLine(pessoa2.ObterInformacoes());

            Console.WriteLine($"Nome: {pessoa2.Nome}");
            Console.WriteLine($"Idade: {pessoa2.Idade}");

            pessoa2.AlterarNome("Tatiana 2");
            pessoa2.Idade += 1;
            (nome_r, idade_r) = pessoa2.ObterValores();
            Console.WriteLine($"Nome: {nome_r}\nIdade: {idade_r}");
            
        }
        static double Soma(double a, double b)
        {
            return a + b;
        }


    }

    // Define uma classe Pessoa
    class Pessoa{

        // Define propriedades da classe
        public string Nome { get; set;}
        public int Idade { get; set;}
    
        // Define um construtor para inicializar a classe
        public Pessoa(string nome, int idade){
            Nome = nome;
            Idade = idade;
        }

        // Define um método para exibir informações da pessoa
        public void ExibirInformacoes(){
            Console.WriteLine("Nome: " + Nome);
            Console.WriteLine("Idade: " + Idade);
        }

        // Método que retorna as informações da pessoa como uma string formatada
        public string ObterInformacoes(){
            return $"Nome: {Nome}\nIdade: {Idade}";
        }

        // Método que retorna uma tupla com os valores de Nome e Idade
        public (string, int) ObterValores(){
            return (Nome, Idade);
        }

        //Método para alterar nome
        public void AlterarNome(string novoNome){
            Nome = novoNome;
        }

        //Método para alterar idade
        public void AlterarIdade(int novaIdade){
            Idade = novaIdade;
        }
    }
}