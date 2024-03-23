from User.User import User
from User.UserServ import UserServ
from User.UserRep import UserRep

UserServo=UserServ()

def logIn(user):
      email = input("Введите адрес электронной почты пользователя: ")
      password = input("Введите пароль пользователя: ")
      UserRepo=UserRep()
      user = UserRepo.GetUserByEmailPassword(email,password)
      return user
      

def SignUp(user):
    
        id = int(input("Введите ID пользователя: "))
        name = input("Введите имя пользователя: ")
        surname = input("Введите фамилию пользователя: ")
        email = input("Введите адрес электронной почты пользователя: ")
        password = input("Введите пароль пользователя: ")
        old_year = int(input("Введите возраст пользователя: "))
        weight = float(input("Введите вес пользователя: "))
        weight_goal = float(input("Введите целевой вес пользователя: "))
        cal_goal = int(input("Введите целевое количество калорий пользователя: "))
        gender = input("Введите пол пользователя: ")
        water_goal = int(input("Введите целевое количество воды пользователя: "))

        user = User(id, name, surname, email,
           password, old_year, weight, weight_goal,
           cal_goal, gender, water_goal)
        
        return user
        






user=None 
print("HELLO!\nITS FOOD DIARY!\nIf you have account please write: YES\nelse write: NO")
Answer=input("Your answer: ")
if Answer == "NO":
    user=SignUp(user)
    UserServo.add_user(user)
        
else:
    user=logIn(user)
    if user == None:
        answer = input("sign up?(YES/NO)")
        if answer=="YES":
            user=SignUp(user)
            UserServo.add_user(user)
  

while True:
    print("MENU:\n \
       1)Add something\n\
       2)check statistics\n\
       4)check from date\n\
       5)check user in db\n")
    ans=input("your answer: ")
    if ans=="5":
        print(logIn(user))           
        