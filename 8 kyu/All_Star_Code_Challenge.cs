using System.Linq;

class Kata
{
    public static int StrCount(string str, char letter)
    {
        return str.Count(x => x == letter);
    }
}
