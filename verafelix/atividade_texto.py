# Teremos alguns textos e queremos descobrir qual deles fala sobre leis.
# Para isso iremos contar a quantidade de vezes que a palavra “lei”
#  ocorre em cada um deles, o que tiver mais ocorrências dessa palavra será o escolhido.
# Já temos os textos no arquivo DescobreTexto.py.

def main():
    texto1 = "Uma infecção curada de dengue confere ao paciente imunidade contra o tipo de vírus responsável. Por existirem quatro tipos diferentes de vírus, para estar totalmente imunizado, é necessário ter tido contato com todos eles. Caso contrário, a cada contágio com um novo tipo de vírus, os sintomas são mais intensos e o risco de desenvolver a dengue grave é mais alto."
    texto2 = "Já num sentido amplo, lei é somente a regra jurídica escrita, excluindo-se dessa aceção, portanto, o costume jurídico. Por fim, numa aceção técnica e específica, a palavra lei designa uma modalidade de regra escrita, que apresenta determinadas características; no direito brasileiro, são técnicas apenas a lei complementar e a lei ordinária."
    texto3 = "Na linha do tempo do futebol feminino brasileiro, ele passou tanto tempo proibido quanto regulamentado: 38 anos. De 1941 a 1979, a lei nacional não permitia a prática do esporte por mulheres devido às “condições da sua natureza”. Já o regulamento da modalidade, que permanece válido até 2021, só foi feito em 1983. "
    texto4 = "A lei dos cossenos é uma expressão matemática que relaciona os três lados de um triângulo qualquer. Por não estar restrita ao triângulo retângulo, a lei dos cossenos pode ser entendida como uma generalização do teorema de Pitágoras."

    textos = [texto1, texto2, texto3, texto4]

    def contar_ocorrencias(texto, palavra):
        return texto.lower().split().count(palavra)

    palavra_chave = "lei"
    contagens = [contar_ocorrencias(texto, palavra_chave) for texto in textos]

    max_ocorrencias = max(contagens)
    indice_texto_escolhido = contagens.index(max_ocorrencias)
    texto_escolhido = textos[indice_texto_escolhido]

    print("Texto escolhido:")
    print(texto_escolhido)


main()
