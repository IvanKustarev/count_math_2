class Function:
    run = ""
    function_print = ""

    def __init__(self, run, function_print):
        self.run = run
        self.function_print = function_print


class Data:
    term_left = ""
    term_right = ""
    approx_left = ""
    approx_right = ""
    function = ""
    accuracy = ""

    def __init__(self, term_border_left, term_border_right, approximation_border_left, approximation_border_right,
                 fun: Function, accuracy):
        self.term_left = term_border_left
        self.term_right = term_border_right
        self.approx_left = approximation_border_left
        self.approx_right = approximation_border_right
        self.function = fun
        self.accuracy = accuracy


class Response:
    root = 0
    fun_in_root = 0
    i_count = 0
    message = ""
    code = 0

    def __init__(self, root, fun_in_root, i_count, message, code):
        self.root = root
        self.fun_in_root = fun_in_root
        self.i_count = i_count
        self.message = message
        self.code = code


class Request:
    data: Data = 0
    method = 0

    def __init__(self, data, method):
        self.data = data
        self.method = method
