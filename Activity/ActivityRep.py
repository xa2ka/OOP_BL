# import json
# # from Activity.Activity import Activity
# from EntitiesForOOP import Activity


# class ActivityRep:
#     def __init__(self):
#         self.file_name = "Activities.json"
#         self.activities = self.load_activities_from_file()



#     def GetActivityByName(self, name):
#         for activity in self.activities:
#             if activity.name == name:
#                 return activity
#         return None

#     def GetAllActivities(self):
#             try:
#                 self.activities = self.load_activities_from_file()
#                 return self.activities
#             except Exception as e:
#                 print(f"Ошибка при чтении файла: {e}")

#     def WriteActivityInDb(self, activity):
#         try:
#             self.activities.append(activity)
#             self.WriteActivitiesToFile()
#             print("Activity written to database")
#         except Exception as e:
#             print(f"Ошибка при чтении файла: {e}") 

#     def WriteActivitiesToFile(self):
#         # Преобразование списка активностей в список словарей
#         activities_data = [activity.__dict__ for activity in self.activities]

#         # Запись данных в файл в формате JSON
#         with open(self.file_name, 'w') as file:
#             json.dump(activities_data, file)

#         print("Activities written to file")

#     def load_activities_from_file(self):
#         try:
#             with open(self.file_name, 'r') as file:
#                 activities_data = json.load(file)
#                 activities = [Activity(**activity_data) for activity_data in activities_data]
#                 return activities
#         except FileNotFoundError:
#             return []
#         except Exception as e:
#             print(f"Ошибка при чтении файла: {e}")
#             return []
import sqlite3
from EntitiesForOOP import Activity

class ActivityRep:
    def __init__(self):
        self.database_file = "OOP.db"
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        try:
            with sqlite3.connect(self.database_file) as con:
                cursor = con.cursor()
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS activities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    cal INTEGER
                )
                """)
        except sqlite3.Error as e:
            print(f"Ошибка создания таблицы: {e}")

    def GetActivityByName(self, name):
        try:
            with sqlite3.connect(self.database_file) as con:
                cursor = con.cursor()
                cursor.execute("SELECT * FROM activities WHERE name = ?", (name,))
                row = cursor.fetchone()
                if row:
                    return Activity(row[1], row[2])
                else:
                    return None
        except sqlite3.Error as e:
            print(f"Ошибка чтения из базы данных: {e}")
            return None

    def GetAllActivities(self):
        try:
            with sqlite3.connect(self.database_file) as con:
                cursor = con.cursor()
                cursor.execute("SELECT * FROM activities")
                rows = cursor.fetchall()
                activities = [Activity(row[2], row[1]) for row in rows]
                return activities
        except sqlite3.Error as e:
            print(f"Ошибка чтения из базы данных: {e}")
            return []

    def WriteActivityInDb(self, activity):
        try:
            with sqlite3.connect(self.database_file) as con:
                cursor = con.cursor()
                cursor.execute("INSERT INTO activities (name, cal) VALUES (?, ?)", (activity.name, activity.cal))
                con.commit()
                print("Активность записана в базу данных")
        except sqlite3.Error as e:
            print(f"Ошибка записи в базу данных: {e}")