class RemindersRep:
    Reminders = []

    def __init__(self):
        pass

    def GetRemindsByUserId(self, user_id):
        try:
            user_reminders = []
            for reminder in self.Reminders:
                if reminder.user_id == user_id:
                    user_reminders.append(reminder)
            return user_reminders
        except Exception as e:
            print("Произошла ошибка при получении напоминаний по идентификатору пользователя:", str(e))
            return []

    def AddRemindInDb(self, reminder):
        try:
            self.Reminders.append(reminder)
            print("Reminder добавлен.")
        except Exception as e:
            print("Произошла ошибка при добавлении напоминания в базу данных:", str(e))

    def DelRemindInDb(self, reminder_id):
        try:
            for reminder in self.Reminders:
                if reminder.id == reminder_id:
                    self.Reminders.remove(reminder)
                    print("Reminder удален.")
                    return
            print("Reminder не найден.")
        except Exception as e:
            print("Произошла ошибка при удалении напоминания из базы данных:", str(e))