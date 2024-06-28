
def main():

    texto1 = "Uma infecção curada de dengue confere ao paciente imunidade contra o tipo de vírus responsável. Por existirem quatro tipos diferentes de vírus, para estar totalmente imunizado, é necessário ter tido contato com todos eles. Caso contrário, a cada contágio com um novo tipo de vírus, os sintomas são mais intensos e o risco de desenvolver a dengue grave é mais alto."
    texto2 = "Já num sentido amplo, lei é somente a regra jurídica escrita, excluindo-se dessa aceção, portanto, o costume jurídico. Por fim, numa aceção técnica e específica, a palavra lei designa uma modalidade de regra escrita, que apresenta determinadas características; no direito brasileiro, são técnicas apenas a lei complementar e a lei ordinária."
    texto3 = "Na linha do tempo do futebol feminino brasileiro, ele passou tanto tempo proibido quanto regulamentado: 38 anos. De 1941 a 1979, a lei nacional não permitia a prática do esporte por mulheres devido às “condições da sua natureza”. Já o regulamento da modalidade, que permanece válido até 2021, só foi feito em 1983. "
    texto4 = "A lei dos cossenos é uma expressão matemática que relaciona os três lados de um triângulo qualquer. Por não estar restrita ao triângulo retângulo, a lei dos cossenos pode ser entendida como uma generalização do teorema de Pitágoras."
    
    pesquisa_palavra1 = texto1.count("lei")
    pesquisa_palavra2 = texto2.count("lei")
    pesquisa_palavra3 = texto3.count("lei")
    pesquisa_palavra4 = texto4.count("lei")


    if pesquisa_palavra1 > pesquisa_palavra2 and pesquisa_palavra1 > pesquisa_palavra3 and pesquisa_palavra1 > pesquisa_palavra4:
        print(texto1)
    elif pesquisa_palavra2 > pesquisa_palavra1 and pesquisa_palavra2 > pesquisa_palavra3 and pesquisa_palavra2 > pesquisa_palavra4:
        print (texto2)
    elif pesquisa_palavra3 > pesquisa_palavra1 and pesquisa_palavra3 > pesquisa_palavra2 and pesquisa_palavra3 > pesquisa_palavra4:
        print(texto3)
    else:
        print(texto4)


main()
