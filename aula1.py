

nome = input("Insira o nome :")
idade = input("Qual a idade ?")

if nome and idade:
    print(f"Seu nome é : {nome}")
    print(f"Seu nome invetido é : {nome[::-1]}")

    if ' ' in nome:
        print("Seu nome tem epaço")
    else:
        print("Não tem espaços")

    print(f'Seu nome tem {len(nome)}')
    print(f'primneira letra : {nome[1]}')
    print(f'ultima letra : {nome[-1]}')


else:
    print("algum Campo vazio")



