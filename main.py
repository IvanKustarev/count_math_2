import matplotlib.pyplot as plt
import numpy as np

from data_classes import Request, Data
from in_out import read, write


def paint(source: Data):
    x = np.arange(source.term_left, source.term_right, 0.01)
    plt.plot(x, source.function.run(x))
    plt.show()


request: Request = read()
# paint(request.data)
response = request.method(request.data)
write(response)
