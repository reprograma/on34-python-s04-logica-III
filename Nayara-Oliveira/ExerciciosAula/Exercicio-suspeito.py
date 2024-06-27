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
    lista_respostas = []
    for pergunta in perguntas:
        resposta = input(pergunta)
        lista_respostas.append(resposta)
    
    if lista_respostas.count("Sim") == 5:
        print("Assassino")
    elif lista_respostas.count("Sim") == 3 or lista_respostas.count("Sim") == 4:
        print("Cúmplice")
    elif lista_respostas.count("Sim") == 2:
        print("Suspeita")
    else:
        print("Inocente")
main()