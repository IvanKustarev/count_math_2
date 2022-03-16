import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

from data_classes import Single_request
from in_out import read, write, write_sys, write_err


def paint(request):
    if type(request) == Single_request:
        x = np.arange(request.term_left, request.term_right, 0.01)
        plt.plot(x, request.function.exe(x))
        plt.show()
    else:
        x, y = sp.symbols("x y")
        sp.plot_implicit(
            sp.Or(sp.Eq(request.functions["first"].exe(x, y), 0), sp.Eq(request.functions["second"].exe(x, y), 0)))


if __name__ == '__main__':
    request = read()
    paint(request)
    response = request.method(request)
    if response.code == 1:
        write_err(response)
    elif type(request) == Single_request:
        write(response)
    else:
        write_sys(response)
