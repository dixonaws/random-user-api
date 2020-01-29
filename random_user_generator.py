import boto3
from faker import Faker
import json
from random import randint
from random import choice
import random

fake = Faker()

def main():
    while (True):
        dict_user = generate_user()
        json_user = json.dumps(dict_user)
        print(json_user)

def generate_user():
    dict_user = {}

    str_name = fake.name()
    lst_name = str_name.split()

    dict_user["first_name"] = lst_name[0]
    dict_user["last_name"] = lst_name[1]
    dict_user["address"] = fake.address()

    lst_gender = ["m", "f"]
    dict_user["gender"] = choice(lst_gender)

    # Latitudes range from -90 to 90
    flt_latitude = random.uniform(-90.0000000000, 90.0000000000)

    # and longitudes range from -180 to 80. Uses the format "DDD MM SS + compass direction (N, S, E, or W)." Latitudes range from 0 to 90 and longitudes range from 0 to 180. The last degree, minute, or second or a latitude or longitude may contain a decimal portion
    flt_longitude = random.uniform(-180.0000000000, 80.0000000000)

    dict_user["latitude"] = flt_latitude
    dict_user["longitude"] = flt_longitude
    dict_user["age"] = randint(21, 100)

    return (dict_user)

main()
