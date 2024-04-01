import ProdRep
import Product


class ProdServ:
    
    def AddProd(self, product):
        
        try:
        
          productRepo = ProdRep()
          productRepo.WriteProdInDb(product)
          print("success")
        
        except Exception as e:
            #Обработка исключения
            print(f"Произошла ошибка:{e}")
       
        finally:
            pass

    def GetProdForCalculating(self,name):
        try:
            pass
        except Exception as e:
            pass
        finally:
            pass    
