import Water
import WaterRep

class WaterServ:
    
    def addWater(self,water):
        try:
          
          WaterRepo=WaterRep()
          WaterRepo.WriteInDb(water)
          print("success")
        except Exception as e:
          print(f"Ошибка: {e}")

        finally:
          pass

