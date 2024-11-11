using System.Xml.Schema;

public class RentalCar
{

    public static int RentalCarCost(int d)
    {
        int totalCost;
        totalCost = 40 * d;

        //if (d >= 3 && d < 7)
        //{
        //    totalCost -= 20;
        //}
        //else if (d >= 7)
        //{
        //    totalCost -= 50;
        //}

        int result = (d >= 3 && d < 7) ? totalCost - 20 : (d >= 7) ? totalCost - 50 : totalCost;

        return result;
    }
}