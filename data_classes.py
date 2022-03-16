class Function:
    exe = ""
    present = ""
    approx_left = ""
    approx_right = ""

    def __init__(self, exe, present):
        self.exe = exe
        self.present = present


class Response:
    root = 0
    fun_in_root = 0
    i_count = 0
    message = ""
    code = 0
    error_vector = {}

    def __init__(self, root, fun_in_root, i_count, message, code):
        self.root = root
        self.fun_in_root = fun_in_root
        self.i_count = i_count
        self.message = message
        self.code = code


class Request:
    function: Function = 0
    method = 0
    term_left = 0
    term_right = 0
    accuracy = 0

    def __init__(self, function, method, term_left, term_right, accuracy):
        self.function = function
        self.method = method
        self.term_left = term_left
        self.term_right = term_right
        self.accuracy = accuracy

class Sys_request:
    functions = {}
    method = 0
    term_left = 0
    term_right = 0
    accuracy = 0

    def __init__(self, functions, method, term_left, term_right, accuracy):
        self.functions = functions
        self.method = method
        self.term_left = term_left
        self.term_right = term_right
        self.accuracy = accuracy