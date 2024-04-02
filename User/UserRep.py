from User.User import User

class UserRep:
   
    users = []
    
    def __init__(self):
        pass 
    
    def GetUserByEmailPassword(self, email,password):
     
          for user in self.users:
              if user.email == email and user.password == password:
                 return user
              else:
                 return None

    
    def GetUserById(self, user_id):
      try:
          for user in self.users:
              if user.id == user_id:
                 return user
      except Exception as e:
        print(f"ОШИБКА: {e}")
      return None

    def WriteInDb(self, user):
      try:
          for i, existing_user in enumerate(self.users):
              if existing_user.id == user.id:
                  self.users[i] = user
                  print("User data was updated!")
                  return
          # Если пользователь с заданным идентификатором не найден, добавляем его в список
          user.id = len(self.users) + 1
          self.users.append(user)
          print("User was added!")
      except Exception as e:
          print(f"Ошибка: {e}")

    def DelUserInDb(self, user_id):
      try:
        for user in self.users:
          if user.id == user_id:
            self.users.remove(user) 
            print(f"User with {user_id} was DELETED")
      except Exception as e:
        print(f"Ошибка: {e}")
        # Удалить пользователя из базы данных по идентификатору user_id
