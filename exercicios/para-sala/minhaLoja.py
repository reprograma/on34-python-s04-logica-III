produtos_venda = {
    "blusa": 10,
    "calça": 20,
    "short": 15,
    "vestido": 30,
    "sapato": 25
}

#chegou um produto novo, vamos adicionar


#acabou o short, precisamos remover

#tirar o ultimo item
produtos_venda.popitem()

#meu cliente comprou uma blusa, quanto ele gastou?


#meu cliente adicionou esses itens na compra calca, sapato e vestido, qual o novo valor?


#vestido mudou de valor, agora é 45


#todos os itens tiveram um aumento de 10 reais


#criei um item conjunto, o valor dele é da calca e da blusa somados
produtos_venda["conjunto"] = produtos_venda["calça"] + produtos_venda["blusa"]
print(produtos_venda)



print(produtos_venda)