x = 0
y = 0
op = 0


def init(a, b, c):
    global x
    global y
    global op

    x = a
    y = b
    op = c


def div():
    if op == 1:
        return x / y
    elif op == 2:
        return x // y
    elif op == 3:
        return x % y