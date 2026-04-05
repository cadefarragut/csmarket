import sqlite3

class Database:
    def __init__(self, name):
        self.name = name

    def create_connection(self):
        print(f"Creating connection for {self.name}")
        try:
            conn = sqlite3.connect(self.name)
            print("Connected")
            return conn
        except:
            print(f"Failed to connect to {self.name}")
            return None

    def create_cursor(self, conn):
        print("Creating cursor")
        try:
            cursor = conn.cursor()
            print("cusor created")
            return cursor
        except:
            print("failed to create cursor")
            return None 
        
    def create_table(self, cursor, conn):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS skins (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       weapon TEXT,
                       rarity TEXT,
                       price REAL,
                       updated_at TEXT
                       )
                """)
        conn.commit()


        

# This function creates a sqlite db file and return the cursor for execution

def createDB(name):
    inv = Database(name)

    conn = inv.create_connection()

    cursor = inv.create_cursor(conn)

    inv.create_table(cursor, conn)

    return cursor 

def insertDB(cursor):
    pass

    


