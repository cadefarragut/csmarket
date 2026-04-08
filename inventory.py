import utils

class Inventory:
    def __init__(self, steamid):
        self.steamid = steamid
        self.skins = []

    def getInventory(self):
        inventory = utils.load_json(f"https://steamcommunity.com/inventory/{self.steamid}/730/2", "inv.json")
        for items in inventory["descriptions"]:
            self.skins.append(items["market_hash_name"])



def inv_init(steamid):
    inv = Inventory(steamid)

    inv.getInventory()

    return inv
