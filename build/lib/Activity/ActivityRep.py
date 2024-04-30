import json
from Activity.Activity import Activity

class ActivityRep:
    def __init__(self):
        self.file_name = "Activities.json"
        self.activities = self.load_activities_from_file()



    def GetActivityByName(self, name):
        for activity in self.activities:
            if activity.name == name:
                return activity
        return None

    def GetAllActivities(self):
            try:
                self.activities = self.load_activities_from_file()
                return self.activities
            except Exception as e:
                print(f"Ошибка при чтении файла: {e}")

    def WriteActivityInDb(self, activity):
        try:
            self.activities.append(activity)
            self.WriteActivitiesToFile()
            print("Activity written to database")
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}") 

    def WriteActivitiesToFile(self):
        # Преобразование списка активностей в список словарей
        activities_data = [activity.__dict__ for activity in self.activities]

        # Запись данных в файл в формате JSON
        with open(self.file_name, 'w') as file:
            json.dump(activities_data, file)

        print("Activities written to file")

    def load_activities_from_file(self):
        try:
            with open(self.file_name, 'r') as file:
                activities_data = json.load(file)
                activities = [Activity(**activity_data) for activity_data in activities_data]
                return activities
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return []