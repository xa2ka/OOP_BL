import datetime

from User.User import User
from User.UserServ import UserServ
from Product.ProdRep import ProdRep
from Product.ProdServ import ProdServ
from UserProd.UserProdServ import UserProdServ
from Water.WaterServ import WaterServ
from Activity.ActivityServ import ActivityServ
from UserAct.UserActServ import UserActServ
from UserProd.UserProd import UserProd
from Water.Water import Water
from Reminders.Reminders import Reminder
from Reminders.RemindersServ import RemindersServ



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
        activity = ActivityServo.GetActByName(name_act)
        time_min = int(input("Enter time of your activity: "))
        UserActServo.addUserAct(activity, user.id, time_min)

        for item in UserActServo.user_activity_repo.UserActList:
            print("Name:", item.name)
            print("User ID:", item.user_id)
            print("Calories:", item.cal)
            print("Number of Minutes:", item.number_min)
            print("Date:", item.date)
            print()  # Пустая строка для разделения вывода каждого элемента
    else:
        print("Invalid choice")
        return
    
def case_2():
        try:
            date_str = input("Enter date for checking Product List(DD.MM.YYYY): ")
            Date = datetime.datetime.strptime(date_str, "%d.%m.%Y").date()
        except Exception as e:
            print(f"Invalid input: {e}")

        # Date = int(input("Enter date for checking Product List: "))
        UserProdLst = UserProdServo.GetUserProdByDate(user.id, Date)

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
    date_str = input("Enter date for statistics (DD.MM.YYYY): ")
    Date = datetime.datetime.strptime(date_str, "%d.%m.%Y").date()

    print("----------------STATISTICS--------------\n\n\n")
    print("----------------WATER----------------\n")
    try: 
        WatLst = WaterServo.GetwaterByDate(user.id, Date)
        WaterSum = 0
        for wat in WatLst:
            WaterSum += wat.ml
        print(f"The amount of water: {WaterSum}")    
    except Exception as e:
        print(f"Error: {e}") 
    print("The goal of water per day: ",user.water_goal)
    print("Remaining water(ml) per day",user.water_goal-WaterSum)

    print("----------------PRODUCTS----------------\n")
  
    try:
        UserProdLst = UserProdServo.GetUserProdByDate(user.id, Date)
        ProtSum = 0
        FatSum = 0
        CarbsSum = 0
        CalSum = 0

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
        print(f"Error: {e}") 

    print("the goal of calories per day: ",user.cal_goal)
    print("Remaining calories per day",user.cal_goal-CalSum)


    print("----------------ACTIVITIES----------------\n")
  
    try:
        UserActList = UserActServo.GetUserActByDate(user.id, Date)
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
            date = datetime.datetime.strptime(date_str, "%d.%m.%Y").date()
        except Exception as e:
            print(f"Error: {e}")

        UserProdLst = UserProdServo.GetUserProdByDate(user.id, date)

        print("User Product List:\n--------------------------")
        for user_prod in UserProdLst:
            print("Name:", user_prod.name)
            print("Calories:", user_prod.cal)
            print("Protein:", user_prod.protein)
            print("Carbs:", user_prod.carbs)
            print("Fats:", user_prod.fats)
            print("Date:", user_prod.date)
            print("Weight:", user_prod.weight)
            print("-------------------------")  

        print("User Activities:\n--------------------------")
        UserActList = UserActServo.GetUserActByDate(user.id, date)
        for user_act in UserActList:
            print("Activity name: ",user_act.name)
            print("Activity date: ",user_act.date)
            print("Activity calories: ",user_act.cal)
            print("Activity time in min: ",user_act.number_min)


def case_5():
    print(UserServo.logIn()) 


def case_6():
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

    for prod in ProdRep.ProdList:
        prod_info = vars(prod)
        for attr, value in prod_info.items():
            print(attr + ":", value)
        print("------------------")    

    NameOfProduct=input("Write name of Product: ")
            
    for prod in ProdRep.ProdList:
        if NameOfProduct == prod.name:
            product = ProdServo.GetProdForCalculating(NameOfProduct)
        
    try:
        weight = int(input("Write weight of product in grams: "))
    except Exception as e:
            print(f"Произошла ошибка: {e}")  
            return 

    UserProdo=UserProd()
    UserProdo.weight=weight
    UserProdo.date=0
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
    print("HELLO!\n"
          "ITS FOOD DIARY!\n"
          "If you have an account, please write: YES\n"
          "Otherwise, write: NO")

    answer = input("Your answer: ")

    if answer == "NO":
        user = UserServo.SignUp()
        UserServo.add_user(user)

    else:
        user = UserServo.logIn()
        if user is None:
            answer = input("Sign up? (YES/NO)")
            if answer == "YES":
                user = UserServo.SignUp()
                UserServo.add_user(user)
    
    return user

################################################# PROGRAMM

user=initialize()

while True:

    print("MENU:\n \
            1)Add Product\Water\Activity\Reminders\n\
            2)Delete Product in List by date\n\
            3)Check statistics\n\
            4)View ProductList\Activities by date\n\
            5)Check user in db\n\
            6)Add Reminders\n\
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