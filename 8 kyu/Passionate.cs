using System;

public class Kata
{
    public static string HowMuchILoveYou(int nb_petals)
    {
        // Adjust modulus operation to wrap around correctly
        int index = (nb_petals - 1) % 6;
        string[] phrases = { "I love you", "a little", "a lot", "passionately", "madly", "not at all" };

        return phrases[index];
    }
}
