# from Reminders.Reminders import Reminder
from EntitiesForOOP.Reminders import Reminder
import sqlite3


class RemindersRep:
    def __init__(self):
        self.database_file = "OOP.db"
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        try:
            with sqlite3.connect(self.database_file) as con:
                cursor = con.cursor()
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS reminders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    name TEXT,
                    on_off INTEGER,
                    time TEXT
                )
                """)
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def GetRemindersByUserId(self, user_id):
        try:
            with sqlite3.connect(self.database_file) as con:
                cursor = con.cursor()
                cursor.execute("SELECT * FROM reminders WHERE user_id = ?", (user_id,))
                rows = cursor.fetchall()
                reminders = [Reminder(row[0], row[1], row[2], row[3], row[4]) for row in rows]
                return reminders
        except sqlite3.Error as e:
            print(f"Error getting reminders: {e}")
            return []

    def AddRemindInDb(self, reminder):
        try:
            with sqlite3.connect(self.database_file) as con:
                cursor = con.cursor()
                cursor.execute("INSERT INTO reminders (user_id, name, on_off, time) VALUES (?, ?, ?, ?)", 
                              (reminder.user_id, reminder.name, reminder.on_off, reminder.time))
                con.commit()
                print("Reminder added.")
        except sqlite3.Error as e:
            print(f"Error adding reminder: {e}")

    def DelRemindInDb(self, reminder_id):
        try:
            with sqlite3.connect(self.database_file) as con:
                cursor = con.cursor()
                cursor.execute("DELETE FROM reminders WHERE id = ?", (reminder_id,))
                if cursor.rowcount > 0:
                    con.commit()
                    print("Reminder deleted.")
                else:
                    print("Reminder not found.")
        except sqlite3.Error as e:
            print(f"Error deleting reminder: {e}")
# class RemindersRep:
#     def __init__(self):
#         self.file_name = "Reminders.json"
#         self.Reminders = self.load_reminders_from_file()

#     def create_table_if_not_exists(self):
#         try:
#             with sqlite3.connect(self.database_file) as con:
#                 cursor = con.cursor()
#                 cursor.execute("""
#                 CREATE TABLE IF NOT EXISTS reminders (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     user_id INTEGER
#                     name TEXT
#                     on_off INTEGER
#                     time TEXT
#                 )
#                 """)
#         except sqlite3.Error as e:
#             print(f"Error creating table: {e}")    
        
#     def load_reminders_from_file(self):
#         try:
#             with open(self.file_name, 'r') as file:
#                 reminders_data = json.load(file)
#                 reminders = [Reminder.from_dict(reminder_dict) for reminder_dict in reminders_data]
#                 return reminders
#         except FileNotFoundError:
#             return []
#         except Exception as e:
#             print("Произошла ошибка при чтении файла напоминаний:", str(e))
#             return []

#     def write_reminders_to_file(self):
#         reminders_data = [reminder.to_dict() for reminder in self.Reminders]
#         try:
#             with open(self.file_name, 'w') as file:
#                 json.dump(reminders_data, file)
#         except Exception as e:
#             print("Произошла ошибка при записи в файл напоминаний:", str(e))

#     def GetRemindsByUserId(self, user_id):
#         user_reminders = []
#         for reminder in self.Reminders:
#             if reminder.user_id == user_id:
#                 user_reminders.append(reminder)
#         return user_reminders

#     def AddRemindInDb(self, reminder):
#         try:
#             self.Reminders.append(reminder)
#             self.write_reminders_to_file()
#             print("Reminder добавлен.")
#         except Exception as e:
#             print("Произошла ошибка при добавлении напоминания в базу данных:", str(e))

#     def DelRemindInDb(self, reminder_id):
#         try:
#             for reminder in self.Reminders:
#                 if reminder.id == reminder_id:
#                     self.Reminders.remove(reminder)
#                     self.write_reminders_to_file()
#                     print("Reminder удален.")
#                     return
#             print("Reminder не найден.")
#         except Exception as e:
#             print("Произошла ошибка при удалении напоминания из базы данных:", str(e))