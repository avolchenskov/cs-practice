import numpy as np

def make_hours():
    return np.arange(0, 22, 3).tolist()


def vector_report(values):
    vector = np.asarray(values, dtype = float)
    d = dict()
    d['third'] = vector[2].item()
    d['last'] = vector[-1].item()
    d['middle'] = vector[2:6].tolist()
    d['every_second'] = vector[::2].tolist()
    d['reversed'] = vector[::-1].tolist()

    return d


def change_vector(values):
    vector = np.asarray(values.copy())
    vector[2:5] = 99
    vector[::2] = -1

    return vector.tolist()


def cap_above(values, limit):
    vector = np.asarray(values.copy())
    vector[vector>limit] = limit
    return vector.tolist()


def celsius_to_fahrenheit(c):
    return ((np.asarray(c.copy()) * (9 / 5)) + 32).tolist()
