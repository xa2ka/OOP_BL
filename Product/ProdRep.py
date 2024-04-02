from Product.Product import Product
from Product.ProdRep import ProdRep


class ProdRep:
    ProdList = []
    ProdRepo=ProdRep()

    def __init__(self):
        product1 = Product(id=1, name="MEAT", cal=100, fats=5, carbs=20, protein=10)
        product2 = Product(id=2, name="MILK", cal=150, fats=8, carbs=25, protein=15)
        product3 = Product(id=3, name="BREAD", cal=80, fats=2, carbs=15, protein=5)
        product4 = Product(id=4, name="EGGS", cal=70, fats=5, carbs=1, protein=6)
        
        self.ProdList.append(product1)
        self.ProdList.append(product2)
        self.ProdList.append(product3)
        self.ProdList.append(product4) 

    def GetProdForCalculating(self, name):
        for prod in self.ProdList:
            if prod.name == name:
                return prod
        return None
    
    def WriteProdInDb(self, product):
        self.ProdList.append(product)