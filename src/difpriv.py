#!/usr/bin/python3

import csv
import stats

def try_num(value):
    try:
        return float(value)
    except:
        return value

with open(input("database csv: "), newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     data = [{ key.strip(): try_num(value) for key, value in row.items()} for row in reader]
     print(data)

while True:
    print("=================")
    field = input("summarize field: ")
    summary = getattr(stats, input("summary function: "))
    where = eval("lambda row:" + input("where row: "))
    print(summary([row[field] for row in data if where(row)]))
