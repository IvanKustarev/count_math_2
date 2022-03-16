from data_classes import Function

functions = {
    1: Function(
        lambda x: x ** 3 + 2.84 * x ** 2 - 5.606 * x - 14.766,
        "y = x^2"
    )
}

systems = {
    1: {
        "first": Function(
            lambda x, y: x + 0.1 * x ** 2 + 0.2 * y ** 2 - 0.3,
            "1"
        ),
        "second": Function(
            lambda x, y: y + 0.2 * x ** 2 - 0.1 * x - 0.7,
            "2"
        )
    }
}
