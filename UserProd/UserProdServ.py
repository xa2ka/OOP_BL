from UserProd.UserProdRep import UserProdRep
from Product.ProdRep import ProdRep
from UserProd.UserProd import UserProd

class UserProdServ:
    user_prod_repo = UserProdRep()
    prod_repo = ProdRep()

    def addUserProd(self, user_prod, product):
        try:
            print(self.user_prod_repo.UserProdList)

            user_prod.name = product.name
            user_prod.cal = product.cal * user_prod.weight
            user_prod.carbs = product.carbs * user_prod.weight
            user_prod.fats = product.fats * user_prod.weight
            user_prod.protein = product.protein * user_prod.weight

            self.user_prod_repo.WriteInDb(user_prod)
            print("Success")
            print("UserProdList:")
            for item in self.user_prod_repo.UserProdList:
                print("Name:", str(item.name))
                print("Calories:", str(item.cal))
                print("Carbs:", str(item.carbs))
                print("Fats:", str(item.fats))
                print("Protein:", str(item.protein))
                print("Date:", str(item.date))
                print()  # Пустая строка для разделения вывода элементов

        except Exception as e:
            print("Error:", str(e))

    def deleteUserProd(self, user_prod):
        try:
            self.user_prod_repo.DelInDb(user_prod)
            print("Success")
        except Exception as e:
            print(f"Ошибка: {e}")

    def GetUserProdByDate(self,user_id, date):
            user_prods = []
            for user_prod in self.user_prod_repo.UserProdList:
                if user_prod.date == date and user_id==user_prod.user_id:
                    user_prods.append(user_prod)
          
            for item in user_prods:
                print("User ID:", item.user_id)
                print("Name:", item.name)
                print("Calories:", item.cal)
                print("Protein:", item.protein)
                print("Carbs:", item.carbs)
                print("Fats:", item.fats)
                print("Date:", item.date)
                print("Weight:", item.weight)
                print()  # Пустая строка для разделения вывода каждого элемента
            return user_prods