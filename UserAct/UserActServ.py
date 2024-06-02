from UserAct.UserActivityRep import UserActivityRep
# from UserAct.UserAct import UserAct
from EntitiesForOOP.UserAct import UserAct
from EntitiesForOOP.Activity import Activity



class UserActServ:
    def __init__(self):
        self.user_activity_repo = UserActivityRep()

    def GetCalActiv(self,user_id,date):
        sumCal=0
        for user_act in self.user_activity_repo.GetUserActList():
            if user_act.user_id == user_id and user_act.date == date:
                sumCal+=user_act.cal
        return sumCal
                  
                    # UserActServo.addUserAct(activity, user.id,time_min)

    def addUserAct(self,activity,user_id,time_min,date):
        # try:
           user_activity=UserAct()
           user_activity.name = activity.name
           user_activity.user_id=user_id
           user_activity.number_min=time_min
           user_activity.cal=activity.cal * time_min
           user_activity.date=date
           self.user_activity_repo.WriteInDb(user_activity)
           print("Success")
        # except Exception as e:
        #     print(f"Произошла ошибка: {e}")

    def GetUserActByDate(self,user_id,date):
        try:
           return  self.user_activity_repo.GetUserActByDate(user_id, date)
        except Exception as e:
            print(f"Произошла ошибка: {e}")          
   
    # def deleteUserAct(self, user_activity):
    #     try:     
    #         self.user_activity_repo.DelInDb(user_activity) 
    #     except Exception as e:
    #         print(f"Произошла ошибка: {e}")
    #     finally:
    #       pass

