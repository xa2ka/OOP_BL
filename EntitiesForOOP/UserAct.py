import datetime


class UserAct:
    def __init__(self, name="", user_id=0, date=None, cal=0, number_min=0):
        self.name = name
        self.user_id = user_id
        self.cal = cal
        self.number_min = number_min
        self.date = date if date is not None else datetime.date.today()
 
    def to_dict(self):
        return {
            "name": self.name,
            "user_id": self.user_id,
            "cal": self.cal,
            "number_min": self.number_min,
            "date": self.date.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name", ""),
            user_id=data.get("user_id", 0),
            cal=data.get("cal", 0),
            number_min=data.get("number_min", 0),
            date=datetime.datetime.fromisoformat(data.get("date"))
        )
    