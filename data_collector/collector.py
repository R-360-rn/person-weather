from users.models import UserBase, Weather
import json
import requests

def insert_rand_user():
    userdata = requests.get('https://randomuser.me/api/').json()
    name = userdata['results'][0]['name']['first']
    surname = userdata['results'][0]['name']['last']
    age = userdata['results'][0]['dob']['age']
    obj = UserBase(name=name, surname=surname, age=age)
    obj.save()
    print(f'UserBase {obj.name} saved to db.')

def insert_weather():
    pass