# Faça um Programa que leia uma lista A com 10 números inteiros, calcule e mostre a soma dos
# quadrados dos elementos do vetor.


def soma_dos_quadrados():
    numeros = input("Digite 10 números separados por vírgula: ")
    lista_usuario = numeros.split(",")
    
    lista_quadrado = []
    for item in lista_usuario:
        item_int = int(item)
        item_quadrado = item_int ** 2
        lista_quadrado.append(item_quadrado) 
    
    total = 0
    for num_quadrado in lista_quadrado:
        total += num_quadrado 
    print(total)

soma_dos_quadrados()