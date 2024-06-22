def main():
    frutas=["abacaxi"]
    frutas.append("uva")#adicionar 1 item
    frutas.extend(["morango","banana", "graviola"]) #adicionar + de 1 item
    print(frutas[3])
    print(frutas.index("banana"))
    frutas.sort(reverse=True)
    print(len(frutas))
    frutas.pop(4)



    print(frutas)

main()