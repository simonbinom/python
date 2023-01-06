# import requests
import requests

# send a HTTP-GET to the API and save response in a variable
try:
    response = requests.get("https://sv443.net/jokeapi/v2/joke/Programming")
except requests.exceptions.RequestException as e:
    # handle exceptions that may occur when making the request
    print("An error occurred while making the request:", e)

# parse response in json
try:
    data = response.json()
except ValueError as e:
    # handle exceptions that may occur when parsing the response
    print("An error occurred while parsing the response:", e)

# extract joke from json
try:
    joke = data["joke"]
except KeyError as e:
    # handle exceptions that may occur when extracting the joke from the data
    print("An error occurred while extracting the joke from the data:", e)

# print joke
print(joke)