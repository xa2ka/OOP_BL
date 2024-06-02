import sqlite3
from EntitiesForOOP.UserAct import UserAct

class UserActivityRep:
    def __init__(self):
        self.database_file = "OOP.db"
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        try:
            with sqlite3.connect(self.database_file) as con:
                cursor = con.cursor()
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS UserActivities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    user_id INTEGER,
                    date TEXT,
                    cal REAL,
                    number_min INTEGER
                )
                """)
                con.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def GetUserActList(self):
        with sqlite3.connect(self.database_file) as con:
            cursor = con.cursor()
            cursor.execute("SELECT * FROM UserActivities")
            rows = cursor.fetchall()
            user_acts = []
            for row in rows:
                user_act = UserAct()
                user_act.id, user_act.name, user_act.user_id, user_act.date, user_act.cal, user_act.number_min = row
                user_acts.append(user_act)
            return user_acts

    def GetUserActByDate(self, user_id, date):
        with sqlite3.connect(self.database_file) as con:
            cursor = con.cursor()
            cursor.execute("SELECT * FROM UserActivities WHERE user_id = ? AND date = ?", (user_id, date))
            rows = cursor.fetchall()
            user_acts = []
            for row in rows:
                user_act = UserAct()
                user_act.id, user_act.name, user_act.user_id, user_act.date, user_act.cal, user_act.number_min = row
                user_acts.append(user_act)
            return user_acts

    def WriteInDb(self, user_act):
        with sqlite3.connect(self.database_file) as con:
            cursor = con.cursor()
            cursor.execute("INSERT INTO UserActivities (name, user_id, date, cal, number_min) VALUES (?, ?, ?, ?, ?)",
                           (user_act.name, user_act.user_id, user_act.date, user_act.cal, user_act.number_min))
            con.commit()
            print("User activity written to database")

    def delete_from_db(self, user_id):
        with sqlite3.connect(self.database_file) as con:
            cursor = con.cursor()
            cursor.execute("DELETE FROM UserActivities WHERE user_id = ?", (user_id,))
            con.commit()
            print("User activity deleted from database")