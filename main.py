from User.User import User
from User.UserServ import UserServ
from User.UserRep import UserRep
from Product.Product import Product
from Product.ProdRep import ProdRep
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
        

ProdList=ProdRep()
user=None 

print("HELLO!\n\
      ITS FOOD DIARY!\n\
      If you have account please write: YES\n\
      else write: NO")

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
  
################################################# PROGRAMM

while True:

    print("MENU:\n \
       1)Add something\n\
       2)check statistics\n\
       4)check from date\n\
       5)check user in db\n")
  
    ans=input("your answer: ")
    
    if ans=="1":
        ans2 = input("What you would like to add?\n"
                "1) Food\n"
                "2) Water\n"
                "3) Activity\n")
      
        if ans2=="1":
            # ProductForUser=Product()
            # ProductForUser.name=input("Write name of your product: ")
            # ProductForUser.cal=float(input("Write callories of your product: "))
            # ProductForUser.fats=float(input("Write fats of your product: "))
            # ProductForUser.carbs=float(input("Write carbs of your product: "))
            # ProductForUser.protein=float(input("Write protein of your product: "))   
            # ProdList.WriteProdInDb(ProductForUser)
         
            ProdRep = ProdRep()

            # Вывод списка ProdList
            for prod in ProdRep.ProdList:
                prod_info = vars(prod)
                for attr, value in prod_info.items():
                    print(attr + ":", value)
                print("------------------")

            NameOfProduct=("Wrie name of Product: ")
            
            for prod in ProdRep.ProdList:
                if NameOfProduct == prod.name:
                    Prod = ProdRep.GetProdForCalculating(NameOfProduct)
                    pass
                #СПРОСИТЬ!!!!!!!!!!!!!!!!!!!!!!!!!


        elif ans2==2:
            pass
        elif ans2==3:
             pass

    
    if ans=="2":
        pass 

    if ans=="3":
        pass 

    if ans=="4":
        pass

    if ans=="5":
        print(logIn(user))              
        