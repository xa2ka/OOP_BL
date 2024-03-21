import UserActivityRep

from Activity.ActivityRep import ActivityRep
class UserActServ:
    
    def addUserAct(self, user_activity):
        try:
            activity_repo = ActivityRep()
            activity = activity_repo.GetActivityById(user_activity.activity_id)

            user_activity.cal = activity.cal * user_activity.number_min

            user_activity_repo = UserActivityRep()

            user_activity_repo.WriteInDb(user_activity)

            print("Success")

        except Exception as e:
            print(f"Произошла ошибка: {e}")
      
   
    def deleteUserAct(self, user_activity):
        try:
            user_activity_repo = UserActivityRep()
            user_activity_repo.DelInDb(user_activity) 

        except Exception as e:
            print(f"Произошла ошибка: {e}")
        finally:
          pass

