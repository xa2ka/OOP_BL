# from Reminders.Reminders import Reminder
from EntitiesForOOP.Reminders import Reminder
import json

class RemindersRep:
    def __init__(self):
        self.file_name = "Reminders.json"
        self.Reminders = self.load_reminders_from_file()

    def load_reminders_from_file(self):
        try:
            with open(self.file_name, 'r') as file:
                reminders_data = json.load(file)
                reminders = [Reminder.from_dict(reminder_dict) for reminder_dict in reminders_data]
                return reminders
        except FileNotFoundError:
            return []
        except Exception as e:
            print("Произошла ошибка при чтении файла напоминаний:", str(e))
            return []

    def write_reminders_to_file(self):
        reminders_data = [reminder.to_dict() for reminder in self.Reminders]
        try:
            with open(self.file_name, 'w') as file:
                json.dump(reminders_data, file)
        except Exception as e:
            print("Произошла ошибка при записи в файл напоминаний:", str(e))

    def GetRemindsByUserId(self, user_id):
        user_reminders = []
        for reminder in self.Reminders:
            if reminder.user_id == user_id:
                user_reminders.append(reminder)
        return user_reminders

    def AddRemindInDb(self, reminder):
        try:
            self.Reminders.append(reminder)
            self.write_reminders_to_file()
            print("Reminder добавлен.")
        except Exception as e:
            print("Произошла ошибка при добавлении напоминания в базу данных:", str(e))

    def DelRemindInDb(self, reminder_id):
        try:
            for reminder in self.Reminders:
                if reminder.id == reminder_id:
                    self.Reminders.remove(reminder)
                    self.write_reminders_to_file()
                    print("Reminder удален.")
                    return
            print("Reminder не найден.")
        except Exception as e:
            print("Произошла ошибка при удалении напоминания из базы данных:", str(e))