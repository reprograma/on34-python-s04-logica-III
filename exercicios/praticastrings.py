def palavra_contem(nome,letra):
    if nome[0]==letra:
        print(" O nome '{}' contém a letra '{}'".format(nome,letra))

    elif nome[1]==letra:
        print(" O nome '{}' contém a letra '{}'".format(nome,letra))

    elif nome[2]==letra:
        print(" O nome '{}' contém a letra '{}'".format(nome,letra))

    
    elif nome[3]==letra:
        print(" O nome '{}' contém a letra '{}'".format(nome,letra))

def main():
    palavra_contem("Maria", "a")
    palavra_contem("Maria", "c")



main ()        