def impar_par(lista):
    impar = 0
    par = 0
    for num in lista:
        if num % 2 == 0:
            par += 1
            print(f'\n {num} é Par')
        else:
            impar += 1
            print(f'\n {num} é Impar')
    print(f'\nTotal: Impar = {impar} | Par = {par}')

numeros = []

titulo = "---Impar/Par---"
print("=" * len(titulo))
print(titulo)
print("=" * len(titulo))
while True:
    try:
        entrada = input("Digite um numero ou 'parar' pra sair: ")
        if entrada.lower() == "parar":
            break
        numero = int(entrada)
        numeros.append(numero)

    except ValueError:
        print("Entrada invalida!")
if not numeros:
    print("Nenhum numero digitado foi encontrado.")
else:
    impar_par(numeros)