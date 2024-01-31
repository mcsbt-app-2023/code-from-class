#%%
#{
#  "language": "fr",
#  "translation": "bonjour"
#}

import requests

requests.put(
    "http://127.0.0.1:5000/translation",
    json={"language": "fr", "translation": "bonjour"}
)
# %%
