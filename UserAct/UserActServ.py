from UserAct.UserActivityRep import UserActivityRep
from UserAct.UserActivityRep import UserActivityRep


class UserActServ:

    user_activity_repo = UserActivityRep()
    
    def GetCalActiv(self,user_id,date):
        sumCal=0
        for user_act in self.user_activity_repo.UserActList:
            if user_act.user_id == user_id and user_act.date == date:
                sumCal+=user_act.cal
        return sumCal
        
    def addUserAct(self,activity, user_activity):
        try:
            user_activity.cal = activity.cal * user_activity.number_min
            self.user_activity_repo.WriteInDb(user_activity)
            print("Success")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def GetUserActByDate(self,user_id,date):
        try:
           
           self.user_activity_repo.GetUserActByDate(user_id, date)
        except Exception as e:
            print(f"Произошла ошибка: {e}")          
   
    # def deleteUserAct(self, user_activity):
    #     try:     
    #         self.user_activity_repo.DelInDb(user_activity) 
    #     except Exception as e:
    #         print(f"Произошла ошибка: {e}")
    #     finally:
    #       pass

