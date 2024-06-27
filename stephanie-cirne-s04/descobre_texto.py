texto1 = "Uma infecção curada de dengue confere ao paciente imunidade contra o tipo de vírus responsável. Por existirem quatro tipos diferentes de vírus, para estar totalmente imunizado, é necessário ter tido contato com todos eles. Caso contrário, a cada contágio com um novo tipo de vírus, os sintomas são mais intensos e o risco de desenvolver a dengue grave é mais alto."
texto2 = "Já num sentido amplo, lei é somente a regra jurídica escrita, excluindo-se dessa aceção, portanto, o costume jurídico. Por fim, numa aceção técnica e específica, a palavra lei designa uma modalidade de regra escrita, que apresenta determinadas características; no direito brasileiro, são técnicas apenas a lei complementar e a lei ordinária."
texto3 = "Na linha do tempo do futebol feminino brasileiro, ele passou tanto tempo proibido quanto regulamentado: 38 anos. De 1941 a 1979, a lei nacional não permitia a prática do esporte por mulheres devido às “condições da sua natureza”. Já o regulamento da modalidade, que permanece válido até 2021, só foi feito em 1983. "
texto4 = "A lei dos cossenos é uma expressão matemática que relaciona os três lados de um triângulo qualquer. Por não estar restrita ao triângulo retângulo, a lei dos cossenos pode ser entendida como uma generalização do teorema de Pitágoras."
    
textos = [texto1, texto2, texto3, texto4]

#Criamos a função "contador" com o objetivo de percorrer por dentro de cada str, contando a palavra "lei", adicionamos o +1 para contar o número de vezes que a "lei" aparece

def contador (texto):
        texto_extraido = texto.split()
        contagem = 0
        for palavra_encontrada in texto_extraido:
            if palavra_encontrada == "lei":
                contagem +=1

        return contagem        

#Na função "identifica" contamos qual str da lista possui o maior número de vezes que a palavra lei aparece

def identifica (textos):
    resultado = []
    for texto in textos:
        quantidade = contador (texto)
        resultado.append (quantidade)

#Na função "enumerate" retorna a posição e o valor da lista dentro de resultado e percorra dentro dele. Enumerate retorna a posição e o valor. O segundo if vai checar qual é o maior da lista e identificar a sua posição

    for posicao, valor in enumerate (resultado):
        if posicao == 0:
            maior_valor = valor
            posicao_maior_valor = posicao +1

        if valor > maior_valor:
            maior_valor = valor
            posicao_maior_valor = posicao +1
            
    return posicao_maior_valor
    
        
posicao_maior_valor = identifica (textos)        
print (f"O texto com maior número da palavra lei é o texto número {posicao_maior_valor}")