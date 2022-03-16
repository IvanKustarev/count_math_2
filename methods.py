from data_classes import Response, Request, Sys_request


def same_sign(first, second):
    return True if (first < 0 and second < 0) or (first > 0 and second > 0) or (first == second == 0) else False


def finding_der(param, fun):
    return (fun(param + 0.00000001) - fun(param)) / 0.00000001


def half_division_method(request: Request):
    response = Response

    if same_sign(request.function.exe(request.function.approx_left),
                 request.function.exe(request.function.approx_right)):
        response.message = "No one root"
        response.code = 1
        return response

    last_x = request.function.approx_left
    while True:
        response.i_count += 1
        x = (request.function.approx_left + request.function.approx_right) / 2
        if same_sign(request.function.exe(x), request.function.exe(request.function.approx_left)):
            request.function.approx_left = x
        else:
            request.function.approx_right = x
        if abs(x - last_x) < request.accuracy:
            response.root = x
            response.fun_in_root = request.function.exe(x)
            break
        last_x = x
    return response


def iterations_method(request: Request):
    response = Response
    a_dev = finding_der(request.function.approx_left, request.function.exe)
    b_dev = finding_der(request.function.approx_right, request.function.exe)

    lyam = -1 / max(a_dev, b_dev)
    fi = lambda param: param + lyam * request.function.exe(param)
    fi_der = lambda param: finding_der(param, fi)

    # Проверка достаточного условия сходимости
    if abs(fi_der(request.function.approx_left)) > 1 or abs(fi_der(request.function.approx_right)) > 1:
        response.message = "Достаточное условие сходимости не выполнено"
        response.code = 1
        return response

    last_x = request.function.approx_left
    while True:
        response.i_count += 1
        x = fi(last_x)
        if abs(x - last_x) < request.accuracy:
            response.root = x
            response.fun_in_root = request.function.exe(x)
            break
        last_x = x
    return response


# Частная производная по х
def calc_dx(function, x, y, h=0.00000001):
    return (function(x + h, y) - function(x - h, y)) / (2 * h)


# Частная производная по у
def calc_dy(function, x, y, h=0.00000001):
    return (function(x, y + h) - function(x, y - h)) / (2 * h)


def iterations_method_system(sys_request: Sys_request):
    response = Response
    fi_1 = lambda x, y: (sys_request.functions["first"].exe(x, y) - x) * -1
    fi_2 = lambda x, y: (sys_request.functions["second"].exe(x, y) - y) * -1

    f1_approx = sys_request.functions["first"].approx_right
    f2_approx = sys_request.functions["second"].approx_right

    if max(abs(calc_dx(fi_1, f1_approx, f2_approx)) + abs(calc_dy(fi_2, f1_approx, f2_approx)),
           abs(calc_dx(fi_2, f1_approx, f2_approx)) + abs(calc_dy(fi_1, f1_approx, f2_approx))) >= 1:
        response.message = "Достаточное условие сходимости не выполнено"
        response.code = 1
        return response
    last_x = sys_request.functions["first"].approx_right
    last_y = sys_request.functions["second"].approx_right
    while True:
        response.i_count += 1
        x = fi_1(last_x, last_y)
        y = fi_2(last_y, last_y)
        response.error_vector[response.i_count] = {"x": abs(x - last_x), "y": abs(y - last_y)}
        if max(abs(x - last_x), abs(y - last_y)) < sys_request.accuracy:
            response.root = {x, y}
            response.fun_in_root = {sys_request.functions["first"].exe(x, y), sys_request.functions["second"].exe(x, y)}
            break
        last_x = x
        last_y = y
    return response
