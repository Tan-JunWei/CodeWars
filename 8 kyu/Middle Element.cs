using System;
using System.Linq;

public class Kata
{
    public static int Gimme(double[] inputArray)
    {
        double min = inputArray.Min();
        double max = inputArray.Max();

        double middleValue = inputArray.First(x => x != min && x != max);

        return Array.IndexOf(inputArray, middleValue);
    }
}
