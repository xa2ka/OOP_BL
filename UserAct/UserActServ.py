import UserActivityRep

class UserActServ:
    
    def addUserAct(self,UserActivity):
      try:
         
         UserActivityRepo=UserActivityRep()
         UserActivityRepo.WriteActivityInDb(UserActivity)
         
         print("Success")

      except Exception as e:
         print(f"Произошла ошибка: {e}")
      
      finally:
         pass

    def deleteUserAct(self,UserActivity):
        
      try:
         UserActivityRepo=UserActivityRep()
         UserActivityRepo.DelInDb(UserActivity) 

      except Exception as e:
         print(f"Произошла ошибка: {e}")
      
      finally:
         pass