#!/usr/bin/python3

import csv
import stats
from math import log
from random import uniform

def laplace(mu, b):
    u = uniform(-1, 1)
    return mu - (1 if u > 0 else -1) * log(abs(u))

def try_num(value):
    try:
        return float(value)
    except:
        return value

enable_dp = bool(input("use dp? "))

def dp_value(x):
    global enable_dp
    if enable_dp:
        return x + laplace(0, 1)
    else:
        return x

with open(input("database csv: "), newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     data = [{ key.strip(): try_num(value) for key, value in row.items()} for row in reader]
     print(data)

while True:
    print("=================")
    field = input("summarize field: ")
    summary = getattr(stats, input("summary function: "))
    where = eval("lambda row:" + input("where row: "))
    print(summary([dp_value(row[field]) for row in data if where(row)]))
