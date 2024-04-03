from Activity.Activity import Activity


class ActivityRep:
    ActList = []

    def __init__(self):
        Activity1 = Activity(1, 100, "RUNNING")
        Activity2 = Activity(2, 200, "SWIMMING")
        Activity3 = Activity(3, 150, "CYCLING")
        Activity4 = Activity(4, 120, "YOGA")
        Activity5 = Activity(5, 180, "HIKING")
        self.ActList.extend([Activity1, Activity2, Activity3, Activity4, Activity5])
    
    def GetActivityByName(self, name):
        for activity in self.ActList:
            if activity.name == name:
                return activity
        return None

    def WriteActivityInDb(self, activity):
        self.ActList.append(activity)
        print("Activity written to database")