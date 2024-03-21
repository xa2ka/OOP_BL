import sys
sys.path.append('D:\\OOP\\Water')
from Water import Water
sys.path.append('D:\\OOP\\User')
from User import User 


user = User(id=1, name='John', surname='Doe', email='johndoe@example.com',
            password='mypassword', old_year=30, weight=70, weight_goal=65,
            cal_goal=2000, gender='male', water_goal=2000)


water=Water()
water.id=13


print(water.id, user.id)