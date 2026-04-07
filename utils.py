import json
import requests
import os

def load_json(url, cache_file):
    if os.path.exists(cache_file):
        with open(cache_file, "r") as f:
            return json.load(f)
    response = requests.get(url)
    r_json = response.json()

    with open(cache_file, "w") as f:
        json.dump(r_json, f)
    
    return r_json
  