using System.Linq;

public static class Kata
{
    public static int TotalPoints(string[] games)
    {
        int totalPoints = 0;

        foreach (string s in games)
        {
            int x = int.Parse(s.Split(":")[0]);
            int y = int.Parse(s.Split(":")[1]);

            //if (x > y)
            //{
            //    totalPoints += 3;
            //}
            //else if (x == y)
            //{
            //    totalPoints += 1;
            //}
            //else
            //{
            //    continue;
            //}

            totalPoints += (x > y) ? 3 : (x == y) ? 1 : 0;
        }

        return totalPoints;
    }
}