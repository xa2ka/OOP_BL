class User:
    def __init__(self, id=0, name="", surname="", email="", password=0, old_year=0,
                 weight=0, weight_goal=0, cal_goal=0, gender="", water_goal=0):
        self.id, self.name, self.surname, self.email, self.password, self.old_year, \
        self.weight, self.weight_goal, self.cal_goal, self.gender, self.water_goal = \
            id, name, surname, email, password, old_year, weight, weight_goal, cal_goal, gender, water_goal

    def __str__(self):
        return f"User ID: {self.id}\nName: {self.name}\nSurname: {self.surname}\nEmail: \
            {self.email}\nPassword: {self.password}\nOld Year: {self.old_year}\nWeight:\
            {self.weight}\nWeight Goal: {self.weight_goal}\nCalorie Goal:\
            {self.cal_goal}\nGender: {self.gender}\nWater Goal: {self.water_goal}"