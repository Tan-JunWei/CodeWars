public static class Kata
{
    public static string RemoveUrlAnchor(string url)
    {
        int indexOfAnchor = url.IndexOf("#");

        // Check if '#' is found
        if (indexOfAnchor == -1)
        {
            return url; 
        }

        return url.Substring(0, indexOfAnchor); // Remove anchor

        /* 
        return url.Split("#)[0]; 
        */
    }
}
