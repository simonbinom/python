# import requests
import requests

# send a HTTP-GET to the API and save response in a variable
response = requests.get("https://sv443.net/jokeapi/v2/joke/Programming")

# parse response in json
data = response.json()

# extract joke from json
joke = data["joke"]

# print joke
print(joke)