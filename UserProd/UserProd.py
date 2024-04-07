import datetime

class UserProd:
    def __init__(self, user_id=0, name="", cal=0,
                 protein=0, carbs=0, fats=0, date=None, weight=0):
        if date is None:
            date = datetime.date.today()
        self.user_id = user_id
        self.name = name
        self.cal = cal
        self.protein = protein
        self.carbs = carbs
        self.fats = fats
        self.date = date
        self.weight = weight