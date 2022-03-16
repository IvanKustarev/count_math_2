import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

from data_classes import Request
from in_out import read, write, write_sys, write_err


def paint(source):
    if type(source) == Request:
        x = np.arange(source.term_left, source.term_right, 0.01)
        plt.plot(x, source.function.exe(x))
        plt.show()
    else:
        x, y = sp.symbols("x y")
        sp.plot_implicit(sp.Or(sp.Eq(source.functions["first"].exe(x, y), 0), sp.Eq(source.functions["second"].exe(x, y), 0)))


request: Request = read()
paint(request)
response = request.method(request)
if response.code == 1:
    write_err(response)
elif type(request) == Request:
    write(response)
else:
    write_sys(response)
