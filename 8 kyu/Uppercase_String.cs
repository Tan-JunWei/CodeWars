public static class StringExtensions
{
    public static bool IsUpperCase(this string text)
    {
        int countUpper = 0;

        for (int i = 0; i < text.Length; i++)
        { 
            if (char.IsUpper(text[i]) || text[i].ToString() == " ")
            {
                countUpper++;
            }
        }

        return countUpper == text.Length;
    }
}