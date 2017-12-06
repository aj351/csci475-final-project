#!/usr/bin/python3

import csv
import stats
import math
from math import log
from random import uniform

def forever():
    while True:
        yield

def laplace(mu, b):
    u = uniform(-1, 1)
    return mu - b * (1 if u > 0 else -1) * log(abs(u))

def try_num(value):
    try:
        return float(value)
    except:
        return value

def eval_where(row, clause):
    return eval(clause, {'math': math}, row)

enable_dp = input('use dp (y/n): ') == 'y'
if enable_dp:
    eps = float(input('epsilon: '))
    query_limit = int(input('query limit: '))

def apply_dp(rows, func):
    stat, delta = func(rows)
    if delta is None:
        if len(rows) > 1:
            delta = max(abs(func([x for j, x in enumerate(rows) if i != j]) - stat) for i in range(len(rows)))
        elif len(rows) == 1:
            delta = rows[0]
    global eps
    global query_limit
    b = query_limit * delta / eps
    print(f'# stat={stat:f} b={b:f}')
    return stat + laplace(0, b)

with open(input('database csv: '), newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     columns = reader.fieldnames
     data = [{ key.strip(): try_num(value) for key, value in row.items()} for row in reader]

print()
print("summary functions:", *stats.OPS.keys())
print("columns:", *columns)
print()

for query_index in range(query_limit) if enable_dp else forever():
    while True:
        print('=================')
        try:
            field = input('summarize field: ')
            summary = stats.OPS[input('summary function: ')]
            where = compile(input('where: '), '<where clause>', 'eval')
            rows = [row[field] for row in data if eval_where(row, where)]
            if len(rows) == 0:
                rows = [sum(row[field] for row in data) / len(data)]
            output = apply_dp(rows, summary) if enable_dp else summary(rows)[0]
            print(f'{output:f}')
        except Exception as e:
            print("Error!", e)
        else:
            break
