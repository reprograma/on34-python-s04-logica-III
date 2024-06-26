# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".


def main():
    perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?" ]

    # Lista de perguntas
    perguntas = [
        "Telefonou para a vítima?",
        "Esteve no local do crime?",
        "Mora perto da vítima?",
        "Devia para a vítima?",
        "Já trabalhou com a vítima?"
    ]

    # Inicializar contador de respostas positivas
    respostas_positivas = 0

    # Fazer as perguntas e contar respostas positivas
    for pergunta in perguntas:
        resposta = input(pergunta + " (sim/não): ").strip().lower()
        if resposta == "sim":
            respostas_positivas += 1

    # Determinar a classificação final
    if respostas_positivas == 2:
        print("Suspeita")
    elif 3 <= respostas_positivas <= 4:
        print("Cúmplice")
    elif respostas_positivas == 5:
        print("Assassino")
    else:
        print("Inocente")


main()