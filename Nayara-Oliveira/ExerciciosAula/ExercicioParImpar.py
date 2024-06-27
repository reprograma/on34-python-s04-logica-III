#Faça um Programa que leia 10 números inteiros e armazene-os num vetor. 
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

def main():
    numeros = input("Digite 10 números separados por vírgula: ")
    lista_numeros = numeros.split(",")
    lista_par = []
    lista_impar = []
    
    for numero in lista_numeros:
        numero_int = int(numero)
        if numero_int % 2 == 0:
            lista_par.append(numero_int)
        else:
            lista_impar.append(numero_int)
    print(f"A lista de números é: {lista_numeros}")
    print(f"A lista dos números pares é: {lista_par}")
    print(f"A lista dos números ímpares é: {lista_impar}")

main()

