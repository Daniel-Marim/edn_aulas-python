def verifica_senha(key):
    verificador = {
        'Minimo de 8 digitos': len(senha) >= 8,
        'Minimo de uma letra  Maiúcula': any(char.isupper() for char in senha),
        'Minimo de uma letra  minúcula': any(char.islower() for char in senha),
        'Minimo de um numero' : any(char.isdigit() for char in senha),
        'Caractere especial' : any(not char.isalnum() for char in senha),
    }
    return verificador

titulo = "---Verificação--de--Senha---"
print("=" * len(titulo))
print(titulo)
print("=" * len(titulo))
while True:
    try:
        senha = input('Digite sua senha: ')
        resultado = verifica_senha(senha)

        for regra, valido in resultado.items():
            print(f"{regra}: {valido}")

        if all(resultado.values()):
            print('Senha valida!')
            break
        else:
            print('Senha invalida! Complete todos os requisitos.')
    except ValueError:
        print("Entrada invalida!")
