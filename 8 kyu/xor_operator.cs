public class Kata
{
    public static bool Xor(bool a, bool b)
    {
        // if (a == b)
        // {
        //     return false;
        // }
        // else
        // {
        //     return true;
        // }

        bool result;
        result = (a == b) ? false : true;

        return result;
    }
}

// Console.WriteLine(Kata.Xor(true, false)); // true