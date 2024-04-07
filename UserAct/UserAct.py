import datetime


class UserAct:
    def __init__(self, name="", user_id=0, date=None, cal=0, number_min=0):
        self.name, self.user_id, self.cal, self.number_min, self.date = \
            name, user_id, cal, number_min, date
        if date is None:
            date = datetime.date.today()