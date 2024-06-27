#Nessa função voces irão receber o valor do troco e irá imprimir quantidade de cada nota usada
def gera_troco(valor_do_troco, notas):
    
    if valor_do_troco > 238:
        print("Infelizmente, não há troco")
    elif valor_do_troco < 0:
        print("Valor pago é menor que valor do produto. Não há troco")
    elif valor_do_troco == 0:
        print("Valor pago é igual ao valor do produto. Não há troco")
    else:
        notas_usadas = {}
        for valor_nota in notas.keys():
            quantidade_nota = valor_do_troco // valor_nota
            valor_do_troco -= valor_nota * quantidade_nota
            notas[valor_nota] -= quantidade_nota
            notas_usadas[valor_nota] = quantidade_nota
        
        print(f"A quantidade usada de cada nota para o troco é: {notas_usadas}")


#Nessa função voces irão receber o valor do produto e o valor que a pessoa pagou e retornar o troco
def calcula_valor_troco(valor_produto, valor_pago):
    valor_do_troco = valor_pago - valor_produto
    return valor_do_troco

def main():
    #O dicionário estará sempre ordenado das notas maiores para as menores
    notas = {
        50: 3,
        10: 5,
        5: 7,
        1: 3
    }

    #Utilizar valores inteiros, não temos centavos
    valor_produto = int(input("Digite o valor do produto: "))
    valor_pago = int(input("Digite o valor que foi pago: "))
    
    gera_troco(calcula_valor_troco(valor_produto, valor_pago), notas)
    

    """Exemplos de teste: 
    Produto: 50 - Valor Pago: 50 
    Produto: 50 - Valor Pago: 20 
    Produto: 10 - Valor Pago: 50  
    Produto: 1 - Valor Pago : 100    
    Produto: 4 - Valor Pago : 100
    Produto: 32 - Valor Pago : 50
    """
    

main()
