import requests

response = requests.get("http://google.com")

print(response.text)

# Next, get the information about Luke Skywalker from SWAPI!
#
# https://swapi.dev/api/people/1/
#
# After getting it, print their height and eye color
#
# Hint: you'll probably need to access the json body of the response with the
# json() method
