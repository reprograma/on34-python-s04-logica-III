def diario (dia):
    data = "{} de janeiro".format(dia)
    data += "\n___________________\n"
    return data

def main ():
    janeiro = ""
    janeiro += diario(1)
    janeiro += diario(2)
    janeiro += diario(3)
    janeiro += diario(4)
    janeiro += diario(5)
    janeiro += diario(6)
    janeiro += diario(7)
    janeiro += diario(8)
    janeiro += diario(9)
    janeiro += diario(10)

    print(janeiro)

main()