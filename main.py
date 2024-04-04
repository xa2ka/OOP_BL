from User.User import User
from User.UserServ import UserServ
# from User.UserRep import UserRep
# from Product.Product import Product
from Product.ProdRep import ProdRep
from Product.ProdServ import ProdServ
from UserProd.UserProdServ import UserProdServ
from UserAct.UserAct import UserAct
from Water.WaterServ import WaterServ
from Activity.ActivityServ import ActivityServ
from UserAct.UserActServ import UserActServ
from UserProd.UserProd import UserProd
from Water.Water import Water

import datetime
current_date = datetime.date.today()



user=User()

ProdServo=ProdServ()
UserServo=UserServ()
UserProdServo=UserProdServ()
WaterServo=WaterServ()
ActivityServo=ActivityServ()
UserActServo=UserActServ()


def WritingUserProd():

    for prod in ProdRep.ProdList:
        prod_info = vars(prod)
        for attr, value in prod_info.items():
            print(attr + ":", value)
            print("------------------")

    NameOfProduct=input("Write name of Product: ")
            
    for prod in ProdRep.ProdList:
        if NameOfProduct == prod.name:
            product = ProdServo.GetProdForCalculating(NameOfProduct)
        
    weight = int(input("Write weight of product in grams: "))
    UserProdo=UserProd()
    UserProdo.weight=weight
    UserProdo.date=0
    UserProdo.user_id=user.id
    UserProdServo.addUserProd(UserProdo,product)
    



def AddWaterForUser():
            MlOfWater = input("Enter the amount of water: ")
            #Добавить дату
            Watero=Water()
            Watero.user_id = user.id
            Watero.ml=MlOfWater
            WaterServo.addWater(Watero)


################################################# PROGRAMM


print("HELLO!\n\
      ITS FOOD DIARY!\n\
      If you have account please write: YES\n\
      else write: NO")

Answer=input("Your answer: ")

if Answer == "NO":
    user=UserServo.SignUp()
    UserServo.add_user(user)
        
else:
    user=UserServo.logIn()
    if user == None:
        answer = input("sign up?(YES/NO)")
        if answer=="YES":
            user=UserServo.SignUp()
            UserServo.add_user(user)
  
while True:

    print("MENU:\n \
       1)Add something\n\
       2)check statistics\n\
       5)check user in db\n")
       
  
    ans=input("Your answer: ")
    
    if ans=="1":
        ans2 = input("What you would like to add?\n"
                "1) Food\n"
                "2) Water\n"
                "3) Activity\n")
      
        if ans2=="1":
            WritingUserProd()

        elif ans2=="2":
            AddWaterForUser()

        elif ans2=="3":
            ActivityServo.GetAllActivities()
            name_act = input("Enter name of activity: ")
            activity = ActivityServo.GetActByName(name_act)
            time_min = int(input("Enter time of your activity: "))
            UserActServo.addUserAct(activity, user.id,time_min)

            for item in UserActServo.user_activity_repo.UserActList:
                print("Name:", item.name)
                print("User ID:", item.user_id)
                print("Calories:", item.cal)
                print("Number of Minutes:", item.number_min)
                print("Date:", item.date)
                print()  # Пустая строка для разделения вывода каждого элемента

# class UserAct:
#     def __init__(self, name="", user_id=0, data=0, cal=0, number_min=0):
#         self.name, self.user_id, self.activity_id, self.cal, self.number_min, self.data = \
#         name, user_id, cal, number_min, data


    if ans=="2":
        Date=int(input("Enter date for statistic: "))
        
        try: 
            WatLst=WaterServo.GetwaterByDate(user.id,Date)
            WaterSum=0
            for wat in WatLst:
                WaterSum+=wat.ml
            print(f"The amount of water: {WaterSum}")    
        except Exception as e:
            print(f"Ошибка: {e}")    

        try:
            UserProdLst = UserProdServo.GetUserProdByDate(user.id,Date)
            ProtSum=0
            FatSum=0
            CarbsSum=0
            CalSum=0

            for UserProd_ in UserProdLst:    
                ProtSum+=UserProd_.protein
                FatSum+=UserProd_.fats
                CarbsSum+=UserProd_.carbs
                CalSum+=UserProd_.cal
            print(f"The amount of protein: {ProtSum}\n"
                f"The amount of fats: {FatSum}\n"
                f"The amount of fats: {CalSum}\n"
                f"The amount of carbs: {CarbsSum}\n")  
            
        except Exception as e:
            print(f"Ошибка: {e}") 
        
        try:
            UserActList=UserActServo.GetUserActByDate(user.id,Date)
            CalOfUsersActs=0
            for user_act in UserActList:
                CalOfUsersActs+=user_act.cal

            print(f"Callories in activity: {CalOfUsersActs}")
        except Exception as e:
            print(f"Ошибка: {e}")

    if ans=="3":
        pass 

    if ans=="4":
        pass

    if ans=="5":
        print(UserServo.logIn())             
   
    # if ans == "6":
    #     date = int(input("Write date: "))
    #     lst = UserProdServo.GetUserProdByDate(user.id, date)
    #     print("---------------RESULT-----------------")
    #     for item in lst:
    #         print("User ID:", item.user_id)
    #         print("Name:", item.name)
    #         print("Calories:", item.cal)
    #         print("Protein:", item.protein)
    #         print("Carbs:", item.carbs)
    #         print("Fats:", item.fats)
    #         print("Date:", item.date)
    #         print("Weight:", item.weight)
    #         print()  # Пустая строка для разделения вывода каждого элемента