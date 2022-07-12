import math


def main():
    """
     Функция main позволяет ввести значения с клавиатуры
     и запустить вычисление действия калькулятора
    """
    operand1 = float(input("Введите 1 число:"))
    operand2 = float(input("Введите 2 число:"))
    action = input("Введите действие: ")
    print(type(operand1), type(operand2))
    result = calculate(operand1, operand2, action, settings.get('precision'))
    print("Результат вычисления:", result)


settings = {'precision': '0.00001'}


def convert_precision(precision):
    """
    Конвертирует точность вида float(ex.:0.001)
    в целочисленный выд
    """
    if precision is None:
        precision = '0.001'
    if type(precision) is float:
        precision = str(f'{precision:f}')
    for i in range(len(str(precision))):
        if float(precision) * 10**i >= 1:
            return i


def convert_precision_alt(**kwargs):
    """
    Альтернативная функция конвертации точности,
    здесь аргумент берется из словаря с заданной точностью
    вместо обычного числа или строки
    """
    precision = kwargs.get('precision')
    if precision is None:
        precision = '0.001'
    if type(precision) is float:
        precision = str(precision)
    for i in range(len(precision)):
        if float(precision) * 10**i >= 1:
            return i


def standard_deviation(*args, precision=None):
    """
    Функция вычисляет среднеквадратическое отклонение из
    произвольного числа аргументов в виде кортежа
    """
    precision = convert_precision(precision)
    arith_mean = 0
    sum_squares = 0
    for arg in args:
        arith_mean += arg
    arith_mean /= len(args)
    for arg in args:
        sum_squares += (arg - arith_mean)**2
    deviation = math.sqrt(sum_squares / len(args))
    return round(deviation, precision)


def digits_round(result, precision):
    """
    Функция позволяет округлять вещественные числа 
    по точности precision
    """
    if type(result) == float and not result.is_integer():
        precision = convert_precision(precision)
        result = round(result, precision)
        return result
    else:
        return result


def calculate(op1, op2, act, precision=None):
    """
    Просто калькулятор)
    """
    if act == "+":
        res = op1 + op2
    elif act == "-":
        res = op1 - op2
    elif act == "*":
        res = op1 * op2
        if precision:
            res = digits_round(res, precision)
    elif act == "/":
        if op2 != 0:
            res = digits_round(op1 / op2, precision)
        else:
            res = "Деление на ноль невозможно"
    elif act == "^":
        if op2 % 1 == 0:
            res = digits_round(op1 ** op2, precision)
        else:
            res = "Возведение в вещественную степень невозможно"
    # Целочисленное деление
    elif act == "//":
        if op2 != 0:
            res = op1 // op2
        else:
            res = "Деление на ноль невозможно"
    # Остаток от деления
    elif act == "%":
        if op2 != 0:
            res = digits_round(op1 % op2, precision)
        else:
            res = "Деление на ноль невозможно"
    else:
        res = "Операция не распознана"

    if isinstance(res, float) and res.is_integer():
        res = int(res)

    return res


def test_sum():
    assert calculate(1, 2, "+") == 3


def test_divide():
    assert calculate(7, 3, "//") == 2


def test_mod():
    assert calculate(9, 2, "%") == 1


def test_type_of_result_sum():
    assert type(calculate(1, 2, "+")) is int


def test_standard_deviation():
    assert standard_deviation(45, 45, 32, 65, 999, precision=0.00001) == 381.04614


def test_cp_with_1():
    assert convert_precision('0.1') == 1, "Должна быть 1"


def test_cp_with_2():
    assert convert_precision('0.01') == 2, "Должно быть 2"


def test_cp_with_5():
    assert convert_precision('0.00001') == 5, "Должно быть 5"


def test_cp_with_5_as_float():
    assert convert_precision(0.00001) == 5, "Должно быть 5"


main()
test_standard_deviation()
test_sum()
test_type_of_result_sum()
test_cp_with_1()
test_cp_with_2()
test_cp_with_5()
test_cp_with_5_as_float()
test_divide()
test_mod()
