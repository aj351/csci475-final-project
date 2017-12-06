#!/usr/bin/python3

from random import randint, uniform, choice, choices, lognormvariate
from math import log, floor
from names import get_full_name
import csv

count = int(input("row count: "))

def full_random_zip():
    nums = [str(i) for i in range(10)]
    return "".join([choice(nums[1:])] + choices(nums, k=4))

zip_set = [full_random_zip() for i in range(count // 250)]

def random_zip():
    return choice(zip_set)

def random_name():
    """
    letters = [chr(97 + i) for i in range(26)]
    first = "".join(choices(letters, k=randint(3, 7)))
    last = "".join(choices(letters, k=randint(5, 10)))
    return first + " " + last
    """
    return get_full_name()

income_mu = log(60000)
def random_income():
    global income_mu
    return floor(lognormvariate(income_mu, 0.5))

def random_age():
    return randint(18, 65)

net_worth_add_mu = log(1000)
def random_net_worth(income, age):
    global net_worth_add_mu
    return floor(income * age * uniform(0, 0.3) + lognormvariate(net_worth_add_mu, 2.0))

def random_person():
    age = random_age()
    income = random_income()
    net_worth = random_net_worth(income, age)
    return { 'name': random_name(), 'age': age, 'income': income, 'zip': random_zip(), 'net_worth': net_worth }

with open(input("filename: "), 'w') as csvfile:
    fieldnames = ['name', 'age', 'income', 'zip', 'net_worth']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(count):
        writer.writerow(random_person())
