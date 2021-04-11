def fname(fcs, values):
    for f in fcs:
        if values[f.__name__] != "":
            return f(values[f.__name__])


def a(x):
    return x


def b(x):
    return x


def c(x):
    return x


if __name__ == "__main__":
    fcs = [a, b, c]
    values = {
        "a": "",
        "b": "ja",
        "c": "",
    }
    print(fname(fcs, values))
