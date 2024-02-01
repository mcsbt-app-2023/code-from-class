# %%
import requests

tweet = {"name": "Larbi", "content": "My code doesn't work, lol"}
url = "http://127.0.0.1:5000/tweet"

response = requests.put(url, json=tweet)

print(response)
print(response.text)

# %%
