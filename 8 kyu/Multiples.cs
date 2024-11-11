using System.Collections.Generic;

public class Kata
{
    public static List<int> FindMultiples(int integer, int limit)
    {
        List<int> multiples = new List <int> ();

        for (int i = integer; i <= limit; i += integer)
        {
            multiples.Add(i);
        }

        return multiples;
    }
}