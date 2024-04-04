from Activity.ActivityRep import ActivityRep
from Activity.Activity import Activity

class ActivityServ:
    activityRepo = ActivityRep()

    def GetAllActivities(self):
        activities = self.activityRepo.ActList
        if not activities:
            print("No activities found.")
        else:
            print("All activities:\n")
            for activity in activities:
                print(f"- Name: {activity.name}")

    def GetActByName(self,name):
        for activity in self.activityRepo.ActList:
            if activity.name == name:
                return activity   
        return None

    def addAct(self, activity):
        try:
            self.activityRepo.WriteActivityInDb(activity)
            print("success")
        except Exception as e:
            print(f"Произошла ошибка при добавлении активности: {e}")
            # error           
        finally:
            pass