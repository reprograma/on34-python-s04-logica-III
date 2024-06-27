def main():
    texto_dengue = "Uma infecção curada de dengue confere ao paciente imunidade contra o tipo de vírus responsável. Por existirem quatro tipos diferentes de vírus, para estar totalmente imunizado, é necessário ter tido contato com todos eles. Caso contrário, a cada contágio com um novo tipo de vírus, os sintomas são mais intensos e o risco de desenvolver a dengue grave é mais alto."
    texto_lei_juridica = "Já num sentido amplo, lei é somente a regra jurídica escrita, excluindo-se dessa aceção, portanto, o costume jurídico. Por fim, numa aceção técnica e específica, a palavra lei designa uma modalidade de regra escrita, que apresenta determinadas características; no direito brasileiro, são técnicas apenas a lei complementar e a lei ordinária."
    texto_futebol_feminino = "Na linha do tempo do futebol feminino brasileiro, ele passou tanto tempo proibido quanto regulamentado: 38 anos. De 1941 a 1979, a lei nacional não permitia a prática do esporte por mulheres devido às “condições da sua natureza”. Já o regulamento da modalidade, que permanece válido até 2021, só foi feito em 1983."
    texto_lei_cossenos = "A lei dos cossenos é uma expressão matemática que relaciona os três lados de um triângulo qualquer. Por não estar restrita ao triângulo retângulo, a lei dos cossenos pode ser entendida como uma generalização do teorema de Pitágoras."
    
    lista_textos = [texto_dengue, texto_lei_juridica, texto_futebol_feminino, texto_lei_cossenos]
    
    maior_numero_leis = 0
    texto_com_mais_leis = ""
    #analise do texto
    for texto in lista_textos:
        numero_leis = 0
        posicao_atual = 0
        while posicao_atual < len(texto):
            if posicao_atual <= len(texto) - 3:
                if (texto[posicao_atual] == 'l' or texto[posicao_atual] == 'L') and texto[posicao_atual + 1] == 'e' and texto[posicao_atual + 2] == 'i':
                    numero_leis += 1
            posicao_atual += 1
        
        if numero_leis > maior_numero_leis:
            maior_numero_leis = numero_leis
            texto_com_mais_leis = texto
    
    print("Texto escolhido:")
    print(texto_com_mais_leis)

main()
