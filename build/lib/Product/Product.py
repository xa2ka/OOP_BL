# class Product:
#     def __init__(self, id=None, name="", cal=0, fats=0, carbs=0, protein=0):
#         self.id = id
#         self.name = name
#         self.cal = cal
#         self.fats = fats
#         self.carbs = carbs
#         self.protein = protein

#     def to_dict(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "cal": self.cal,
#             "fats": self.fats,
#             "carbs": self.carbs,
#             "protein": self.protein
#         }

#     @classmethod
#     def from_dict(cls, data_dict):
#         return cls(
#             id=data_dict.get("id"),
#             name=data_dict.get("name"),
#             cal=data_dict.get("cal"),
#             fats=data_dict.get("fats"),
#             carbs=data_dict.get("carbs"),
#             protein=data_dict.get("protein")
#         )