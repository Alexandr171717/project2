sign = input('Знак операции: ')
a = int(input('Число 1: '))
b = int(input('Число 2: '))

match sign:
    case '+':
        print(a + b)
    case '-':
        print(a - b)
    case '/':
        if b != 0:
            print(round(a / b, 2))
    case '*':
        print(a * b)
    case _:
        print('Неверный знак операции')