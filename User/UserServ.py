from User.UserRep import UserRep
# from User.User import User
from EntitiesForOOP.User import User


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
            id = None
            # while id is None:
            #     try:
            #         id = int(input("Введите ID пользователя: "))
            #         for user in self.UserRepo.users:
            #             if id == user.id:
            #                 print("Некорректный ввод. Пользователь с таким id уже есть.")
            #                 id=None
            #                 break
            #     except ValueError:
            #         print("Некорректный ввод. Пожалуйста, введите целое число.")
            #         continue
                    
            name = input("Введите имя пользователя: ")

            surname = input("Введите фамилию пользователя: ")

            email = None
            while email is None:
                email = input("Введите адрес электронной почты пользователя: ")
                if "@" not in email or "." not in email:
                    print("Некорректный адрес электронной почты. Пожалуйста, введите правильный адрес.")
                    email = None
                    
            password = input("Введите пароль пользователя: ")
            old_year = None
            while old_year is None:
                try:
                    old_year = int(input("Введите возраст пользователя: "))
                except ValueError:
                    print("Некорректный ввод. Пожалуйста, введите целое число.")
                    continue
                    
            weight = None
            while weight is None:
                try:
                    weight = float(input("Введите вес пользователя: "))
                except ValueError:
                    print("Некорректный ввод. Пожалуйста, введите число.")
                    continue
                    
            weight_goal = None
            while weight_goal is None:
                try:
                    weight_goal = float(input("Введите целевой вес пользователя: "))
                except ValueError:
                    print("Некорректный ввод. Пожалуйста, введите число.")
                    continue
                    
            cal_goal = None
            while cal_goal is None:
                try:
                    cal_goal = int(input("Введите целевое количество калорий пользователя: "))
                except ValueError:
                    print("Некорректный ввод. Пожалуйста, введите целое число.")
                    continue
                    
            gender = None
            while gender is None:
                gender = input("Введите пол пользователя: ")
                if gender.lower() not in ["m", "w"]:
                    print("Некорректный ввод. Пожалуйста, введите 'м' для мужского пола или 'ж' для женского пола.")

            water_goal = None
            while water_goal is None:
                try:
                    water_goal = int(input("Введите целевое количество воды пользователя: "))
                except ValueError:
                    print("Некорректный ввод. Пожалуйста, введите целое число.")
                    continue
                    
            user = User(id, name, surname, email,
            password, old_year, weight, weight_goal,
            cal_goal, gender, water_goal)
            
            self.add_user(user)
            return user

    def add_user(self,user):
        try:
            self.UserRepo.WriteInDb(user)
            print("User was added!")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
    

            
    def change_user_data(self, user_id, field_name, new_value):
        try:
         
            user = self.UserRepo.GetUserById(user_id)
            
            setattr(user, field_name, new_value)
            
            self.UserRepo.UpdateUserInDb(user)
        except Exception as e:
            print(f"Произошла ошибка: {e}")