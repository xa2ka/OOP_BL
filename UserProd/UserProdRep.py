# from UserProd.UserProd import UserProd
from EntitiesForOOP.UserProd import UserProd
import json

class UserProdRep:
    def __init__(self):
        self.file_name = "UserProductData.json"
        self.UserProdList = self.load_user_product_data_from_file()

    def WriteInDb(self, userProd):
        try:
            self.UserProdList.append(userProd)
            self.write_user_product_data_to_file()
            print("User product data written to database")
        except Exception as e:
            print(f"Error: {e}")

    def DelInDb(self, userProd):
        try:
            self.UserProdList = [prod for prod in self.UserProdList if prod.name != userProd.name]
            self.write_user_product_data_to_file()
            print("User product data deleted from database")
        except Exception as e:
            print(f"Error: {e}")

    def write_user_product_data_to_file(self):
        user_product_data = [userProd.to_dict() for userProd in self.UserProdList]

        with open(self.file_name, 'w') as file:
            json.dump(user_product_data, file)

        print("User product data written to file")

    def load_user_product_data_from_file(self):
        user_product_data = []

        try:
            with open(self.file_name, 'r') as file:
                user_product_data = json.load(file)
        except FileNotFoundError:
            print("User product data file not found. Starting with an empty list.")

        user_products = [UserProd.from_dict(data_dict) for data_dict in user_product_data]
        return user_products