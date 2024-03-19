import ActivityRep
import Activity

class ActivityServ:
    
    def addAct(self, activity):
        try:
            
            activityRepo = ActivityRep()
            activityRepo.WriteInDb(activity)
            print("success")

        except Exception as e:
            print(f"Произошла ошибка при добавлении активности: {e}")
            # error
                   
        finally:
            pass