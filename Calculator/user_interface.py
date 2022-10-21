import excep
import model_sum
import model_sub
import model_mult
import model_div
import model_pow
import model_sqrt
import logg



def view_welcome():
    print('Calculator welcomes you!')
    print('\n'*1)


def input_type():
    print('Working with:')
    print('1 - rational')
    print('2 - complex')
    print('0 - exit')
    while True:
        val = input()
        if excep.check_type(val):
            return int(val)


def input_operation():
    print('Working with:')
    print('1 - sum')
    print('2 - sub')
    print('3 - mul')
    print('4 - div')
    print('5 - pow')
    print('6 - sqrt')
    print('0 - previous menu')
    while True:
        val = input()
        if excep.check_operation(val):
            return int(val)


def input_div():
    print('Operations:')
    print('1 - /')
    print('2 - //')
    print('3 - %')
    print('0 - previous menu')
    while True:
        val = input()
        if excep.check_div(val):
            return int(val)


def input_numbers(operation, is_compl):
    if operation == 6:
        return [enter_number("", is_compl), 0]

    else:
        res_ls = []
        res_ls.append(enter_number("1 ", is_compl))
        res_ls.append(enter_number("2 ", is_compl, operation == 4))
        return res_ls


def enter_number(count_str, is_compl=False, zero_check=False):

    if not is_compl:
        while True:
            val = input('Enter %1 number: '.replace('%1 ', count_str))
            if excep.check_number(val, zero_check):
                return float(val)
    else:
        while True:
            val = input('Enter %1 real part: '.replace('%1 ', count_str))
            if not excep.check_number(val, zero_check):
                continue
            else:
                break
        val1 = float(val)

        while True:
            val = input('Enter %1 imaginary number: '.replace('%1 ', count_str))
            if not excep.check_number(val, zero_check):
                continue
            else:
                break
        val2 = float(val)

        return complex(val1, val2)


def calculate(numbers, type_op, type_div):
    if type_op == 1:
        model_sum.init(numbers[0], numbers[1])
        res = model_sum.summ()
        print(res)
        logg.logger('+', numbers, res)
    elif type_op == 2:
        model_sub.init(numbers[0], numbers[1])
        res = model_sub.sub()
        print(res)
        logg.logger('-', numbers, res)
    elif type_op == 3:
        model_mult.init(numbers[0], numbers[1])
        res = model_mult.mult()
        print(res)
        logg.logger('*', numbers, res)
    elif type_op == 4:
        model_div.init(numbers[0], numbers[1], type_div)
        res = model_div.div()
        print(res)
        logg.logger('/', numbers, res)
    elif type_op == 5:
        model_pow.init(numbers[0], numbers[1])
        res = model_pow.powr()
        print(res)
        logg.logger('pow', numbers, res)
    elif type_op == 6:
        model_sqrt.init(numbers[0])
        res = model_sqrt.sqrt()
        print(res)
        logg.logger('sqrt', numbers, res)


def start():
    view_welcome()
    while True:
        type_num = input_type()
        is_complex = False
        if type_num == 0:
            break
        elif type_num == 2:
            is_complex = True

        while True:
            type_op = input_operation()
            if type_op == 0:
                break

            numbers = input_numbers(type_op, is_complex)

            type_div = 0

            if type_op == 4 and not is_complex:
                # while True:
                type_div = input_div()
                if type_div == 0:
                    continue

            calculate(numbers, type_op, type_div)
            break