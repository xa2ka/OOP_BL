import sqlite3
from datetime import datetime
from EntitiesForOOP.UserProd import UserProd

class UserProdRep:
    def __init__(self):
        self.database_file = "OOP.db"
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        try:
            with sqlite3.connect(self.database_file) as con:
                cursor = con.cursor()
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS UserProducts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    user_id INTEGER,
                    cal INTEGER,
                    protein REAL,
                    carbs REAL,
                    fats REAL,
                    date TEXT,
                    weight REAL
                )
                """)
                con.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def GetUserProdList(self, user_id):
        with sqlite3.connect(self.database_file) as con:
            cursor = con.cursor()
            cursor.execute("SELECT * FROM UserProducts WHERE user_id = ?", (user_id,))
            rows = cursor.fetchall()
            user_prods = []
            for row in rows:
                user_prod = UserProd(user_id=row[2], name=row[1], cal=row[3], protein=row[4], carbs=row[5], fats=row[6], date=datetime.strptime(row[7], "%Y-%m-%d").date(), weight=row[8])
                user_prod.id = row[0]
                user_prods.append(user_prod)
            return user_prods

    def WriteInDb(self, user_prod):
        with sqlite3.connect(self.database_file) as con:
            cursor = con.cursor()
            cursor.execute("INSERT INTO UserProducts (name, user_id, cal, protein, carbs, fats, date, weight) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                           (user_prod.name, user_prod.user_id, user_prod.cal, user_prod.protein, user_prod.carbs, user_prod.fats, user_prod.date.strftime("%Y-%m-%d"), user_prod.weight))
            con.commit()
            print("User product written to database")

    def DelInDb(self, user_prod):
        with sqlite3.connect(self.database_file) as con:
            cursor = con.cursor()
            cursor.execute("DELETE FROM UserProducts WHERE id = ?", (user_prod.id,))
            con.commit()
            print("User product deleted from database")
    
    def GetAllUserProd(self):
        with sqlite3.connect(self.database_file) as con:
            cursor = con.cursor()
            cursor.execute("SELECT * FROM UserProducts")
            rows = cursor.fetchall()
            user_prods = []
            for row in rows:
                user_prod = UserProd()
                user_prod.user_id = row[2]
                user_prod.name = row[1]
                user_prod.cal = row[3]
                user_prod.protein = row[4]
                user_prod.carbs = row[5]
                user_prod.fats = row[6]
                user_prod.date = row[7]
                user_prod.weight = row[8]
                user_prod.id = row[0]
                user_prods.append(user_prod)
            return user_prods