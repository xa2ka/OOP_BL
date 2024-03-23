from User.User import User
from User.UserServ import UserServ
from User.UserRep import UserRep


while True:
    print("HELLO!\nITS FOOD DIARY!\n If you have account please write: YES\nelse write: NOT")
    Answer=input("Your answer: ")
    if Answer == "NO":

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



    else:
        email = input("Введите адрес электронной почты пользователя: ")
        password = input("Введите пароль пользователя: ")
        
      