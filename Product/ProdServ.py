import ProdRep
import Product


class ProdServ:
    
    def addProd(self, prodForWriting):
        
        try:
        
          productRepo = ProdRep()
          productRepo.WriteProdInDb(prodForWriting)
          print("success")
        
        except Exception as e:
            #Обработка исключения
            print(f"Произошла ошибка:{e}")
       
        finally:
            pass
