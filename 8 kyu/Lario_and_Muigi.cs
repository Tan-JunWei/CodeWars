using System.Collections.Generic;
using System.Linq;

public class Fixer
{
    public static List<int> PipeFix(List<int> numbers)
    {
        int min = numbers.Min();
        int max = numbers.Max();

        List<int> incrementList = new List <int> ();

        for (int i = min; i <= max; i++)
        {
            incrementList.Add(i);
        }

        return incrementList;
    }
}