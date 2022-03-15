from data_classes import Data, Response, Request
from data_functions import f1
from methods import iterations_method


def read():
    return Request(Data(-10, 10, 3, 4, f1, 0.01), iterations_method)


def write(response: Response):
    print("root = " + str(response.root))
    print("function in root = " + str(response.fun_in_root))
    print("iteration count  = " + str(response.i_count))
