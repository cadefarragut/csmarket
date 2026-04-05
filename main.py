import requests
import json
import os
import database as db

BASE_URL= "https://raw.githubusercontent.com/ByMykel/CSGO-API/main/public/api/en"
SKINS_URL = f"{BASE_URL}/skins.json"
WEARS_URL = f"{BASE_URL}/skins_not_grouped.json"

def load_json(url, cache_file):
    if os.path.exists(cache_file):
        with open(cache_file, "r") as f:
            return json.load(f)
    response = requests.get(url)
    r_json = response.json()

    with open(cache_file, "w") as f:
        json.dump(r_json, f)
    
    return r_json


def getInformation(skin_id):
    for skin in wears:
        if skin["id"] == skin_id:
            return {
                "id": skin["id"],
                "name": skin["name"],
                "market_hash_name": skin["market_hash_name"],
            }
    return None
        


def main():
    m9_bayonet_stained_ft = getInformation("skin-bab9cbb31702_2")
    ak47_sv_pant_ft = getInformation("skin-2faa35fd1c44_2_so")
    m4a1_play_ft = getInformation("skin-4dd5dccd2fdd_2")


    my_inventory.append(m9_bayonet_stained_ft)
    my_inventory.append(ak47_sv_pant_ft)
    my_inventory.append(m4a1_play_ft)

    inv = db.createDB("CadeInv.db")
    #for skins in my_inventory:
    inv.insertInv(my_inventory)


my_inventory = []    
skins = load_json(SKINS_URL, "skins_cache.json")
wears = load_json(WEARS_URL, "wears_cache.json")
main()

