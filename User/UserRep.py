import json
# from User.User import User
from EntitiesForOOP.User import User
import sqlite3 as sq
import sqlite3

class UserRep:
    # def __init__(self):
    #     self.filename = "users.json"
    #     self.users = self.load_users_from_file()

    # def load_users_from_file(self):
    #     try:
    #         with open(self.filename, 'r') as file:
    #             users_data = json.load(file)
    #             users = [User(**user_data) for user_data in users_data]
    #             return users
    #     except FileNotFoundError:
    #         return []
    #     except Exception as e:
    #         print(f"Ошибка при чтении файла: {e}")
    #         return []

    # def save_users_to_file(self):
    #     try:
    #         users_data = [user.__dict__ for user in self.users]
    #         with open(self.filename, 'w') as file:
    #             json.dump(users_data, file)
    #         print("Пользователи сохранены в файл")
    #     except Exception as e:
    #         print(f"Ошибка при сохранении файла: {e}")

    # def GetUserByEmailPassword(self, email, password):
    #     self.users = self.load_users_from_file()
    #     for user in self.users:
    #         if user.email == email and user.password == password:
    #             return user
    #     return None

    # def GetUserById(self, user_id):
    #     for user in self.users:
    #         if user.id == user_id:
    #             return user
    #     return None

    def GetUserById(self, user_id):
        import sqlite3
        with sqlite3.connect("OOP.db") as con:
            cur = con.cursor()
            
            # Выбрать пользователя из таблицы users по user_id
            cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
            user_data = cur.fetchone()
            
            if user_data:
                # Создать объект пользователя с данными из базы данных
                user = User(
                    id=user_data[0],
                    name=user_data[1],
                    surname=user_data[2],
                    email=user_data[3],
                    password=user_data[4],
                    old_year=user_data[5],
                    weight=user_data[6],
                    weight_goal=user_data[7],
                    cal_goal=user_data[8],
                    gender=user_data[9],
                    water_goal=user_data[10]
                )
                return user
            else:
                return None
            

    def GetUserByEmailPassword(self, email, password):
        import sqlite3
        with sqlite3.connect("OOP.db") as con:
            cur = con.cursor()
            
            # Выбрать пользователя из таблицы users по email и password
            cur.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
            user_data = cur.fetchone()
            
            if user_data:
                # Создать объект пользователя с данными из базы данных
                user = User(
                    id=user_data[0],
                    name=user_data[1],
                    surname=user_data[2],
                    email=user_data[3],
                    password=user_data[4],
                    old_year=user_data[5],
                    weight=user_data[6],
                    weight_goal=user_data[7],
                    cal_goal=user_data[8],
                    gender=user_data[9],
                    water_goal=user_data[10]
                )
                return user
            else:
                return None
        
    # def WriteInDb(self, user):
        # try:
        #     for existing_user in self.users:
        #         if existing_user.id == user.id:
        #             existing_user.update(user)
        #             self.save_users_to_file()
        #             return

        #     # Если пользователь с заданным идентификатором не найден, добавляем его в список
        #     user.id = len(self.users) + 1
        #     self.users.append(user)
        #     self.save_users_to_file()
        #     print("Пользователь добавлен в базу данных!")
        # except Exception as e:
        #     print(f"Ошибка: {e}")

    def WriteInDb(self, user):
        import sqlite3
        with sqlite3.connect("OOP.db") as con:
            cur = con.cursor()
            
            # Создание таблицы users, если она еще не существует
            cur.execute("""CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        surname TEXT,
                        email TEXT,
                        password TEXT,
                        old_year INTEGER,
                        weight REAL,
                        weight_goal REAL,
                        cal_goal REAL,
                        gender TEXT,
                        water_goal REAL
                        )""")


            # Вставка данных в таблицу users
            cur.execute("INSERT INTO users (name, surname, email, password, old_year, weight, weight_goal, cal_goal, gender, water_goal) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                    (user.name, user.surname, user.email, user.password, user.old_year, user.weight, user.weight_goal, user.cal_goal, user.gender, user.water_goal))
            # Получение последнего добавленного user_id
            user.user_id = cur.lastrowid
            con.commit()

    def DelUserInDb(self, user_id):
        import sqlite3
        try:
            with sqlite3.connect("OOP.db") as con:
                cur = con.cursor()
                
                # Проверка, существует ли такой пользователь в базе данных
                cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
                user = cur.fetchone()
                
                if user:
                    # Удаление пользователя из базы данных
                    cur.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
                    con.commit()
                    print(f"Пользователь с ID {user_id} удален")
                else:
                    print(f"Пользователь с ID {user_id} не найден")
        except Exception as e:
            print(f"Ошибка: {e}")

    # def UpdateUserInDb(self,user):
    #     try:
    #         for user_ in self.users:
    #             if user_.id == user.id:
    #                 user_=user
    #                 print("User was update")
    #                 self.save_users_to_file()   
    #                 return     
    #     except Exception as e:
    #         print(f"Возникла ошибка: {e}")


    def UpdateUserInDb(self, user):
        try:
            # Connect to the SQLite database
            with sqlite3.connect("OOP.db") as con:
                cur = con.cursor()

                # Update the user data in the database
                cur.execute("UPDATE users SET name=?, surname=?, email=?, password=?, old_year=?, weight=?, weight_goal=?, cal_goal=?, gender=?, water_goal=? WHERE user_id=?",
                            (user.name, user.surname, user.email, user.password, user.old_year, user.weight, user.weight_goal, user.cal_goal, user.gender, user.water_goal, user.id))
                con.commit()
                print("User was updated")
        except Exception as e:
            print(f"Error occurred: {e}")