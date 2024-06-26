#Faça um Programa que leia 10 números inteiros e armazene-os num vetor. 
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

def main():
    numeros = input("Digite 10 números separados por vírgula: ")

    # Dividir a string de entrada nos números individuais e converter para inteiros
    vetor = [int(num) for num in numeros.split(',')]

    # Inicializar vetores para números pares e ímpares
    vetor_par = []
    vetor_impar = []

    # Separar os números pares e ímpares
    for num in vetor:
        if num % 2 == 0:
            vetor_par.append(num)
        else:
            vetor_impar.append(num)

    # Imprimir os três vetores
    print(f"Vetor original: {vetor}")
    print(f"Números pares: {vetor_par}")
    print(f"Números ímpares: {vetor_impar}")


main()

