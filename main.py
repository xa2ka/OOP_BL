import sys
sys.path.append('D:\\OOP')

from Water.Water import Water
from User.User import User




user = User(id=1, name='John', surname='Doe', email='johndoe@example.com',
            password='mypassword', old_year=30, weight=70, weight_goal=65,
            cal_goal=2000, gender='male', water_goal=2000)


water=Water()
water.id=13


print(water.id, user.id)

while True:
    pass