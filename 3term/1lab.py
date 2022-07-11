def main():
    # Функция main позволяет ввести значения с клавиатуры
    # и запустить вычисление действия калькулятора
    operand1 = float(input("Введите 1 число:"))
    operand2 = float(input("Введите 2 число:"))
    action = input("Введите действие: ")
    print(type(operand1), type(operand2))
    result = calculate(operand1, operand2, action)
    print("Результат вычисления:", result)


def calculate(op1, op2, act):
    # 2-3 дополнительных действия с двумя операндами
    op1 = float(op1)
    op2 = float(op2)
    if act == "+":
        res = op1 + op2
    elif act == "-":
        res = op1 - op2
    elif act == "*":
        res = op1 * op2
    elif act == "/":
        if op2 != 0:
            res = op1 / op2
        else:
            res = "Деление на ноль невозможно"
    elif act == "^":
        if op2 % 1 == 0:
            res = op1**op2
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
            res = op1 % op2
        else:
            res = "Деление на ноль невозможно"
    else:
        res = "Операция не распознана"

    if not isinstance(res, str) and res.is_integer():
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


main()
test_sum()
test_type_of_result_sum()
test_divide()
test_mod()
