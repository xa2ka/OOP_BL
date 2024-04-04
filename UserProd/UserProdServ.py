from UserProd.UserProdRep import UserProdRep
from Product.ProdRep import ProdRep


class UserProdServ:
    user_prod_repo = UserProdRep()
    prod_repo = ProdRep()

    def addUserProd(self, user_prod, product):
        try:
            # print(self.user_prod_repo.UserProdList)

            user_prod.name = product.name
            user_prod.cal = product.cal * user_prod.weight
            user_prod.carbs = product.carbs * user_prod.weight
            user_prod.fats = product.fats * user_prod.weight
            user_prod.protein = product.protein * user_prod.weight

            self.user_prod_repo.WriteInDb(user_prod)
            print("Success")

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
            return user_prods