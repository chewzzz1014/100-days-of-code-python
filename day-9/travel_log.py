travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, cities):
    c = {}
    c["country"] = country
    c["visits"] = visits
    c["cities"] = cities
    travel_log.append(c)
    print(f"You've visited {country} {visits} times.")

    outString = "You've been to "
    for idx in range(len(cities)):
      if idx < len(cities)-2:
        outString += cities[idx] + ", "
      elif idx < len(cities)-1:
        outString += cities[idx] + " and "
      else:
        outString += cities[idx] + "."

    print(outString)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])


