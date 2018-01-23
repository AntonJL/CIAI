#GENERATE 300 UNITS
#EVERY UNIT CONTAINS THREE PROPERTIES AND ORDER HISTORY
#THE AI TRAINS ON THE AVERAGE ORDER, SPLIT ACROSS ALL THE HISTORY
#THE AI IS SUPPLEMENTED WITH THE CONTEXT INJECTION, ALLOWING FOR INDIVIDUAL ORDERS TO BE RENDERED

import numpy as np


class Unit:
    def __init__(self, a_a, a_h, a_h_i, o_h):
        self.a_a = a_a
        self.a_h = a_h
        self.a_h_i = a_h_i
        self.o_h = o_h
        self.average = np.mean(o_h)



def normal(val):
    return np.random.normal(val, 0.01)


ARR_LENGTH = 30
u_c = []
age_mu = 75
height_mu = 170
hi_mu = 8.3

for i in range(0,ARR_LENGTH):
    nu = Unit(normal(75), normal(170), normal(8.3), np.random.normal(15, 0.05, (208, )))
    u_c.append(nu)
    print(nu.average)
    
