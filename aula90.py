import os

lista = []

while True: 
    os.system('cls')
    opcao = input("Selecione uma opção [i]nserir [a]pagar [l]istar: ")

    if opcao == "i":
        os.system('cls')
        produto = input("Qual produto? ")       
        lista.append(produto)

    elif opcao == 'a':
        os.system('cls')
        indice = input("Qual índice?:  ")
        try:
            indice = int(indice)
            del lista[indice]
            print("Item removido com sucesso!")
        except ValueError:
            print("Digite um número válido")
        except IndexError:
            print("Índice não encontrado")
        except Exception:
            print("Erro desconhecido")

    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print("Nada para listar")
        else:
            print("Lista de compras:")
            for i, valor in enumerate(lista):
                print(i, valor)

    else:
        os.system('cls')
        print("Opção inválida")

    input("\nPressione ENTER para continuar...")
