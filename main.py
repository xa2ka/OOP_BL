import datetime

# from Product.Product import Product
# from User.User import User
# from Water.Water import Water
# from Reminders.Reminders import Reminder
# from UserProd.UserProd import UserProd

import sqlite3 as sq
# ----------DONE-----
# Product 
# User
#


#  Water user_id=0, ml=0, date=None


# with sq.connect("OOP.db") as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE products(
#         product_id  INTEGER PRIMARY KEY,
#         name  TEXT NOT NULL,
#         cal  INTEGER,
#         fats  INTEGER,
#         carbs  INTEGER,
#         protein  INTEGER
#     )""")
 
from EntitiesForOOP.Product import Product
from EntitiesForOOP.User import User
from EntitiesForOOP.Water import Water
from EntitiesForOOP.Reminders import Reminder
from EntitiesForOOP.UserProd import UserProd
from EntitiesForOOP.Activity import Activity
from EntitiesForOOP.Water import Water
from User.UserServ import UserServ
from Product.ProdRep import ProdRep
from Product.ProdServ import ProdServ
from UserProd.UserProdServ import UserProdServ
from Water.WaterServ import WaterServ
from Activity.ActivityServ import ActivityServ
from UserAct.UserActServ import UserActServ
from Reminders.RemindersServ import RemindersServ
from User.UserRep import UserRep


import datetime
current_date = datetime.date.today()

user=User()

ProdServo=ProdServ()
UserServo=UserServ()
UserProdServo=UserProdServ()
WaterServo=WaterServ()
ActivityServo=ActivityServ()
UserActServo=UserActServ()
RemindersServo=RemindersServ()
UserRepo=UserRep()

def case_1():
    print("What would you like to add?\n"
                    "1) Food\n"
                    "2) Water\n"
                    "3) Activity\n")
    ans2 = input("Your answer: ")

    if ans2 == "1":
        WritingUserProd()

    elif ans2 == "2":
        AddWaterForUser()

    elif ans2 == "3":
        ActivityServo.GetAllActivities()
        name_act = input("Enter name of activity: ")
        activity_=Activity()
        activity_= ActivityServo.GetActByName(name_act)
        time_min = int(input("Enter time of your activity: "))

        date_str = input("Enter date for adding your activity(DD.MM.YYYY): ")
        Date = datetime.datetime.strptime(date_str, "%d.%m.%Y").date()
        
        UserActServo.addUserAct(activity_, user.id, time_min,Date)
                
    else:
        print("Invalid choice")
        return
    

def case_2():


        date_str = input("Enter date for checking Product List(DD.MM.YYYY): ")
        try:
            Date = datetime.datetime.strptime(date_str, "%d.%m.%Y").date()
        except ValueError:
            print("Некорректный формат даты. Пожалуйста, введите дату в правильном формате (дд.мм.гггг).")


        Date_str = Date.strftime("%Y-%m-%d")
        UserProdLst = UserProdServo.GetUserProdByDate(user.id, Date_str)

        print("User Product List:\n--------------------------")
        for user_prod in UserProdLst:
            print("Name:", user_prod.name)
            print("Calories:", user_prod.cal)
            print("Protein:", user_prod.protein)
            print("Carbs:", user_prod.carbs)
            print("Fats:", user_prod.fats)
            print("Date:", user_prod.date)
            print("Weight:", user_prod.weight)
            print("-------------------------")  # Add an empty line for better readability
        
        NameForDeleting=input("Enter name of product for deleting in your product list: ")
        for user_prod in UserProdLst:
            if NameForDeleting==user_prod.name:
                UserProdServo.deleteUserProd(user_prod)


