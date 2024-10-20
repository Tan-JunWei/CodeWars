public class Kata
{
  public static string Shortcut(string input)
  {
    foreach (char c in "aeiou")
    {
      input = input.Replace(c.ToString(), "");
    }

    // foreach (char c in input)
    // {
    //   if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
    //   {
    //     input = input.Replace(c.ToString(), "");
    //   }
    // }
    
    return input;
  }
}
