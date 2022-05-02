#!C:\python.exe
# ^^^ Update this line with the path to your python env!

import requests
import os
import sys
import json
try:
    with open(".\names.json") as names:
        
        # Names being a json file mapping country codes to countries
        nameslist = json.load(names)

        # Get name input from the user
        if len(sys.argv) > 1:
            nameInput = str(sys.argv[1])
        else:
            nameInput = input("Please give us your first name: ")

        # Send name input to age, gender, and country APIs
        ageResponse = requests.get("https://api.agify.io/?name="+nameInput)
        genderResponse = requests.get("https://api.genderize.io/?name="+nameInput)
        countryResponse = requests.get("https://api.nationalize.io/?name="+nameInput)

        # Take the first country that is listed as probable
        # If there is only one or two countries returned, change the response accordingly
        country1 = countryResponse.json()["country"][0]["country_id"]
        try:
            country2 = countryResponse.json()["country"][1]["country_id"]
            country3 = countryResponse.json()["country"][2]["country_id"]
            print("Based on this, we estimate you to be", genderResponse.json()["gender"]+ ",", ageResponse.json()["age"], "years old, and from either", nameslist[country1]+ ",", nameslist[country2]+ ", or", nameslist[country3]) 
            

        except:
            try:
                country2 = countryResponse.json()["country"][1]["country_id"]
                print("Based on this, we estimate you to be", genderResponse.json()["gender"]+ ",", ageResponse.json()["age"], "years old, and from either", nameslist[country1], "or", nameslist[country2]) 
                
            except:
                print("Based on this, we estimate you to be", genderResponse.json()["gender"]+ ",", ageResponse.json()["age"], "years old, and from", nameslist[country1]) 
                

# Handle bad names
except IndexError:
    print("This is an invalid name. Please try again")

# Handle other exceptions
except Exception as e:
    print(e)
