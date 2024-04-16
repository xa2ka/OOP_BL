from Product.Product import Product
import json


class ProdRep:
    ProdList=[]
    def __init__(self):
        self.file_name = "Product.json"
        self.ProdList = self.load_product_data_from_file()

        if not self.ProdList:
            self.initialize_data()

    def GetAllProducts(self):
        try:
            self.ProdList = self.load_product_data_from_file()
            return self.ProdList
        except Exception as e:
            print(f"Error: {e}")

    def GetProdForCalculating(self, name):
        self.ProdList=self.load_product_data_from_file()
        for prod in self.ProdList:
            if prod.name == name:
                return prod
        return None

    def WriteProdInDb(self, product):
        try:
            self.ProdList.append(product)
            self.write_product_data_to_file()
            print("Product data written to database")
        except Exception as e:
            print(f"Error: {e}")

    def write_product_data_to_file(self):
        product_data = [prod.to_dict() for prod in self.ProdList]

        with open(self.file_name, 'w') as file:
            json.dump(product_data, file)

        print("Product data written to file")

    def load_product_data_from_file(self):
        try:
            with open(self.file_name, 'r') as file:
                product_data = json.load(file)
                products = [Product.from_dict(prod_dict) for prod_dict in product_data]
                return products
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Error while reading file: {e}")
            return []

    def create_file(self):
        with open(self.file_name, 'w') as file:
            json.dump([], file)
        print("File created:", self.file_name)


    def initialize_data(self):
        products = [
            Product(id=1, name="MEAT", cal=100, fats=5, carbs=20, protein=10),
            Product(id=2, name="MILK", cal=150, fats=8, carbs=25, protein=15),
            Product(id=3, name="BREAD", cal=80, fats=2, carbs=15, protein=5),
            Product(id=4, name="EGGS", cal=70, fats=5, carbs=1, protein=6),
            Product(id=5, name="APPLE", cal=50, fats=0, carbs=15, protein=0),
            Product(id=6, name="YOGURT", cal=120, fats=3, carbs=10, protein=8),
            Product(id=7, name="CHICKEN", cal=150, fats=9, carbs=0, protein=20),
            Product(id=8, name="RICE", cal=200, fats=1, carbs=45, protein=4),
            Product(id=9, name="POTATO", cal=120, fats=0, carbs=30, protein=2),
            Product(id=10, name="SALMON", cal=250, fats=15, carbs=0, protein=25),
            Product(id=11, name="BANANA", cal=90, fats=0, carbs=23, protein=1),
            Product(id=12, name="CHEESE", cal=180, fats=12, carbs=2, protein=14),
            Product(id=13, name="TOMATO", cal=20, fats=0, carbs=5, protein=1),
            Product(id=14, name="SPINACH", cal=10, fats=0, carbs=2, protein=1),
            Product(id=15, name="CARROT", cal=30, fats=0, carbs=7, protein=1),
            Product(id=16, name="ORANGE", cal=60, fats=0, carbs=15, protein=1),
            Product(id=17, name="CUCUMBER", cal=10, fats=0, carbs=2, protein=0),
            Product(id=18, name="OATMEAL", cal=150, fats=3, carbs=27, protein=5),
            Product(id=19, name="BROCCOLI", cal=55, fats=0, carbs=11, protein=5),
            Product(id=20, name="ALMONDS", cal=160, fats=14, carbs=6, protein=6),
        ]
        self.ProdList.extend(products)
        self.write_product_data_to_file()