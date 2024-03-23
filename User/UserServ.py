from User.UserRep import UserRep

class UserServ:

    def add_user(self,user):
        try:
          
            UserRepo = UserRep()
            UserRepo.WriteInDb(user)
            print("User was added!")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
    



    def change_name(self, user_id, new_name):
   
        try:
          
            UserRepo = UserRep()
            user = UserRepo.GetUserById(user_id)
            user.name = new_name
            UserRepo.WriteInDb(user)

        except Exception as e:
            print(f"Произошла ошибка: {e}")
    

    def change_surname(self, user_id, new_surname):
       
        try:
          
            UserRepo = UserRep()            
            user = UserRepo.GetUserById(user_id)
            user.surname = new_surname
       
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        
        else:
            UserRepo.WriteInDb(user_id)

    def change_water_goal(self, user_id, new_water_goal):
     
        try:
        
            UserRepo = UserRep()            
            user = UserRepo.GetUserById(user_id)
            user.water_goal = new_water_goal
       
        except Exception as e:
            print(f"Произошла ошибка: {e}")
       
        else:
            UserRepo.WriteInDb(user_id)

    def change_cal_goal(self, user_id, new_cal_goal):
        
        try:
         
            UserRepo = UserRep()            
            user = UserRepo.GetUserById(user_id)
            user.cal_goal = new_cal_goal
      
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        
        else:
            UserRepo.WriteInDb(user_id)

    def change_gender(self, user_id, new_gender):
       
        try:
         
            UserRepo = UserRep()            
            user = UserRepo.GetUserById(user_id)
            user.gender = new_gender
      
        except Exception as e:
            print(f"Произошла ошибка: {e}")
       
        else:
            UserRepo.WriteInDb(user_id)

    def change_old_year(self, user_id, new_old_year):
  
        try:
        
            UserRepo = UserRep()            
            user = UserRepo.GetUserById(user_id)
            user.old_year = new_old_year
       
        except Exception as e:
            print(f"Произошла ошибка: {e}")
       
        else:
            UserRepo.WriteInDb(user_id)

    def change_weight_goal(self, user_id, new_weight_goal):
  
        try:
          
            UserRepo = UserRep()  
            user = UserRepo.GetUserById(user_id)
            user.weight_goal = new_weight_goal
       
        except Exception as e:
            print(f"Произошла ошибка: {e}")
       
        else:
            UserRepo.WriteInDb(user_id)

    def change_weight(self, user_id, new_weight):
  
        try:
           
            UserRepo = UserRep()  
            user = UserRepo.GetUserById(user_id)
            user.weight = new_weight
      
        except Exception as e:
           
            print(f"Произошла ошибка: {e}")
       
        else:
            UserRepo.WriteInDb(user_id)