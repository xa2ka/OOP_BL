# import datetime


# class UserProd:
#     def __init__(self, user_id=0, name="", cal=0, protein=0, carbs=0, fats=0, date=None, weight=0):
#         if date is None:
#             date = datetime.date.today()
#         self.user_id = user_id
#         self.name = name
#         self.cal = cal
#         self.protein = protein
#         self.carbs = carbs
#         self.fats = fats
#         self.date = date
#         self.weight = weight

#     def to_dict(self):
#         return {
#             "user_id": self.user_id,
#             "name": self.name,
#             "cal": self.cal,
#             "protein": self.protein,
#             "carbs": self.carbs,
#             "fats": self.fats,
#             "date": self.date.strftime("%Y-%m-%d"),
#             "weight": self.weight
#         }

#     @classmethod
#     def from_dict(cls, data_dict):
#         date_str = data_dict.get("date")
#         date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else None

#         return cls(
#             user_id=data_dict.get("user_id"),
#             name=data_dict.get("name"),
#             cal=data_dict.get("cal"),
#             protein=data_dict.get("protein"),
#             carbs=data_dict.get("carbs"),
#             fats=data_dict.get("fats"),
#             date=date,
#             weight=data_dict.get("weight")
#         )
