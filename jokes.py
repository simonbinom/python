# This code sends a GET request to an API at the specified URL. 
# The API returns a joke about programming in JSON format. 
# The code parses the response and extracts the joke from it. 
# Finally, the code prints the joke to the console.

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