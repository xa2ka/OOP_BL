import RemindersRep



class RemindersServ:
    
    def addReminders(self,reminder,user_id):
        
        try:
    
            RemindersRepo=RemindersRep()
            RemindersRepo.AddRemindInDb(user_id,reminder)
            print("success")
            
        except Exception as e:
            print(f"Ошибка: {e}")

        finally:
            pass

    def deleteReminders(self,reminder):

        pass
    
    def GetRemindsByUserId(self,user_id):
        pass
