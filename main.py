import database as db
import inventory as inv
import utils

BASE_URL= "https://raw.githubusercontent.com/ByMykel/CSGO-API/main/public/api/en"
SKINS_URL = f"{BASE_URL}/skins.json"
WEARS_URL = f"{BASE_URL}/skins_not_grouped.json"
  




def main():
    skins = utils.load_json(SKINS_URL, "skins_cache.json")
    wears = utils.load_json(WEARS_URL, "wears_cache.json")

    inventory = inv.createInv("76561198146131977")
    print(inventory.skins)
    

    database = db.createDB("CadeInv.db")
    #for skins in my_inventory:
    #database.insertInv(inven)



if __name__ == "__main__":
    main()

