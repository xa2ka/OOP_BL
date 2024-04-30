from Water.Water import Water
import json


class WaterRep:
    def __init__(self):
        self.file_name = "Water.json"
        self.WaterList = self.load_water_data_from_file()

    def GetWaterByUserData(self, user_id, date):
        user_waters = []
        for water in self.WaterList:
            if water.user_id == user_id and water.date == date:
                user_waters.append(water)
        return user_waters

    def WriteWaterInDb(self, water):
        try:
            self.WaterList.append(water)
            self.write_water_data_to_file()
            print("Water data written to database")
        except Exception as e:
            print(f"Error: {e}")

    def write_water_data_to_file(self):
        water_data = [water.to_dict() for water in self.WaterList]

        with open(self.file_name, 'w') as file:
            json.dump(water_data, file)

        print("Water data written to file")

    def load_water_data_from_file(self):
        try:
            with open(self.file_name, 'r') as file:
                water_data = json.load(file)
                waters = [Water.from_dict(water_dict) for water_dict in water_data]
                return waters
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Error while reading file: {e}")
            return []

    def create_file(self):
        with open(self.file_name, 'w') as file:
            json.dump([], file)
        print("File created:", self.file_name)