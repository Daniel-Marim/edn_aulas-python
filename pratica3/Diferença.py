while True:
    try:
        a = int(input('Digite um valor: '))
        b = int(input('Digite outro valor: '))

        if a > b:
            print(f'A diferença entre o valor {a} e o valor {b} é igual a: {a - b}')
            break
        elif a < b:
            print(f'A diferença entre o valor {b} e o valor {a} é igual a: {b - a}')
            break
        else:
            print('Os valores são iguais')
            break
    except ValueError:
        print("Entrada invalida!")