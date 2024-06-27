def main():

    texto1 = "Uma infecção curada de dengue confere ao paciente imunidade contra o tipo de vírus responsável. Por existirem quatro tipos diferentes de vírus, para estar totalmente imunizado, é necessário ter tido contato com todos eles. Caso contrário, a cada contágio com um novo tipo de vírus, os sintomas são mais intensos e o risco de desenvolver a dengue grave é mais alto."
    texto2 = "Já num sentido amplo, lei é somente a regra jurídica escrita, excluindo-se dessa aceção, portanto, o costume jurídico. Por fim, numa aceção técnica e específica, a palavra lei designa uma modalidade de regra escrita, que apresenta determinadas características; no direito brasileiro, são técnicas apenas a lei complementar e a lei ordinária."
    texto3 = "Na linha do tempo do futebol feminino brasileiro, ele passou tanto tempo proibido quanto regulamentado: 38 anos. De 1941 a 1979, a lei nacional não permitia a prática do esporte por mulheres devido às “condições da sua natureza”. Já o regulamento da modalidade, que permanece válido até 2021, só foi feito em 1983. "
    texto4 = "A lei dos cossenos é uma expressão matemática que relaciona os três lados de um triângulo qualquer. Por não estar restrita ao triângulo retângulo, a lei dos cossenos pode ser entendida como uma generalização do teorema de Pitágoras."
    
    textos = [texto1, texto2, texto3, texto4]

    """Quero buscar o texto sobre direito, para isso quero saber quantas vezes 
    aparece a palavra "lei" em cada texto."""
    
    # Cria um dicionário contador para salvar a quantidade de palavras em cada índice da lista textos
    contador = {
        0: 0,
        1: 0,
        2: 0,
        3: 0
    }
    
    # Faz um for em textos para pegar cada texto separado
    for texto in textos:
        # Separa as palavras em uma lista
        palavras = texto.split(' ')
        # Faz um for na lista de palavras
        for palavra in palavras:
            # Compara cada palavra com a palavra 'lei'
            if palavra.lower() == 'lei':
                # Soma 1 na chave do dicionário contador que é igual ao índice de texto na lista textos cada vez que a palavra atual for 'lei'
                contador[textos.index(texto)] += 1
    # Pega a chave ( que é igual ao índice que será escolhido ) que possui o maior valor 
    indice_do_maior_valor = max(contador, key=contador.get)

    # Escolhe um índice com base no retorno da chave do contador que tem o maior valor 
    texto_escolhido = textos[indice_do_maior_valor]

    """O texto certo será o que contiver mais vezes a palavra lei.
    Após descobrir qual é o texto certo, imprimi-lo aqui"""
    print(texto_escolhido)
    
main()