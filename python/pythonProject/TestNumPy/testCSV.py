import numpy as np


def write_to_csv(name, data):
    np.savetxt(name, data, fmt=['%6s', '%20s'], delimiter=',')  # datatype must be same


def read_from_csv(name):
    return np.genfromtxt(name, delimiter=',')


#data = np.array([['a', 1], ['b', 2], ['c', 3]])
#write_to_csv('test.csv', data)
print(read_from_csv('test.csv'))


