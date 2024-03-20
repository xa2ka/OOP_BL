from UserProdRep import UserProdRep
from ProdRep import ProdRep

class UserProdServ:
    
    def addUserProd(self, user_prod):
        try:
            user_prod_repo = UserProdRep()
            prod_repo = ProdRep()
          
            product = prod_repo.GetProdById(user_prod.prod_id)
          
            user_prod.cal = product.cal * user_prod.weight
            user_prod.carbs = product.carbs * user_prod.weight
            user_prod.fats = product.fats * user_prod.weight
            user_prod.protein = product.protein * user_prod.weight
        
            user_prod_repo.WriteInDb(user_prod)
            print("Success")
        except Exception as e:
            print(f"Ошибка: {e}")
        
    def deleteUserProd(self, user_prod):
         try:
           user_prod_repo = UserProdRep()
           user_prod_repo.DelInDb(user_prod)
       
           print("Success")
         except Exception as e:
           print(f"Ошибка: {e}")