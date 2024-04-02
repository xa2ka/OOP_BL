class WaterRep:
    WaterList = []

    def __init__(self):
        pass 

    def GetWaterByUserData(self, user_id, date): 
        user_waters = []
        for water in self.WaterList:
            if water.user_id == user_id and water.date == date:
                user_waters.append(water)
        return user_waters

    def WriteWaterInDb(self, water):
        self.WaterList.append(water)