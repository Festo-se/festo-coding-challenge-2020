namespace Part3
{
    class Program
    {
        static void Main(string[] args)
        {
            var bestRoute = new Delivery()
                .EnumerateRoutes(new List<Station>(), Delivery.AllStations.ToList())
                .Select(route => new { cost = Delivery.RouteCost(route), route })
                .OrderBy(x => x.cost)
                .Take(1);
                ;
        }
    }


    class Station
    {
        public int index { get; init; }
        public bool pick { get; init; }
        public int restaurantId { get; init; }
    }

    class Delivery
    {
        private static byte[,] field = new byte[12, 12]
        {
            { 0,  6,  3, 22, 20, 10,  0,  0,  0,  0,  0,  0},
              {0,  0,  5, 28, 18,  4, 22, 17,  8, 23, 26,  0},
              {0,  4,  0, 23, 18,  7, 17, 12,  8, 19, 21,  0},
              {0, 25, 21,  0, 21, 27,  5, 17, 22,  6,  4,  0},
              {0, 20, 20, 25,  0, 16, 19, 28, 10, 17, 26,  0},
              {0,  5,  9, 30, 16,  0, 23, 21,  6, 24, 28,  0},
              {0,  0, 16,  6, 16, 21,  0, 14, 16,  3,  6, 16},
              {0, 14,  0, 17, 24, 17, 14,  0, 17, 17, 14, 15},
              {0,  9, 10,  0, 10,  6, 19, 21,  0, 18, 24,  3},
              {0, 22, 18,  8,  0, 22,  4, 19, 16,  0, 10, 17},
              {0, 23, 18,  4, 22,  0,  5, 13, 21,  8,  0, 20},
              {0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},
        };

        public static IEnumerable<Station> AllStations { get; } = new List<Station>
        {
            new Station(){  index = 1, pick = true, restaurantId = 1 },
            new Station(){  index = 2, pick = true, restaurantId = 2 },
            new Station(){  index = 3, pick = true, restaurantId = 3 },
            new Station(){  index = 4, pick = true, restaurantId = 4 },
            new Station(){  index = 5, pick = true, restaurantId = 5},

            new Station(){  index = 6, pick = false, restaurantId = 1 },
            new Station(){  index = 7, pick = false, restaurantId = 2 },
            new Station(){  index = 8, pick = false, restaurantId = 3 },
            new Station(){  index = 9, pick = false, restaurantId = 4 },
            new Station(){  index = 10, pick = false, restaurantId = 5},
        };

        public IEnumerable<IReadOnlyList<Station>> EnumerateRoutes(IReadOnlyList<Station> currentRoute, IReadOnlyList<Station> openStations)
        {
            if(openStations.Count() == 0)
            {
                yield return currentRoute;
                yield break;
            }

            foreach (var nextStation in openStations)
            {
                var currentRouteWorkingCopy = currentRoute.ToList();
                currentRouteWorkingCopy.Add(nextStation);

                if(ValidateRoute(currentRouteWorkingCopy))
                {
                    var openStationsWorkingCopy = openStations.ToList();
                    openStationsWorkingCopy.Remove(nextStation);

                    var validRoutes = EnumerateRoutes(currentRouteWorkingCopy, openStationsWorkingCopy);
                    foreach (var validRoute in validRoutes)
                    {
                        yield return validRoute;
                    }
                }
            }
        }

        private bool ValidateRoute(IReadOnlyList<Station> routeToValidate)
        {
            HashSet<int> currentFoods = new HashSet<int>();

            foreach (var station in routeToValidate)
            {
                if(station.pick)
                {
                    currentFoods.Add(station.restaurantId);
                    if(currentFoods.Count > 3)
                    {
                        // diese Station würde das Bike überladen
                        return false;
                    }
                }
                else
                {
                    if(!currentFoods.Contains(station.restaurantId))
                    {
                        // das Essen ist noch gar nicht im Korb
                        return false;
                    }
                    currentFoods.Remove(station.restaurantId);
                }
            }

            return true;
        }

        public static int RouteCost(IReadOnlyList<Station> stations)
        {
            int initialCost = field[0, stations.First().index];
            int lastCosts = field[stations.Last().index, 11];

            int intermediateCost = 0;
            for(var i=0; i<stations.Count-1; i++)
            {
                intermediateCost += field[stations[i].index, stations[i + 1].index];
            }

            return initialCost + intermediateCost + lastCosts;
        }
    }
}