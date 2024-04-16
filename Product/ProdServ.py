from Product.ProdRep import ProdRep
# import Product


class ProdServ:
    productRepo = ProdRep()
    
    def AddProd(self, product):
        try:
            self.productRepo.WriteProdInDb(product)
            print("success")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def GetProdForCalculating(self, name):
        try:
            return self.productRepo.GetProdForCalculating(name)
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return None
    def GetAllProducts(self):
        try:
            return self.productRepo.GetAllProducts()
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return None