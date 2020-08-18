'''def print_msg(msg):
    def printer(x):
        print(msg + " " + x)
    return printer


q = print_msg("hello")
q("mehdi")'''


def smart_divide(f):
    def inner(a, b):
        print("iam going to divide", a, "over", b)
        if b == 0:
            print(" b is not allowed to be assigned zero")
            return
        print(f(a, b))
    return inner


@smart_divide
def divide(x, y):
    return x/y


divide(2, 4)
q = smart_divide(divide)
q(2, 4)
