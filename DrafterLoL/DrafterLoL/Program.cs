using System;

class Program{
    static void Main(string[] args)
    {
        const int teamB = 0;
        const int teamR = 1;

        // Déclaration d'un tableau pour stocker les entrées
        string[,] ChampionsSelected = new string[2,5];

        GetInputs(teamB,ChampionsSelected);

        GetInputs(teamR,ChampionsSelected);

        AfficheTeam(ChampionsSelected);
 
        Console.WriteLine("\nAppuiyez sur n'importe quelle touche pour quitter.");
        Console.ReadKey();
    }
    
    static void GetInputs(int team, string[,] inputs)
    {
        for (int i = 0; i < inputs.GetLength(1); i++)
        {
            Console.Write($"Entrée {i + 1}: ");
            inputs[team,i] = Console.ReadLine();
        }
    }

    static void DisplayInputs(int team, string[,] inputs)
    {
        Console.WriteLine("\nValeurs entrées :");
        for (int i = 0; i < inputs.GetLength(1); i++)
        {
            Console.WriteLine($"Entrée {i + 1}: {inputs[team, i]}");
        }
    }

        static void AfficheTeam(string[,] inputs)
    {
        DisplayInputs(0,inputs);
        DisplayInputs(1,inputs);
    }

}
