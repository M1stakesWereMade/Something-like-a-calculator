print('Добро пожаловать в типо калькулятор!')


def calc():
    while True:
        try:
            a = int(input('Введите первое число: '))
            b = int(input('Введите второе число: '))          
            break
        except ValueError:
            print('Что тебе не понятно в слове "ЧИСЛО"!')

    while True:
        try:       
            c = str(input('Введите знак: '))
            if c not in ['+', '-', '/', '*', '%', '//']:
                raise ValueError("Введен неверный знак!")               
            break
        except ValueError:
                print('Что тебе не понятно в слове "Знак"!')

    try:
        if c == '+':
            print(f'Полученное результат: {a + b}')
        elif c == '-':
            print(f'Полученное результат: {a - b}')
        elif c == '/':
            print(f'Полученное результат: {a / b:.2}')
        elif c == '*':
            print(f'Полученное результат: {a * b}')
        elif c == '//':
            print(f'Полученное результат: {a // b}')
        elif c == '%':
            print(f'Полученное результат: {a % b}')

    except ZeroDivisionError:
        print("Много на себя берешь, на ноль делить не принято!")
calc()

