#GENERATE 300 UNITS
#EVERY UNIT CONTAINS THREE PROPERTIES AND ORDER HISTORY

import numpy as np


class Unit:
    def __init__(self, a_a, a_h, a_h_i, o_h, shape=(5, 1)):
        self.a_a = a_a
        self.a_h = a_h
        self.a_h_i = a_h_i
        self.o_h = o_h
        self.average = np.mean(o_h)
        self.shape = shape



def normal(val):
    return np.random.normal(val, 0.03)

def generateUnits(ARR_LENGTH):
    u_c = []
    age_mu = 75
    height_mu = 170
    hi_mu = 8.3

    for i in range(0,ARR_LENGTH):
        nu = Unit(normal(75), normal(170), normal(8.3), np.random.normal(15, 0.05, (208, )))
        u_c.append(nu)
        print(nu.average)

    return u_c
