def calculo_gorjeta(conta):
    print(f'O calculo da gorjeta ficou: {conta*0.15:.2f}\nMuito obrigado pela preferência!! ')
try:
    valor = float(input("Insira o valor da conta: "))
except ValueError:
    print("Entrada invalida!")
calculo_gorjeta(valor)