def case_3():

    while True:
        date_str = input("Введите дату в формате дд.мм.гггг: ")
        try:
            Date = datetime.datetime.strptime(date_str, "%d.%m.%Y").date()
        except ValueError:
            print("Некорректный формат даты. Пожалуйста, введите дату в правильном формате (дд.мм.гггг).")
        else:
            break

    Date_str = Date.strftime("%Y-%m-%d")
    print("----------------STATISTICS--------------\n\n\n")
    print("----------------WATER----------------\n")
    try: 
        WatLst = WaterServo.GetwaterByDate(user.id,Date_str)
        WaterSum = 0
        for wat in WatLst:
            print(wat.ml)
            WaterSum += int(wat.ml)
        print(f"The amount of water: {WaterSum}")    
    except Exception as e:
        print(f"Ошибка: {e}") 
    print("The goal of water per day: ",user.water_goal)
    print("Remaining water(ml) per day",user.water_goal-WaterSum)

    print("----------------PRODUCTS----------------\n")
    CalSum = 0
    ProtSum = 0
    FatSum = 0
    CarbsSum = 0
    try:
        UserProdLst = UserProdServo.GetUserProdByDate(user.id, Date_str)

        for UserProd_ in UserProdLst:    
            ProtSum += UserProd_.protein
            FatSum += UserProd_.fats
            CarbsSum += UserProd_.carbs
            CalSum += UserProd_.cal
        print(f"The amount of protein: {ProtSum}\n"
            f"The amount of fats: {FatSum}\n"
            f"The amount of calories: {CalSum}\n"
            f"The amount of carbs: {CarbsSum}\n")  
    except Exception as e:
        print(f"ТУТ ОШИБКА: {e}") 

    print("the goal of calories per day: ",user.cal_goal)
    print("Remaining calories per day",user.cal_goal-CalSum)


    print("----------------ACTIVITIES----------------\n")
  
    try:
        UserActList = UserActServo.GetUserActByDate(user.id, Date_str)
        CalOfUsersActs = 0
        for user_act in UserActList:
            CalOfUsersActs += user_act.cal

        print(f"Calories burned in activities: {CalOfUsersActs}")
    except Exception as e:
        print(f"Error: {e}")

    print("----------------REMINDERS----------------\n")
     
    reminders = RemindersServo.GetRemindsByUserId(user.id)

    if len(reminders) > 0:
        print("Список ваших напоминаний:")
        print("-------------------------")
        for reminder in reminders:
            print("Название: ", reminder.name)
            print("Статус: ", "Включено" if reminder.on_off == 1 else "Выключено")
            print("Время: ", reminder.time)
            print("-------------------------")
    else:
        print("У вас нет сохраненных напоминаний.")


def case_4():
        try:
            date_str = input("Enter the date when the product was eaten (DD.MM.YYYY): ")
            # date = datetime.datetime.strptime(date_str, "%d.%m.%Y").date()
        except Exception as e:
            print(f"Error: {e}")

        UserProdLst = UserProdServo.GetUserProdByDate(user.id, date_str)

        print("User Product List:\n--------------------------")
        for user_prod in UserProdLst:
            print((f"Name: {user_prod.name}\n"
                f"Calories: {user_prod.cal}\n"
                f"Protein: {user_prod.protein}\n"
                f"Carbs: {user_prod.carbs}\n"
                f"Fats: {user_prod.fats}\n"
                f"Date: {user_prod.date}\n"
                f"Weight: {user_prod.weight}"))
            print("-------------------------")

        print("User Activities:\n--------------------------")
        UserActList = UserActServo.GetUserActByDate(user.id, date_str)
        for user_act in UserActList:
            print((f"Activity name: {user_act.name}\n"
                f"Activity date: {user_act.date}\n"
                f"Activity calories: {user_act.cal}\n"
                f"Activity time in min: {user_act.number_min}"))

def case_5():
    global user
    user=UserRepo.GetUserById(user.id)
    print(f"""PROFILE
    - Your weight: {user.weight}
    - Your weight goal: {user.weight_goal}
    - Your calories goal: {user.cal_goal}
    - Your water goal: {user.water_goal}
    """)


    print("What do you want to change?\n\
          1) Your weight\n\
          2) Your weight goal\n\
          3) Your calories goal\n\
          4) Your water goal\n")
    
    ans = int(input("Write your answer: "))

    if ans == 1:
        ans_ = float(input("Write your new weight: "))
        UserServo.change_user_data(user.id, "weight", ans_)
    elif ans == 2:
        ans_ = float(input("Write your new weight goal: "))
        UserServo.change_user_data(user.id, "weight_goal", ans_)
    elif ans == 3:
        ans_ = int(input("Write your new calories goal: "))
        UserServo.change_user_data(user.id, "cal_goal", ans_)
    elif ans == 4:
        ans_ = int(input("Write your new water goal: "))
        UserServo.change_user_data(user.id, "water_goal", ans_)

