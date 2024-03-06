import UserRep
import User

class UserServ:

    def change_name(self, user_id, new_name):       
     
      UserRepo = UserRep()

      user = UserRepo.GetUserById(user_id)
           
      if user:
            user.name = new_name
      else:
            #error   
         
       UserRepo.WriteInDb(user_id)
      

    def change_surname(self, user_id, new_surname):
      
      UserRepo = UserRep()

      user = UserRepo.GetUserById(user_id)
           
      if user:
            user.surname = new_surname
      else:
            #error   
     
          
       UserRepo.WriteInDb(user_id)

    def change_water_goal(self, user_id, new_water_goal):
      
      UserRepo = UserRep()

      user = UserRepo.GetUserById(user_id)
      
      if user:
            user.water_goal = new_water_goal
      else:
            #error 
       UserRepo.WriteInDb(user_id)

    def change_cal_goal(self, user_id, new_cal_goal):
      
      UserRepo = UserRep()

      user = UserRepo.GetUserById(user_id)
      
      if user:
            user.cal_goal = new_cal_goal
      else:
            #error 
       UserRepo.WriteInDb(user_id)
    

    def change_gender(self, user_id, new_gender):
       
      UserRepo = UserRep()

      user = UserRepo.GetUserById(user_id)
      
      if user:
            user.gender = new_gender
      else:
            #error 
       UserRepo.WriteInDb(user_id)

    def change_old_year(self, user_id, new_old_year):
       
      UserRepo = UserRep()

      user = UserRepo.GetUserById(user_id)
      
      if user:
            user.old_year = new_old_year
      else:
            #error 
       UserRepo.WriteInDb(user_id)

    def change_weight_goal(self, user_id, new_weight_goal):
       
      UserRepo = UserRep()

      user = UserRepo.GetUserById(user_id)
      
      if user:
            user.weight_goal = new_weight_goal
      else:
            #error 
       UserRepo.WriteInDb(user_id)

   
    def change_weigth(self, user_id, new_weight):
       
      UserRepo = UserRep()

      user = UserRepo.GetUserById(user_id)
      
      if user:
            user.weight = new_weight
      else:
            #error 
       UserRepo.WriteInDb(user_id)