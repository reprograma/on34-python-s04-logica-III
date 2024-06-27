# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos
# quadrados dos elementos do vetor.


def main():
    numeros = input("Digite 10 números separados por vírgula: ")
    vetor_a = [int(num) for num in numeros.split(',')]
    
    if len(vetor_a) != 10:
        print("Você precisa digitar exatamente 10 números inteiros.")
        return
    
    soma_quadrados = sum(num ** 2 for num in vetor_a)

    print(f"A soma dos quadrados dos elementos do vetor é: {soma_quadrados}")

main()

