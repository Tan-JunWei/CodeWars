using System;

namespace Extensions
{
  public static class StringExt
  {
    public static string ToAlternatingCase (this string s)
    {
      string AlternatedStr = "";

      foreach (char c in s)
      {
        // if (char.IsUpper(c))
        // {
        //     AlternatedStr += char.ToLower(c);
        // }
        // else
        // {
        //     AlternatedStr += char.ToUpper(c);
        // }
        AlternatedStr += (char.IsUpper(c)) ? char.ToLower(c) : char.ToUpper(c); // using ternary operators
      }

      return AlternatedStr;
    }
  }
}