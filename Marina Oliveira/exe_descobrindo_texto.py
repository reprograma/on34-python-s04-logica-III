def main():

    texto1 = "Uma infecção curada de dengue confere ao paciente imunidade contra o tipo de vírus responsável. Por existirem quatro tipos diferentes de vírus, para estar totalmente imunizado, é necessário ter tido contato com todos eles. Caso contrário, a cada contágio com um novo tipo de vírus, os sintomas são mais intensos e o risco de desenvolver a dengue grave é mais alto."
    texto2 = "Já num sentido amplo, lei é somente a regra jurídica escrita, excluindo-se dessa aceção, portanto, o costume jurídico. Por fim, numa aceção técnica e específica, a palavra lei designa uma modalidade de regra escrita, que apresenta determinadas características; no direito brasileiro, são técnicas apenas a lei complementar e a lei ordinária."
    texto3 = "Na linha do tempo do futebol feminino brasileiro, ele passou tanto tempo proibido quanto regulamentado: 38 anos. De 1941 a 1979, a lei nacional não permitia a prática do esporte por mulheres devido às “condições da sua natureza”. Já o regulamento da modalidade, que permanece válido até 2021, só foi feito em 1983. "
    texto4 = "A lei dos cossenos é uma expressão matemática que relaciona os três lados de um triângulo qualquer. Por não estar restrita ao triângulo retângulo, a lei dos cossenos pode ser entendida como uma generalização do teorema de Pitágoras."
    
    textos = [texto1, texto2, texto3, texto4]
    
    texto_escolhido = None
    max_ocorrencias = 0
    
    # Iterar sobre cada texto na lista
    for texto in textos:
        # Contar o número de ocorrências da palavra "lei" no texto atual
        ocorrencias_lei = texto.lower().count("lei")
        
        # Verificar se este texto tem mais ocorrências do que o máximo encontrado até agora
        if ocorrencias_lei > max_ocorrencias:
            max_ocorrencias = ocorrencias_lei
            texto_escolhido = texto
    
    # Imprimir o texto que contém mais ocorrências da palavra "lei"
    print("Texto com mais ocorrências da palavra 'lei':")
    print(texto_escolhido)

    """Quero buscar o texto sobre direito, para isso quero saber quantas vezes 
    aparece a palavra "lei" em cada texto."""



    """O texto certo será o que contiver mais vezes a palavra lei.
    Após descobrir qual é o texto certo, imprimi-lo aqui"""
    #print(texto_escolhido)

main()