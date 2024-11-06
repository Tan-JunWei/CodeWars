using System;

public class Kata
{   
  public static string NameShuffler(string str)
  {
    string[] names = str.Split(' ');
    Array.Reverse(names);
    return string.Join(" ", names);
  }
}

Console.WriteLine(Kata.NameShuffler("John Doe")); // Doe John