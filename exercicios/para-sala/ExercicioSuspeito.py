# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

'''
def main():
    perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?" ]
    

main()
'''
lista_perguntas = ["Telefonou para a vítima?",
                    "Esteve no local do crime?",
                    "Mora perto da vítima?",
                    "Devia para a vítima?", 
                    "Já trabalhou com a vítima?" ]
lista_respostas = []

for pergunta in lista_perguntas:
    resposta = input(pergunta)
    lista_respostas.append(resposta)
print(lista_respostas)

if lista_respostas.count('sim') == 5:
    print('çulpado')
elif lista_respostas.count('sim') == 3:
    print('cumplice')
elif lista_respostas.count('sim') == 4:
    print('cumplice')
elif lista_respostas.count('sim') == 2:
    print('suspeito')
else:
    print('suspeito')