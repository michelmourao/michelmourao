// Importa os namespaces necessários para o programa
using System;
using System.Collections.Generic;
using System.Linq;

namespace ExemploIntroducao
{
    // Define uma classe principal para o programa
    class Program
    {
        // Define o ponto de entrada principal do programa
        static void Main(string[] args)
        {
            // Imprime uma mensagem no console
            Console.WriteLine("Bem-vindo ao exemplo introdutório de C# .NET!");

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

            // Exemplo de array
            int[] numeros = { 1, 2, 3, 4, 5 };
            Console.WriteLine("Primeiro número no array: " + numeros[0]);

            // Exemplo de lista genérica
            List<string> listaNomes = new List<string> { "Alice", "Bob", "Carlos" };
            listaNomes.Add("Diana");
            Console.WriteLine("Nomes na lista:");
            foreach (string nome in listaNomes)
            {
                Console.WriteLine(nome);
            }

            // Exemplo de estrutura de controle if-else
            if (status)
            {
                Console.WriteLine("Status é verdadeiro.");
            }
            else
            {
                Console.WriteLine("Status é falso.");
            }

            // Exemplo de estrutura de controle switch-case
            switch (numero)
            {
                case 10:
                    Console.WriteLine("Número é 10.");
                    break;
                case 20:
                    Console.WriteLine("Número é 20.");
                    break;
                default:
                    Console.WriteLine("Número não é 10 nem 20.");
                    break;
            }

            // Exemplo de laço for
            Console.WriteLine("Laço for:");
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine("Valor de i: " + i);
            }

            // Exemplo de laço while
            Console.WriteLine("Laço while:");
            int contador = 0;
            while (contador < 5)
            {
                Console.WriteLine("Contador: " + contador);
                contador++;
            }

            // Exemplo de função
            int resultadoSoma = Soma(5, 7);
            Console.WriteLine("Resultado da soma: " + resultadoSoma);

            // Exemplo de classe e objeto
            Pessoa pessoa = new Pessoa("João", 25);
            pessoa.ExibirInformacoes();
        }

        // Define uma função que soma dois números e retorna o resultado
        static int Soma(int a, int b)
        {
            return a + b;
        }
    }

    // Define uma classe Pessoa
    class Pessoa
    {
        // Define propriedades da classe
        public string Nome { get; set; }
        public int Idade { get; set; }

        // Define um construtor para inicializar a classe
        public Pessoa(string nome, int idade)
        {
            Nome = nome;
            Idade = idade;
        }

        // Define um método para exibir informações da pessoa
        public void ExibirInformacoes()
        {
            Console.WriteLine("Nome: " + Nome);
            Console.WriteLine("Idade: " + Idade);
        }
    }
}
