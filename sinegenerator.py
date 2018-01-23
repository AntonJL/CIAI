import numpy as np

# SINUS WAVE WITH RANDOMNESS


def sin_rand(t_val):

    series = np.zeros((t_val, 1))

    for i in range(t_val):
        val_toadd = np.sin(i*np.random.rand())
        series[i] = val_toadd

    return series

