class UserProdRep:
    UserProdList = []

    def __init__(self):
        pass


    def WriteInDb(self, UserProd):
        self.UserProdList.append(UserProd)

    def DelInDb(self, userProd):  
        for prod in self.UserProdList:
            if prod.name == userProd.name:
                self.UserProdList.remove(prod)