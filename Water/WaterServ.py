from Water.WaterRep import WaterRep


class WaterServ:
    def __init__(self): 
        self.WaterRepo = WaterRep()    

    def addWater(self, water):
        try:
            self.WaterRepo.addWater(water)
            print("success")
        except Exception as e:
            print(f"Ошибка: {e}")
        finally:
            pass
          
    def GetwaterByDate(self,user_id,date):
        try:
            water_list = self.WaterRepo.GetwaterByDate(user_id, date)
            return water_list
        except Exception as e:
            print(f"Ошибка: {e}")
            return []