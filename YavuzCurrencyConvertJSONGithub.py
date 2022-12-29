#JSON Currency Convert
#By Yavuz

import json
from urllib.request import urlopen

with urlopen("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd.json") as response:
    source = response.read()

data = json.loads(source)
countries = data["usd"]

print(json.dumps(data["usd"], indent=2))
print("Welcome to the Currency Converter!")
print()
input("Press enter to continue the program!")
print(countries.keys())

with urlopen("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.min.json") as response2:
    countrysource = response2.read()

countrynames = json.loads(countrysource)

print(countrynames)

finished = True

while finished:
    country = input("Enter a country currency to convert into from USD: ")
    if country in countrynames:
        amount = float(input("Enter Dollar amount to be converted: $ "))
        value = amount * float(countries[country])
        print(f"A ${amount} US Dollars is worth ${value} in {countrynames[country]}")
        print()
    else:
        print(f"Country code of {country} not found")
    if input ("Would you like to try another country? (response require as y or n): ").upper() == "N":
        finished = False
        print("Thank you for using our program, have a nice day!")
