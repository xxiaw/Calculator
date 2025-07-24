while True:
    num1 = int(input("Первое число: "))
    num2 = int(input("Второе число: "))

    message = '''
    Выберите операцию:

    + : сложение
    - : вычетание
    * : умножение
    / : деление

    '''

    operation = input(message)

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Идиот, иди учись")
        else:
            result = num1 / num2
    else:
        print("Try again")

    print(f"Результат: {result} \n(Ctrl + C чтобы выйти)")
    