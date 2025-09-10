
# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

pontos = 0 

for pergunta in perguntas:
    print(pergunta['Pergunta'])

    for i, opcao in enumerate(pergunta['Opções'], start=1):
        print(f"{i}) {opcao}")
        
    while True:  # repete até digitar uma opção válida
        escolha = input("Escolha uma opção: ")

        if not escolha.isdigit():
            print("⚠️ Digite apenas números.")
            continue

        indice = int(escolha) - 1

        if 0 <= indice < len(pergunta['Opções']):
            break
        else:
            print(f"⚠️ Escolha um número entre 1 e {len(pergunta['Opções'])}.")
resposta_escolhida = pergunta['Opções'][indice]

if resposta_escolhida == pergunta['Resposta']:
    print("acertou \n")
    pontos += 1 
else: 
     print("Errou") 

print(f"Voce acertou {pontos} de {len(perguntas)} perguntas")

