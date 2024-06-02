import sqlite3
from EntitiesForOOP.Water import Water

class WaterRep:
    def __init__(self):
        self.database_file = "OOP.db"
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        try:
            with sqlite3.connect(self.database_file) as con:
                cursor = con.cursor()
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS Water (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    date TEXT,
                    ml REAL
                )
                """)
                con.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def GetwaterByDate(self, user_id, date):
        try:
            with sqlite3.connect(self.database_file) as con:
                cursor = con.cursor()
                cursor.execute("SELECT id, user_id, date, ml FROM Water WHERE user_id = ? AND date = ?", (user_id, date))
                rows = cursor.fetchall()
                waters = []
                for row in rows:
                    water = Water(row[1], row[3], row[2])
                    water.id = row[0]
                    waters.append(water)
                return waters
        except sqlite3.Error as e:
            print(f"Error retrieving water data: {e}")
            return []

    def addWater(self, water):
        try:
            with sqlite3.connect(self.database_file) as con:
                cursor = con.cursor()
                cursor.execute("INSERT INTO Water (user_id, date, ml) VALUES (?, ?, ?)", 
                              (water.user_id, water.date, water.ml))
                con.commit()
                print("Water data written to database")
        except sqlite3.Error as e:
            print(f"Error writing water data: {e}")

    def DeleteWater(self, water_id):
        try:
            with sqlite3.connect(self.database_file) as con:
                cursor = con.cursor()
                cursor.execute("DELETE FROM Water WHERE id = ?", (water_id,))
                con.commit()
                print("Water data deleted from database")
        except sqlite3.Error as e:
            print(f"Error deleting water data: {e}")