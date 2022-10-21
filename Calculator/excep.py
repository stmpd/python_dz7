def check_type(val):
    if not val.isnumeric():
        print('Wrong value. Try again:')
        return False

    val_int = int(val)

    if val_int != 0 and val_int != 1 and val_int != 2:
        print('Wrong value. Try again:')
        return False

    return True


def check_operation(val):
    if not val.isnumeric():
        print('Wrong value. Try again:')
        return False

    val_int = int(val)

    if not (val_int in range(0, 7)):
        print('Wrong value. Try again:')
        return False

    return True


def check_div(val):
    if not val.isnumeric():
        print('Wrong value. Try again:')
        return False

    val_int = int(val)

    if not (val_int in range(0, 4)):
        print('Wrong value. Try again:')
        return False

    return True


def check_number(val, zero_check=False):
    try:
        float(val)
    except ValueError:
        print('Wrong value. Try again:')
        return False

    val_float = float(val)

    if val_float == float(0) and zero_check:
        print('Wrong value. Try again:')
        return False

    return True