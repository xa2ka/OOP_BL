# from Product.Product import Product
from EntitiesForOOP.Product import Product
import json
import sqlite3

class ProdRep:
    def __init__(self):
            self.db_file = "OOP.db"
            self.create_table_if_not_exists()
            self.add_russian_products()

    def create_table_if_not_exists(self):
            try:
                with sqlite3.connect(self.db_file) as conn:
                    cursor = conn.cursor()
                    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS products (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            cal REAL,
                            fats REAL,
                            carbs REAL,
                            protein REAL
                        )
                    """)
            except sqlite3.Error as e:
                print(f"Error creating table: {e}")

    def GetAllProducts(self):
            try:
                with sqlite3.connect(self.db_file) as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM products")
                    rows = cursor.fetchall()
                    return [Product(id=row[0], name=row[1], cal=row[2], fats=row[3], carbs=row[4], protein=row[5]) for row in rows]
            except sqlite3.Error as e:
                print(f"Error getting products: {e}")
                return []

    def GetProductForCalculating(self, name):
            try:
                with sqlite3.connect(self.db_file) as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM products WHERE name = ?", (name,))
                    row = cursor.fetchone()
                    if row:
                        return Product(id=row[0], name=row[1], cal=row[2], fats=row[3], carbs=row[4], protein=row[5])
                    else:
                        return None
            except sqlite3.Error as e:
                print(f"Error getting product: {e}")
                return None

    def WriteProdInDb(self, product):
            try:
                with sqlite3.connect(self.db_file) as conn:
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO products (name, cal, fats, carbs, protein) VALUES (?, ?, ?, ?, ?)",
                                (product.name, product.cal, product.fats, product.carbs, product.protein))
                    conn.commit()
                    print("Product data written to database")
            except sqlite3.Error as e:
                print(f"Error writing product: {e}")  

    def add_russian_products(self):
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                
                expanded_products = [
                    ("Стейк", 280, 17, 0, 26),
                    ("Курица гриль", 165, 3, 0, 31),
                    ("Лосось", 206, 12, 0, 22),
                    ("Тунец консервированный", 154, 4, 0, 25),
                    ("Яйца куриные", 155, 11, 1, 13),
                    ("Творог обезжиренный", 100, 0, 4, 18),
                    ("Сыр моцарелла", 285, 21, 6, 22),
                    ("Макароны отварные", 158, 1, 31, 6),
                    ("Рис отварной", 200, 0, 44, 4),
                    ("Гречневая каша", 116, 1, 23, 4),
                    ("Хлеб пшеничный", 265, 3, 50, 9),
                    ("Картофель отварной", 87, 0, 20, 2),
                    ("Брокколи отварная", 55, 0, 11, 3),
                    ("Шпинат отварной", 41, 0, 7, 5),
                    ("Куриная грудка запеченная", 165, 3, 0, 31),
                    ("Скумбрия консервированная", 208, 12, 0, 24),
                    ("Сельдь соленая", 208, 12, 0, 23),
                    ("Треска отварная", 182, 0, 0, 39),
                    ("Горбуша запеченная", 206, 12, 0, 23),
                    ("Помидоры черри", 18, 0, 4, 1),
                    ("Авокадо", 160, 15, 9, 2),
                    ("Киви", 61, 0, 15, 1),
                    ("Банан", 89, 0, 23, 1),
                    ("Яблоко", 52, 0, 14, 0),
                    ("Огурец", 15, 0, 3, 1),
                    ("Болгарский перец", 31, 0, 7, 1),
                    ("Морковь", 41, 0, 10, 1),
                    ("Орехи миндальные", 578, 50, 22, 21),
                    ("Семена льна", 534, 42, 28, 18),
                    ("Мюсли", 371, 8, 62, 11),
                    ("Овсяные хлопья", 389, 7, 67, 17),
                    ("Кефир 1%", 49, 3, 5, 3),
                    ("Йогурт греческий", 100, 0, 5, 17),
                    ("Куриные бёдра запечённые", 209, 13, 0, 19),
                    ("Колбаса варёная", 290, 25, 3, 13),
                    ("Шоколад тёмный 70%", 600, 43, 46, 8),
                    ("Ягоды лесные", 32, 0, 6, 1),
                    ("Финики", 282, 0, 75, 2),
                    ("Фундук", 654, 63, 17, 15),
                    ("Оливковое масло", 884, 100, 0, 0),
                    ("Сок томатный", 23, 0, 5, 2),
                    ("Вода негазированная", 0, 0, 0, 0)
                ]
                
                for product in expanded_products:
                    cursor.execute("INSERT INTO products (name, cal, fats, carbs, protein) VALUES (?, ?, ?, ?, ?)", product)
                conn.commit()
                print("40 new products added to the database.")
        except sqlite3.Error as e:
            print(f"Error adding expanded products: {e}")


    # ProdList=[]
    # def __init__(self):
    #     self.file_name = "Product.json"
    #     self.ProdList = self.load_product_data_from_file()

    #     if not self.ProdList:
    #         self.initialize_data()

    # def GetAllProducts(self):
    #     try:
    #         self.ProdList = self.load_product_data_from_file()
    #         return self.ProdList
    #     except Exception as e:
    #         print(f"Error: {e}")

    # def GetProdForCalculating(self, name):
    #     self.ProdList=self.load_product_data_from_file()
    #     for prod in self.ProdList:
    #         if prod.name == name:
    #             return prod
    #     return None

    # def WriteProdInDb(self, product):
    #     try:
    #         self.ProdList.append(product)
    #         self.write_product_data_to_file()
    #         print("Product data written to database")
    #     except Exception as e:
    #         print(f"Error: {e}")

    # def write_product_data_to_file(self):
    #     product_data = [prod.to_dict() for prod in self.ProdList]

    #     with open(self.file_name, 'w') as file:
    #         json.dump(product_data, file)

    #     print("Product data written to file")

    # def load_product_data_from_file(self):
    #     try:
    #         with open(self.file_name, 'r') as file:
    #             product_data = json.load(file)
    #             products = [Product.from_dict(prod_dict) for prod_dict in product_data]
    #             return products
    #     except FileNotFoundError:
    #         return []
    #     except Exception as e:
    #         print(f"Error while reading file: {e}")
    #         return []

    # def create_file(self):
    #     with open(self.file_name, 'w') as file:
    #         json.dump([], file)
    #     print("File created:", self.file_name)


    # def initialize_data(self):
    #     products = [
    #         Product(id=1, name="MEAT", cal=100, fats=5, carbs=20, protein=10),
    #         Product(id=2, name="MILK", cal=150, fats=8, carbs=25, protein=15),
    #         Product(id=3, name="BREAD", cal=80, fats=2, carbs=15, protein=5),
    #         Product(id=4, name="EGGS", cal=70, fats=5, carbs=1, protein=6),
    #         Product(id=5, name="APPLE", cal=50, fats=0, carbs=15, protein=0),
    #         Product(id=6, name="YOGURT", cal=120, fats=3, carbs=10, protein=8),
    #         Product(id=7, name="CHICKEN", cal=150, fats=9, carbs=0, protein=20),
    #         Product(id=8, name="RICE", cal=200, fats=1, carbs=45, protein=4),
    #         Product(id=9, name="POTATO", cal=120, fats=0, carbs=30, protein=2),
    #         Product(id=10, name="SALMON", cal=250, fats=15, carbs=0, protein=25),
    #         Product(id=11, name="BANANA", cal=90, fats=0, carbs=23, protein=1),
    #         Product(id=12, name="CHEESE", cal=180, fats=12, carbs=2, protein=14),
    #         Product(id=13, name="TOMATO", cal=20, fats=0, carbs=5, protein=1),
    #         Product(id=14, name="SPINACH", cal=10, fats=0, carbs=2, protein=1),
    #         Product(id=15, name="CARROT", cal=30, fats=0, carbs=7, protein=1),
    #         Product(id=16, name="ORANGE", cal=60, fats=0, carbs=15, protein=1),
    #         Product(id=17, name="CUCUMBER", cal=10, fats=0, carbs=2, protein=0),
    #         Product(id=18, name="OATMEAL", cal=150, fats=3, carbs=27, protein=5),
    #         Product(id=19, name="BROCCOLI", cal=55, fats=0, carbs=11, protein=5),
    #         Product(id=20, name="ALMONDS", cal=160, fats=14, carbs=6, protein=6),
    #     ]
    #     self.ProdList.extend(products)
    #     self.write_product_data_to_file()
