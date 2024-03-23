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
       #( Получить пользователя из базы данных по идентификатору user_id)
       #( и вернуть объект пользователя)

    def WriteInDb(self, user):
        
        try:
        
           user.id = len(self.users)+1
           self.users.append(user)
       
        except Exception as e:
           print(f"ОШИБКА: {e}")
    
       # Записать данные пользователя с идентификатором user_id в базу данных

    def DelUserInDb(self, user_id):
      try:
        for user in self.users:
          if user.id == user_id:
            self.users.remove(user) 
            print(f"User with {user_id} was DELETED")
      except Exception as e:
        print(f"Ошибка: {e}")
        # Удалить пользователя из базы данных по идентификатору user_id

    def UpdateInDb(self,user_id):
       for user in self.users:
           if user.id== user_id:
               pass
