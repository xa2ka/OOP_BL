import json
from User.User import User

class UserRep:
    def __init__(self):
        self.filename = "users.json"
        self.users = self.load_users_from_file()

    def load_users_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                users_data = json.load(file)
                users = [User(**user_data) for user_data in users_data]
                return users
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return []

    def save_users_to_file(self):
        try:
            users_data = [user.__dict__ for user in self.users]
            with open(self.filename, 'w') as file:
                json.dump(users_data, file)
            print("Пользователи сохранены в файл")
        except Exception as e:
            print(f"Ошибка при сохранении файла: {e}")

    def GetUserByEmailPassword(self, email, password):
        self.users = self.load_users_from_file()
        for user in self.users:
            if user.email == email and user.password == password:
                return user
        return None

    def GetUserById(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def WriteInDb(self, user):
        try:
            for existing_user in self.users:
                if existing_user.id == user.id:
                    existing_user.update(user)
                    self.save_users_to_file()
                    return

            # Если пользователь с заданным идентификатором не найден, добавляем его в список
            user.id = len(self.users) + 1
            self.users.append(user)
            self.save_users_to_file()
            print("Пользователь добавлен в базу данных!")
        except Exception as e:
            print(f"Ошибка: {e}")

    def DelUserInDb(self, user_id):
        try:
            for user in self.users:
                if user.id == user_id:
                    self.users.remove(user)
                    self.save_users_to_file()
                    print(f"Пользователь с ID {user_id} удален")
                    return
            print(f"Пользователь с ID {user_id} не найден")
        except Exception as e:
            print(f"Ошибка: {e}")

    def UpdateUserInDb(self,user):
        try:
            for user_ in self.users:
                if user_.id == user.id:
                    user_=user
                    print("User was update")
                    self.save_users_to_file()   
                    return     
        except Exception as e:
            print(f"Возникла ошибка: {e}")