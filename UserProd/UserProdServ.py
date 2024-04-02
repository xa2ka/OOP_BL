from UserProd import UserProdRep
from Product import ProdRep


class UserProdServ:
    user_prod_repo = UserProdRep()
    prod_repo = ProdRep()

    def addUserProd(self, user_prod, product):
        try:
            user_prod.name = product.name
            user_prod.cal = product.cal * user_prod.weight
            user_prod.carbs = product.carbs * user_prod.weight
            user_prod.fats = product.fats * user_prod.weight
            user_prod.protein = product.protein * user_prod.weight

            self.user_prod_repo.WriteInDb(user_prod)
            print("Success")
        except Exception as e:
            print(f"Ошибка: {e}")

    def deleteUserProd(self, user_prod):
        try:
            self.user_prod_repo.DelInDb(user_prod)
            print("Success")
        except Exception as e:
            print(f"Ошибка: {e}")

    def GetUserProdByDate(self, date):
        user_prods = []
        for prod in self.user_prod_repo.UserProdList:
            if prod.date == date:
                user_prods.append(prod)
        return user_prods