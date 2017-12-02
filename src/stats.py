from math import sqrt

def mean(data):
    return sum(data) / len(data)

def variance(data):
    m = mean(data)
    return sum((v - m) ** 2 for v in data) / len(data)

def sd(data):
    return sqrt(variance(data))

def maximum(data):
    return max(data)

def minimum(data):
    return min(data)
