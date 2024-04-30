# from UserAct.UserAct import UserAct
from EntitiesForOOP.UserAct import UserAct
import datetime
import json


class UserActivityRep:
    def __init__(self):
        self.file_name = "UserActivities.json"
        self.UserActs = self.load_user_activities_from_file()

    def GetUserActByDate(self, user_id, date):
        matching_user_acts = []

        for user_act in self.UserActs:
            if user_act.user_id == user_id and user_act.date == date:
                matching_user_acts.append(user_act)
        return matching_user_acts

    def WriteInDb(self, user_act):
        try:
            self.UserActs.append(user_act)
            self.WriteUserActivitiesToFile()
            print("User activity written to database")
        except Exception as e:
            print(f"Ошибка: {e}")

    def DelInDb(self, user_id):
        self.UserActs = [user_act for user_act in self.UserActs if user_act.user_id != user_id]
        print("User activity deleted from database")

    def WriteUserActivitiesToFile(self):
        user_activities_data = [user_act.to_dict() for user_act in self.UserActs]

        with open(self.file_name, 'w') as file:
            json.dump(user_activities_data, file)

        print("User activities written to file")

    def load_user_activities_from_file(self):
        user_act=UserAct()
        try:
            with open(self.file_name, 'r') as file:
                user_activities_data = json.load(file)
                user_activities = [UserAct.from_dict(user_act_data) for user_act_data in user_activities_data]
                return user_activities
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return []

    def create_file(self):
        with open(self.file_name, 'w') as file:
            json.dump([], file)
        print("File created:", self.file_name)