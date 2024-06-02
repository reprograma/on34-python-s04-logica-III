#Nessa função voces irão receber o valor do troco e irá imprimir quantidade de cada nota usada
def gera_troco(valor_do_troco, notas):
    pass   

#Nessa função voces irão receber o valor do produto e o valor que a pessoa pagou e retornar o troco
def calcula_valor_troco(valor_produto, valor_pago):
    pass

def main():
    #O dicionário estará sempre ordenado das notas maiores para as menores
    notas = {
        50: 3,
        10: 5,
        5: 7,
        1: 3
    }

    #Utilizar valores inteiros, não temos centavos
    valor_produto = input("Digite o valor do produto: ")
    valor_pago = input("Digite o valor que foi pago:")

    """Exemplos de teste: 
    Produto: 50 - Valor Pago: 50 
    Produto: 50 - Valor Pago: 20 
    Produto: 10 - Valor Pago: 50  
    Produto: 1 - Valor Pago : 100    
    Produto: 4 - Valor Pago : 100
    Produto: 32 - Valor Pago : 50
    """
    

main()
