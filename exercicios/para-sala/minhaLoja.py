produtos_venda = {
    "blusa": 10,
    "calça": 20,
    "short": 15,
    "vestido": 30,
    "sapato": 25
}

#chegou um produto novo, vamos adicionar
produtos_venda['meia'] = 5


#acabou o short, precisamos remover
produtos_venda.pop('short')


#retirar o último item

produtos_venda.popitem()
# #meu cliente comprou uma blusa, quanto ele gastou?
print(produtos_venda["blusa"])

#meu cliente adicionou esses itens na compra calca, sapato e vestido, qual o novo valor?
valor_tottal = produtos_venda["blusa"]
valor_tottal += produtos_venda["calça"] # += é a soma do novo produto ao valor total
valor_tottal += produtos_venda["sapato"] # soma dele mesmo com o novo produto
valor_tottal += produtos_venda["vestido"]

#vestido mudou de valor, agora é 45
print(produtos_venda)
produtos_venda["vestido"] = 45
#todos os itens tiveram um aumento de 10 reais
for chave in produtos_venda.keys():
    produtos_venda[chave] += 10

#criei um item conjunto, o valor dele é da calca e da blusa somados

produtos_venda['çonjunto'] = produtos_venda["calça"] + produtos_venda['blusa']

#quero saber se uma chave existe no meu dicionário
print('blusa' in produtos_venda)
print('blsa'in produtos_venda)


print(produtos_venda)