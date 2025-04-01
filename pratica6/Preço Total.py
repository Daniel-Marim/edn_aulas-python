produtos = [
    {"nome": "Arroz", "preco": 22.50, "quantidade": 0},
    {"nome": "Feijão", "preco": 8.99, "quantidade": 0},
    {"nome": "Macarrão", "preco": 5.75, "quantidade": 0},
    {"nome": "Óleo", "preco": 9.50, "quantidade": 0},
    {"nome": "Leite", "preco": 4.99, "quantidade": 0},
    {"nome": "Açúcar", "preco": 3.89, "quantidade": 0},
    {"nome": "Café", "preco": 15.30, "quantidade": 0},
    {"nome": "Farinha", "preco": 6.45, "quantidade": 0},
    {"nome": "Manteiga", "preco": 12.75, "quantidade": 0},
    {"nome": "Chocolate", "preco": 7.99, "quantidade": 0}
]


def calcular_total():
    return sum(produto["quantidade"] * produto["preco"] for produto in produtos)


while True:
    print("\nLista de produtos:")
    for i, produto in enumerate(produtos, start=1):
        total_individual = produto["quantidade"] * produto["preco"]
        print(
            f"{i} - {produto['nome']} (R$ {produto['preco']:.2f}) - Quantidade: {produto['quantidade']} - Total: R$ {total_individual:.2f}")

    print(f"\nTotal da compra: R$ {calcular_total():.2f}")

    escolha = input("\nEscolha um produto pelo número (ou 'sair' para finalizar): ")

    if escolha.lower() == "sair":
        break

    if escolha.isdigit():
        indice = int(escolha) - 1
        if 0 <= indice < len(produtos):
            produto_escolhido = produtos[indice]

            while True:
                print(f"\nProduto selecionado: {produto_escolhido['nome']} (R$ {produto_escolhido['preco']:.2f})")
                print(f"Quantidade atual: {produto_escolhido['quantidade']}")
                print("1 - Adicionar quantidade")
                print("2 - Diminuir quantidade")
                print("3 - Voltar para a seleção de produtos")

                opcao = input("Escolha uma opção: ")

                if opcao == "1":
                    qtd = input("Quantas unidades deseja adicionar? ")

                    if qtd.isdigit() and int(qtd) > 0:
                        produto_escolhido["quantidade"] += int(qtd)
                        print(f"{qtd} unidade(s) de {produto_escolhido['nome']} adicionadas!")
                        break
                    else:
                        print("Entrada inválida! Digite um número positivo.")

                elif opcao == "2":
                    qtd = input("Quantas unidades deseja remover? ")

                    if qtd.isdigit() and int(qtd) > 0:
                        qtd = int(qtd)
                        if produto_escolhido["quantidade"] >= qtd:
                            produto_escolhido["quantidade"] -= qtd
                            print(f"{qtd} unidade(s) de {produto_escolhido['nome']} removidas!")
                        else:
                            print("Você não pode remover mais do que tem!")
                        break
                    else:
                        print("Entrada inválida! Digite um número positivo.")

                elif opcao == "3":
                    break
                else:
                    print("Opção inválida! Escolha 1, 2 ou 3.")

        else:
            print("Número inválido. Escolha um número da lista.")
    else:
        print("Entrada inválida. Digite um número ou 'sair'.")

print("\nResumo da compra:")
for produto in produtos:
    if produto["quantidade"] > 0:
        total_individual = produto["quantidade"] * produto["preco"]
        print(f"{produto['nome']}: {produto['quantidade']} unidades - Total: R$ {total_individual:.2f}")

print(f"\nTotal final da compra: R$ {calcular_total():.2f}")
print("\nObrigado por comprar conosco!")
