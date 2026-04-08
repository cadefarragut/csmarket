import sqlite3

class Database:
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect(self.name)
        self.cursor = self.conn.cursor()

    def createMarketDB(self):
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS market (
                        market_hash_name TEXT,
                        price REAL,
                        source TEXT,
                        time TEXT
                        )
                    """)
        self.conn.commit()

    def insert_price(self, market_hash_name, price, source, time):
        self.cursor.execute("""
                INSERT INTO market (market_hash_name, price, source, time)
                    VALUES (?, ?, ?, ?)
                    """, (market_hash_name, price, source, time))
        self.conn.commit()
    
    def get_prices(self, market_hash_name):
        self.cursor.execute("SELECT * FROM market WHERE market_hash_name = ?", (market_hash_name,))
        return self.cursor.fetchall()



def db_init(name):
    inv_db = Database(name)

    return inv_db


