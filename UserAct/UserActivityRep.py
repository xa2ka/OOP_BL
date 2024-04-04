

class UserActivityRep:
    UserActList = []

    def __init__(self):
        pass


    def GetUserActByDate(self, user_id, date):
        matching_user_acts = []
        
        for user_act in self.UserActList:
            
            print(user_act.user_id,user_id,user_act.date,date)

            if user_act.user_id == user_id and user_act.date == date:
                matching_user_acts.append(user_act)
        return matching_user_acts

    def WriteInDb(self, user_act,):
        self.UserActList.append(user_act)
        print("User activity written to database")

    # def DelInDb(self, user_id):
    #     # Удаляем записи из UserActList по user_id
    #     self.UserActList = [user_act for user_act in self.UserActList if user_act.user_id != user_id]
    #     print("User activity deleted from database")