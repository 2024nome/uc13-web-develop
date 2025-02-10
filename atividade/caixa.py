def menu():
    estoque = {}
    
    while True:
        opcao = input("\n1. Adicionar produto\n2. Atualizar quantidade\n3. Remover produto\n4. Exibir estoque\n5. Calcular valor total\n6. Sair\nEscolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome do produto: ")
            if nome in estoque:
                print("Produto já existe. Use a opção de atualizar.")
                continue
            try:
                estoque[nome] = {"quantidade": int(input("Quantidade: ")), "preco": float(input("Preço unitário: "))}
                print("Produto adicionado com sucesso!")
            except ValueError:
                print("Erro: Insira valores numéricos válidos.")
        elif opcao == "2":
            nome = input("Nome do produto a atualizar: ")
            if nome in estoque:
                try:
                    estoque[nome]["quantidade"] += int(input("Quantidade a adicionar (negativo para remover): "))
                    estoque[nome]["quantidade"] = max(0, estoque[nome]["quantidade"])
                    print("Quantidade atualizada com sucesso!")
                except ValueError:
                    print("Erro: Insira um número válido.")
            else:
                print("Produto não encontrado.")
        elif opcao == "3":
            estoque.pop(input("Nome do produto a remover: "), print("Produto não encontrado."))
        elif opcao == "4":
            print("\nEstoque Atual:")
            for nome, dados in estoque.items():
                print(f"{nome}: {dados['quantidade']} unidades - R$ {dados['preco']:.2f} cada") if estoque else print("Estoque vazio.")
        elif opcao == "5":
            print(f"\nValor total do estoque: R$ {sum(dados['quantidade'] * dados['preco'] for dados in estoque.values()):.2f}")
        elif opcao == "6":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
