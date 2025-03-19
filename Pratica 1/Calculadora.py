def soma(a, b):
    print(f"\nResultado: {a+b}")
def subtract(a, b):
    print(f"\nResultado: {a-b}")
def multiply(a, b):
    print(f"\nResultado: {a*b}")
def divide(a, b):
    print(f"\nResultado: {a/b:.2f}")

def calculadora():
    a = float(input("Digite o primeiro numero: "))
    b = float(input("Digite o segundo numero: "))
    while True:
        try:
            operador = int(input('''Escolha a operação:
             1 - Soma
             2 - Subtracao
             3 - Multiplicacao
             4 - Divisao
             5 - Sair
             - '''))
            if operador == 1:
                soma(a, b)
            elif operador == 2:
                subtract(a, b)
            elif operador == 3:
                multiply(a, b)
            elif operador == 4:
                divide(a, b)
            elif operador == 5:
                exit()
            break
        except ValueError:
            print("Entrada invalida!")
    while True:
        try:
            escolha = int(input("\nGostaria de continuar?\n (1) Sim \n (2) Não\n"))
            if escolha in [1,2]:
                if escolha == 2:
                    exit()
                if escolha == 1:
                    return calculadora()
            else:
                print("Escolha 1 ou 2.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

titulo = "---Calculadora---"
print("=" * len(titulo))
print(titulo)
print("=" * len(titulo))
calculadora()

