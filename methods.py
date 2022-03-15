import numpy as np

from data_classes import Response, Data


def sim_sign(first, second):
    return True if (first < 0 and second < 0) or (first > 0 and second > 0) or (first == second == 0) else False


def half_division_method(data: Data):
    response = Response

    if sim_sign(data.function.run(data.approx_left), data.function.run(data.approx_right)):
        response.message = "No one root"
        response.code = 1
        return response

    last_x = data.approx_left
    while True:
        response.i_count += 1
        x = (data.approx_left + data.approx_right) / 2
        if sim_sign(data.function.run(x), data.function.run(data.approx_left)):
            data.approx_left = x
        else:
            data.approx_right = x
        if abs(x - last_x) < data.accuracy:
            response.root = x
            response.fun_in_root = data.function.run(x)
            break
        last_x = x
    return response


def iterations_method(data: Data):
    dev_finding = lambda x, fun: (fun(x + 0.00000001) - fun(x)) / 0.00000001

    a_dev = dev_finding(data.approx_left, data.function.run)
    b_dev = dev_finding(data.approx_right, data.function.run)

    lam = -1 / max(a_dev, b_dev)
    response = Response
    # андерстенднуть
    if abs(lam) >= 1:
        response.code = 1
        response.message = "No approximate"
        return response

    last_x = data.approx_left
    while True:
        response.i_count += 1
        x = last_x + lam * data.function.run(last_x)
        if abs(x - last_x) < data.accuracy:
            response.root = x
            response.fun_in_root = data.function.run(x)
            break
        last_x = x
    return response
