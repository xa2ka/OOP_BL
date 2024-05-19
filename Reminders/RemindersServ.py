from Reminders.RemindersRep import RemindersRep



class RemindersServ:
    RemindersRepo=RemindersRep()  

    def addReminders(self,reminder):
        try:
            self.RemindersRepo.AddRemindInDb(reminder)
            print("success")
        except Exception as e:
            print(f"Ошибка: {e}")
        finally:
            pass

    def deleteReminders(self,reminder_id):
        try:
           self.RemindersRepo.DelRemindInDb(reminder_id)
           print("Success")
        except Exception as e:
           print(f"Ошибка: {e}")
           return []
        finally:
            pass
    
    def GetRemindsByUserId(self, user_id):
        try:
           reminds = self.RemindersRepo.GetRemindersByUserId(user_id) 
           return reminds
        except Exception as e:
           print(f"Ошибка: {e}")
           return []
       
