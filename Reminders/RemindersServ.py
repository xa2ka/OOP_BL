import RemindersRep



class RemindersServ:
    
    def addReminders(self,reminder):
        
        try:
    
            RemindersRepo=RemindersRep()
            RemindersRepo.AddRemindInDb(reminder)
            print("success")
            
        except Exception as e:
            print(f"Ошибка: {e}")

        finally:
            pass

    def deleteReminders(self,reminder):
      
        try:

           RemindersRepo = RemindersRep()
           RemindersRepo.DelRemindInDb(reminder)
           print("Success")

        except Exception as e:
           
           print(f"Ошибка: {e}")
           return []
       
        finally:
            pass


    
    def GetRemindsByUserId(self, user_id):
        try:

           RemindersRepo = RemindersRep()
           reminds = RemindersRepo.GetRemindsByUserId(user_id) 
           return reminds
       
        except Exception as e:
           
           print(f"Ошибка: {e}")
           return []
       
