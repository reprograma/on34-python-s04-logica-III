def main():

    texto1 = "Uma infecção curada de dengue confere ao paciente imunidade contra o tipo de vírus responsável. Por existirem quatro tipos diferentes de vírus, para estar totalmente imunizado, é necessário ter tido contato com todos eles. Caso contrário, a cada contágio com um novo tipo de vírus, os sintomas são mais intensos e o risco de desenvolver a dengue grave é mais alto."
    texto2 = "Já num sentido amplo, lei é somente a regra jurídica escrita, excluindo-se dessa aceção, portanto, o costume jurídico. Por fim, numa aceção técnica e específica, a palavra lei designa uma modalidade de regra escrita, que apresenta determinadas características; no direito brasileiro, são técnicas apenas a lei complementar e a lei ordinária."
    texto3 = "Na linha do tempo do futebol feminino brasileiro, ele passou tanto tempo proibido quanto regulamentado: 38 anos. De 1941 a 1979, a lei nacional não permitia a prática do esporte por mulheres devido às “condições da sua natureza”. Já o regulamento da modalidade, que permanece válido até 2021, só foi feito em 1983. "
    texto4 = "A lei dos cossenos é uma expressão matemática que relaciona os três lados de um triângulo qualquer. Por não estar restrita ao triângulo retângulo, a lei dos cossenos pode ser entendida como uma generalização do teorema de Pitágoras."
    
    textos = [texto1, texto2, texto3, texto4]


    print('{:=^50}'.format(' Quantas vezes aparece a palavra "Lei" '), '\n')

    for texto in textos:
        contagem_texto1 = texto1.split().count("lei")
        contagem_texto2 = texto2.split().count("lei")
        contagem_texto3 = texto3.split().count("lei")
        contagem_texto4 = texto4.split().count("lei")
        contagem_total = [ 0, contagem_texto1, contagem_texto2, contagem_texto3, contagem_texto4]
        
    contagem_maior = max(contagem_total)
    indice_maior = contagem_total.index(max(contagem_total))

    print(f'''No texto 1 a palavra "Lei" aparece: \033[1;31m{contagem_texto1}\033[m vezes
No texto 2 a palavra "Lei" aparece: \033[1;31m{contagem_texto2}\033[m vezes
No texto 3 a palavra "Lei" aparece: \033[1;31m{contagem_texto3}\033[m vezes
No texto 4 a palavra "Lei" aparece: \033[1;31m{contagem_texto4}\033[m vezes''', '\n')


    """Quero buscar o texto sobre direito, para isso quero saber quantas vezes aparece a palavra "lei" em cada texto."""


    """O texto certo será o que contiver mais vezes a palavra lei.
    Após descobrir qual é o texto certo, imprimi-lo aqui"""

    from time import sleep
    print('{:=^50}'.format(' O texto sobre direito é o... '), '\n')
    sleep(2)
    print(f'O \033[1;31mtexto {indice_maior}\033[m, aparecendo a palavra "Lei" {contagem_maior}x', '\n')
    print('{:=^50}'.format(' FIM '))

main()