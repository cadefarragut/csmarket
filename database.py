import sqlite3

class Database:
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect(self.name)
        self.cursor = self.conn.cursor()
        
    def create_table_inventory(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS skins (
                       id TEXT,
                       name TEXT,
                       market_hash_name TEXT
                       )
                """)
        self.conn.commit()

    def create_table_pricehistory(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS prices (  
                            market_hash_name TEXT,
                            price REAL,
                            timestamp TEXT
                       )
                """)
        self.conn.commit()

    def insertInv(self, inventory):
        self.cursor.executemany("""
            INSERT INTO skins VALUES (:id, :name, :market_hash_name)
                """, inventory)
        self.conn.commit()
        



# This function creates a sqlite db file and return the cursor for execution

def createDB(name):
    inv_db = Database(name)

    inv_db.create_table_inventory()

    inv_db.create_table_pricehistory()

    return inv_db
    


