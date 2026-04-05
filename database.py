import sqlite3

class Database:
    def __init__(self, name):
        self.name = name
        self.conn = None
        self.cursor = None

    def create_connection(self):
        print(f"Creating connection for {self.name}")
        try:
            self.conn = sqlite3.connect(self.name)
            print("Connected")
        except:
            print(f"Failed to connect to {self.name}")

    def create_cursor(self):
        print("Creating cursor")
        try:
            self.cursor = self.conn.cursor()
            print("cusor created")
        except:
            print("failed to create cursor")
        
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS skins (
                       id TEXT,
                       name TEXT,
                       market_hash_name TEXT
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
    inv = Database(name)

    inv.create_connection()

    inv.create_cursor()

    inv.create_table()

    return inv
    


