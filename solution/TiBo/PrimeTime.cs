class PrimeTime
{
    private IEnumerable<double> AllPrimes(int numberOfRooms)
    {
        for (var potenceOf7 = 0; potenceOf7 < numberOfRooms; potenceOf7++)
        {
            for (var potenceOf11 = 0; potenceOf11 < numberOfRooms; potenceOf11++)
            {
                for (var potenceOf13 = 0; potenceOf13 < numberOfRooms; potenceOf13++)
                {
                    yield return (Math.Pow(7, potenceOf7) * Math.Pow(11, potenceOf11) * Math.Pow(13, potenceOf13));
                }
            }
        }
    }

    public double GetMaxRoomNumber(int numberOfRooms)
    {
        return AllPrimes(numberOfRooms).OrderBy(x => x).Skip(199).Take(1).First();
    }
}