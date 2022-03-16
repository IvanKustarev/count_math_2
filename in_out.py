from data_classes import Response, Single_request, Sys_request
from data_functions import functions, systems
from methods import iterations_method_system, half_division_method, iterations_method


def read():
    if int(input("Введите 1 для ввода с консоли или 2 для ввода из файла:")) == 1:
        if int(input("Введите 1 для решения уравнения или 2 для решения системы уравнений:")) == 1:
            print("Доступные уравнения:")
            for key, value in functions.items():
                print("№" + str(key) + ":\n" + value.present)
            fun = functions[int(input("Введите номер уравнения:"))]
            term_left = float(input("Введите левый край отрезка для рассмотрения:"))
            term_right = float(input("Введите правый край отрезка для рассмотрения:"))
            fun.approx_left = float(input("Введите левый край приближения:"))
            fun.approx_right = float(input("Введите правый край приближения:"))
            accuracy = float(input("Введите точность:"))
            if int(input("Выберите метод: 1 - половинного деления, 2 - простой итерации")) == 1:
                method = half_division_method
            else:
                method = iterations_method
            return Single_request(fun, method, term_left, term_right, accuracy)
        else:
            print("Доступные системы:")
            for key, value in systems.items():
                print("№" + str(key) + ":\n" + value["first"].present + "\n" + value["second"].present)
            system = systems[int(input("Введите номер системы:"))]
            # term_left = float(input("Введите левый край отрезка для рассмотрения:"))
            # term_right = float(input("Введите правый край отрезка для рассмотрения:"))
            system["first"].approx_left = float(input("Введите левый край приближения x:"))
            system["first"].approx_right = float(input("Введите правый край приближения x:"))
            system["second"].approx_left = float(input("Введите левый край приближения y:"))
            system["second"].approx_right = float(input("Введите правый край приближения y:"))
            accuracy = float(input("Введите точность:"))
            return Sys_request(system, iterations_method_system, 0, 0, accuracy)
    else:
        print("Не реализованно")


def write(response: Response):
    print("root = " + str(response.root))
    print("function in root = " + str(response.fun_in_root))
    print("iteration count  = " + str(response.i_count))


def write_sys(response: Response):
    print("root = " + str(response.root))
    print("iteration count  = " + str(response.i_count))
    print("Вектор погрешностей:")
    for key, value in response.error_vector.items():
        print(str(key) + ": " + str(value))


def write_err(response: Response):
    print("ERROR!: " + response.message)