def case_6():
    choice = input ("What do you want to change?\n\
          1) Add reminder\n\
          2) Delete reminder\n")
    if choice == "1":
        name=input("Enter name of your reminder: ")
        try:
            on_off=int(input("Enter 1 if reminder is ON and 0 if is OFF: "))
        except Exception as e:
            print(f"Error: {e}")
        
        time=input("Enter time of your reminder: ")
        remind=Reminder()
        remind.user_id=user.id
        remind.name=name
        remind.on_off=on_off
        remind.time=time
        RemindersServo.addReminders(remind)

        reminders = RemindersServo.GetRemindsByUserId(user.id)

        if len(reminders) > 0:
            print("Список ваших напоминаний:")
            print("-------------------------")
            for reminder in reminders:
                print("Название: ", reminder.name)
                print("Статус: ", "Включено" if reminder.on_off == 1 else "Выключено")
                print("Время: ", reminder.time)
                print("-------------------------")
        else:
            print("У вас нет сохраненных напоминаний.")
    elif choice =="2":
        reminders = RemindersServo.GetRemindsByUserId(user.id)

        if len(reminders) > 0:
            print("Список ваших напоминаний:")
            print("-------------------------")
            for reminder in reminders:
                print("Название: ", reminder.name)
                print("Статус: ", "Включено" if reminder.on_off == 1 else "Выключено")
                print("Время: ", reminder.time)
                print("-------------------------")

        reminder_for_deleting=None
        name_for_delete= input("Write name of Reminder for deleting: ")
        for reminder in reminders:
            if reminder.name == name_for_delete:
                reminder_for_deleting = reminder
                break
        if reminder_for_deleting==None:
            print("There is no such reminder")
            return
        RemindersServo.deleteReminders(reminder_for_deleting.id)
    else:
        print("Incorrect Input!")
        

def case_7():
    user=None
    ans=input("Do you wont to exit?Y/N :")
    if ans=="Y":
        exit()
    elif ans=="N":
        initialize()
    else:
        print("Invalid choice")
        return

def WritingUserProd():  

    for prod in ProdServo.GetAllProducts():
        prod_info = vars(prod)
        for attr, value in prod_info.items():
            print(attr + ":", value)
        print("------------------")    

    NameOfProduct=input("Write name of Product: ")
    product = Product()  
    for prod in ProdServo.GetAllProducts():    
      if NameOfProduct == prod.name:
          product=prod
          break
      
   
    try:
        weight = int(input("Write weight of product in grams: "))
    except Exception as e:
            print(f"Произошла ошибка: {e}")  
            return 

    UserProdo=UserProd()
    UserProdo.weight=weight
    UserProdo.user_id=user.id

    date_str = input("Enter the date when the product was eaten (DD.MM.YYYY): ")
    date = datetime.datetime.strptime(date_str, "%d.%m.%Y").date()
    UserProdo.date = date

    UserProdServo.addUserProd(UserProdo,product)
    



def AddWaterForUser():
            
            try:
                MlOfWater = int(input("Enter the amount of water: "))
            except Exception as e:
                print(f"Произошла ошибка: {e}")  

            #Добавить дату
            Watero=Water()
            Watero.user_id = user.id
            Watero.ml=MlOfWater

            date_str = input("Write date when water was drunk (DD.MM.YYYY): ")
            date = datetime.datetime.strptime(date_str, "%d.%m.%Y").date()
            Watero.date = date

            WaterServo.addWater(Watero)

def initialize():
    global user
    print("\n\n\nHELLO!\n"
          "ITS FOOD DIARY!\n"
          "If you have an account, please write: YES\n"
          "Otherwise, write: NO")
    
    answer = input("Your answer: ")
    while answer != "NO" and answer != "YES":
        print("Incorrect input")
        answer = input("Your answer: ")
        

    if answer == "NO":
        user = UserServo.SignUp()
        if user == None:
            return
        else:
            UserServo.add_user(user)

    else:
        user = UserServo.logIn()
        if user is None:
            answer = input("Sign up? (YES/NO): ")
            if answer == "YES":
                user = UserServo.SignUp()
                UserServo.add_user(user)
            else:
                exit()    
    
    return user

################################################# PROGRAMM

user=initialize()
if user==None:
    user=initialize()

while True:

    print("MENU:\n \
            1)Add Product\Water\Activity\Reminders\n\
            2)Delete Product in List by date\n\
            3)Check statistics\n\
            4)View ProductList\Activities by date\n\
            5)Profile\n\
            6)Add\Delete Reminders\n\
            7)Log out\n")
        
    ans = int(input("Your answer: "))

    switch = {
        1: case_1,
        2: case_2,
        4: case_4,
        3: case_3,
        5: case_5,
        6: case_6,
        7: case_7
    }
 
    switch.get(ans, lambda: print("Invalid choice."))()