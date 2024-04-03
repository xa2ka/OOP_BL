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

    NameOfProduct=("Write name of Product: ")
            
    for prod in ProdRep.ProdList:
        if NameOfProduct == prod.name:
            product = ProdServo.GetProdForCalculating(NameOfProduct)
            UserProdServ.addUserProd()
            weight=input("Write weight of product in grams: ")
            UserProd=UserProd()
            UserProdServo.addUserProd(UserProd,product)



def AddWaterForUser():
            MlOfWater = input("Enter the amount of water: ")
            #Добавить дату
            Water=Water()
            Water.user_id = user.id
            Water.ml=MlOfWater()
            WaterServo.addWater()


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
            activity = ActivityServ.GetActByName(name_act)
            time_min = int(input("Enter time of your activity: "))
            UserActo = UserAct(name_act, user.id,current_date,0,time_min)
            UserActServo.addUserAct(UserActo)

    if ans=="2":
        Date=input("Enter date for statistic")
        WatLst=WaterServ.GetwaterByDate(Date)
        WaterSum=0
        for wat in WatLst:
            WaterSum+=wat.ml
        print(f"The amount of water: {WaterSum}")    

        UserProdLst=UserProdServ.GetUserProdByDate(Date)
        ProtSum=0
        FatSum=0
        CarbsSum=0
        for UserProd in UserProdLst:
            ProtSum+=UserProd.protein
            FatSum+=UserProd.fats
            CarbsSum+=UserProd.carbs
        print(f"The amount of protein: {ProtSum}\n"
            f"The amount of fats: {FatSum}\n"
            f"The amount of carbs: {CarbsSum}\n")  

        print(f"Callories in activity: {UserActServo.GetUserActByDate(user.id,current_date)}")


    if ans=="3":
        pass 

    if ans=="4":
        pass

    if ans=="5":
        print(UserServo.logIn())             


        
            # ProductForUser=Product()
            # ProductForUser.name=input("Write name of your product: ")
            # ProductForUser.cal=float(input("Write callories of your product: "))
            # ProductForUser.fats=float(input("Write fats of your product: "))
            # ProductForUser.carbs=float(input("Write carbs of your product: "))
            # ProductForUser.protein=float(input("Write protein of your product: "))   
            # ProdList.WriteProdInDb(ProductForUser)
            # Вывод списка ProdList         
        