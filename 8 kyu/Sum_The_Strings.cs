using System;

namespace Solution
{
  public static class Program
  {
    public static string StringsSum(string s1, string s2)
    {   
        int num1 = 0;
        int num2 = 0; 
      
        // if (string.IsNullOrEmpty(s1))
        // {
        //     num1 = 0;
        // }
        // else{
        //     num1 = Convert.ToInt32(s1);
        // }
        
        // if (string.IsNullOrEmpty(s2))
        // {
        //     num2 = 0;
        // }
        // else{
        //     num2 = Convert.ToInt32(s2);
        // }

        if (s1 != ""){
            num1 = Convert.ToInt32(s1);
        }
        if (s2 != ""){
            num2 = Convert.ToInt32(s2);
        }

        return (num1 + num2).ToString();
    }
  }
}