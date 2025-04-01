def dias_vida(nascimento):
    ano = 2025 - nascimento
    dias = ano * 365
    print(f'Você ja viveu aproximadamente {dias} dias.')
try:
    nascimento = int(input("Ano de nascimento: "))
except ValueError:
    print("Entrada invalida!")
dias_vida(nascimento)