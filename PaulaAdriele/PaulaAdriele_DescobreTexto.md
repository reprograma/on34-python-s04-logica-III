def texto_de_lei():

    texto1 = "Uma infecção curada de dengue confere ao paciente imunidade contra o tipo de vírus responsável. Por existirem quatro tipos diferentes de vírus, para estar totalmente imunizado, é necessário ter tido contato com todos eles. Caso contrário, a cada contágio com um novo tipo de vírus, os sintomas são mais intensos e o risco de desenvolver a dengue grave é mais alto."
    texto2 = "Já num sentido amplo, lei é somente a regra jurídica escrita, excluindo-se dessa aceção, portanto, o costume jurídico. Por fim, numa aceção técnica e específica, a palavra lei designa uma modalidade de regra escrita, que apresenta determinadas características; no direito brasileiro, são técnicas apenas a lei complementar e a lei ordinária."
    texto3 = "Na linha do tempo do futebol feminino brasileiro, ele passou tanto tempo proibido quanto regulamentado: 38 anos. De 1941 a 1979, a lei nacional não permitia a prática do esporte por mulheres devido às “condições da sua natureza”. Já o regulamento da modalidade, que permanece válido até 2021, só foi feito em 1983. "
    texto4 = "A lei dos cossenos é uma expressão matemática que relaciona os três lados de um triângulo qualquer. Por não estar restrita ao triângulo retângulo, a lei dos cossenos pode ser entendida como uma generalização do teorema de Pitágoras."
    
    lista_textos = [texto1, texto2, texto3, texto4]

    quantidade_lei = []
    for texto in lista_textos:
       contagem = texto.count("lei")
       quantidade_lei.append(contagem)
       texto_escolhido = quantidade_lei.index(max(quantidade_lei)) #"Index" Encontra a posição que está o maior número "max"
           
    #print(quantidade_lei) #imprime os número de vezes que foi encontrada a palavra "lei" em cada item da lista
    #print(texto_escolhido) #imprime a posição do texto com mais palavras "lei" encontrada
    #print(lista_textos[3]) #imprime o texto na posição 3
    print("\n------------------------------------------\nO Texto escolhido é o: ", 
    lista_textos[texto_escolhido], "\n------------------------------------------") 
    #imprime O TEXTO da lista de textos na posição encontrada no index

texto_de_lei()
