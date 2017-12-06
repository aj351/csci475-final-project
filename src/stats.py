from math import sqrt

def mean(data):
    total = sum(data)
    count = len(data)
    mean = total / count
    if count > 1:
        delta = abs(mean - (total - max(data, key=lambda x: abs(x - mean))) / (count - 1))
    else:
        delta = total
    return (mean, delta)

def variance(data):
    m = mean(data)[0]
    return (sum((v - m) ** 2 for v in data) / len(data), None)

def sd(data):
    return (sqrt(variance(data)[0]), None)

def _sum(data):
    return (sum(data), max(data))

def _max(data):
    data = sorted(data)
    if len(data) > 1:
        return (data[-1], data[-1] - data[-2])
    else:
        return (data[0], data[0])

def _min(data):
    data = sorted(data)
    if len(data) > 1:
        return (data[0], data[1] - data[0])
    else:
        return (data[0], data[0])

def _len(data):
    return (len(data), 1)

OPS = {
    'sum': _sum,
    'max': _max,
    'min': _min,
    'count': _len,
    'mean': mean,
    'variance': variance,
    'sd': sd
}
