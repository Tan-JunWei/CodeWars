using System.Reflection.Metadata.Ecma335;

public class Number
{
    public bool IsEven(double n)
    {
        bool result = n % 2 == 0 ? true : false;
        return result;
    }

}
