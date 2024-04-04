from User.UserRep import UserRep
from User.User import User


class UserServ:

    UserRepo=UserRep()
    
    def logIn(self):
        try:
            email = input("Введите адрес электронной почты пользователя: ")
            password = input("Введите пароль пользователя: ")
            user = self.UserRepo.GetUserByEmailPassword(email,password)
            if user == None:
                print("Такого пользователя нет.")
                return 
            return user
        except Exception as e:
            print(f"Ошибка: {e}")
            return None
      

    def SignUp(self):
        try:
            id = None
            while id is None:
                try:
                    id = int(input("Введите ID пользователя: "))
                except ValueError:
                    print("Некорректный ввод. Пожалуйста, введите целое число.")

            name = input("Введите имя пользователя: ")

            surname = input("Введите фамилию пользователя: ")

            email = None
            while email is None:
                email = input("Введите адрес электронной почты пользователя: ")
                if "@" not in email or "." not in email:
                    print("Некорректный адрес электронной почты. Пожалуйста, введите правильный адрес.")

            password = input("Введите пароль пользователя: ")

            old_year = None
            while old_year is None:
                try:
                    old_year = int(input("Введите возраст пользователя: "))
                except ValueError:
                    print("Некорректный ввод. Пожалуйста, введите целое число.")

            weight = None
            while weight is None:
                try:
                    weight = float(input("Введите вес пользователя: "))
                except ValueError:
                    print("Некорректный ввод. Пожалуйста, введите число.")

            weight_goal = None
            while weight_goal is None:
                try:
                    weight_goal = float(input("Введите целевой вес пользователя: "))
                except ValueError:
                    print("Некорректный ввод. Пожалуйста, введите число.")

            cal_goal = None
            while cal_goal is None:
                try:
                    cal_goal = int(input("Введите целевое количество калорий пользователя: "))
                except ValueError:
                    print("Некорректный ввод. Пожалуйста, введите целое число.")

            gender = None
            while gender is None:
                gender = input("Введите пол пользователя: ")
                if gender.lower() not in ["м", "ж"]:
                    print("Некорректный ввод. Пожалуйста, введите 'м' для мужского пола или 'ж' для женского пола.")

            water_goal = None
            while water_goal is None:
                try:
                    water_goal = int(input("Введите целевое количество воды пользователя: "))
                except ValueError:
                    print("Некорректный ввод. Пожалуйста, введите целое число.")
         
            user = User(id, name, surname, email,
            password, old_year, weight, weight_goal,
            cal_goal, gender, water_goal)
            
            self.add_user(user)
            return user
        
        except Exception as e:
            print(f"Ошибка: {e}")
            return None


    def add_user(self,user):
        try:
            UserRepo = UserRep()
            UserRepo.WriteInDb(user)
            print("User was added!")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
    
    def update_attribute(self, user_id, attribute_name, new_value):
        try:
            user = self.UserRepo.GetUserById(user_id)
            setattr(user, attribute_name, new_value)
            self.UserRepo.WriteInDb(user)
            print(f"Атрибут '{attribute_name}' пользователя с ID {user_id} обновлен.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

            
    # def change_name(self, user_id, new_name):
    #     try:
    #         UserRepo = UserRep()
    #         user = UserRepo.GetUserById(user_id)
    #         user.name = new_name
    #         UserRepo.WriteInDb(user)
    #     except Exception as e:
    #         print(f"Произошла ошибка: {e}")
    

    # def change_surname(self, user_id, new_surname):
    #     try:     
    #         UserRepo = UserRep()            
    #         user = UserRepo.GetUserById(user_id)
    #         user.surname = new_surname  
    #     except Exception as e:
    #         print(f"Произошла ошибка: {e}") 
    #     else:
    #         UserRepo.WriteInDb(user_id)


    # def change_water_goal(self, user_id, new_water_goal):  
    #     try:     
    #         UserRepo = UserRep()            
    #         user = UserRepo.GetUserById(user_id)
    #         user.water_goal = new_water_goal   
    #     except Exception as e:
    #         print(f"Произошла ошибка: {e}")  
    #     else:
    #         UserRepo.WriteInDb(user_id)


    # def change_cal_goal(self, user_id, new_cal_goal):    
    #     try:    
    #         UserRepo = UserRep()            
    #         user = UserRepo.GetUserById(user_id)
    #         user.cal_goal = new_cal_goal  
    #     except Exception as e:
    #         print(f"Произошла ошибка: {e}")  
    #     else:
    #         UserRepo.WriteInDb(user_id)


    # def change_gender(self, user_id, new_gender):  
    #     try:    
    #         UserRepo = UserRep()            
    #         user = UserRepo.GetUserById(user_id)
    #         user.gender = new_gender 
    #     except Exception as e:
    #         print(f"Произошла ошибка: {e}") 
    #     else:
    #         UserRepo.WriteInDb(user_id)

    # def change_old_year(self, user_id, new_old_year):
    #     try:  
    #         UserRepo = UserRep()            
    #         user = UserRepo.GetUserById(user_id)
    #         user.old_year = new_old_year 
    #     except Exception as e:
    #         print(f"Произошла ошибка: {e}") 
    #     else:
    #         UserRepo.WriteInDb(user_id)


    # def change_weight_goal(self, user_id, new_weight_goal):
    #     try:    
    #         UserRepo = UserRep()  
    #         user = UserRepo.GetUserById(user_id)
    #         user.weight_goal = new_weight_goal 
    #     except Exception as e:
    #         print(f"Произошла ошибка: {e}")  
    #     else:
    #         UserRepo.WriteInDb(user_id)

    # def change_weight(self, user_id, new_weight):
    #     try:     
    #         UserRepo = UserRep()  
    #         user = UserRepo.GetUserById(user_id)
    #         user.weight = new_weight
    #     except Exception as e:     
    #         print(f"Произошла ошибка: {e}") 
    #     else:
    #         UserRepo.WriteInDb(user_id)
