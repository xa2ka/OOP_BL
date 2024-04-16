import datetime

class Water:
    def __init__(self, user_id=0, ml=0, date=None):
        self.user_id = user_id
        self.ml = ml
        self.date = date if date is not None else datetime.date.today()


    def to_dict(self):
        return {
            "user_id": self.user_id,
            "ml": self.ml,
            "date": self.date.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            user_id=data.get("user_id", 0),
            ml=data.get("ml", 0),
            date=datetime.datetime.fromisoformat(data.get("date"))
        )