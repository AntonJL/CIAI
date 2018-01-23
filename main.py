import numpy as np
import sinegenerator as sg

TIME_HORIZON = 300



if __name__ == "__main__":
    random_sine = sg.sin_rand(TIME_HORIZON)
    print(random_sine)