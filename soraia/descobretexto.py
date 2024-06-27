texto1 = "Uma infecção curada de dengue confere ao paciente imunidade contra o tipo de vírus responsável. Por existirem quatro tipos diferentes de vírus, para estar totalmente imunizado, é necessário ter tido contato com todos eles. Caso contrário, a cada contágio com um novo tipo de vírus, os sintomas são mais intensos e o risco de desenvolver a dengue grave é mais alto."
texto2 = "Já num sentido amplo, lei é somente a regra jurídica escrita, excluindo-se dessa aceção, portanto, o costume jurídico. Por fim, numa aceção técnica e específica, a palavra lei designa uma modalidade de regra escrita, que apresenta determinadas características; no direito brasileiro, são técnicas apenas a lei complementar e a lei ordinária."
texto3 = "Na linha do tempo do futebol feminino brasileiro, ele passou tanto tempo proibido quanto regulamentado: 38 anos. De 1941 a 1979, a lei nacional não permitia a prática do esporte por mulheres devido às “condições da sua natureza”. Já o regulamento da modalidade, que permanece válido até 2021, só foi feito em 1983. "
texto4 = "A lei dos cossenos é uma expressão matemática que relaciona os três lados de um triângulo qualquer. Por não estar restrita ao triângulo retângulo, a lei dos cossenos pode ser entendida como uma generalização do teorema de Pitágoras."
    
lista_texto1 = texto1.split()
lista_texto2 = texto2.split()
lista_texto3 = texto3.split()
lista_texto4 = texto4.split()
listas = [lista_texto1, lista_texto2, lista_texto3, lista_texto4]
 
qnt_palavra_lei = 0
def texto_contem(lei,lista):
    qnt_palavra_lei = 0
    for palavra_lei in lista:
        if  palavra_lei == lei:
            qnt_palavra_lei +=1
            
    return qnt_palavra_lei 

qntd_palavras_texto1 = texto_contem("lei",lista_texto1)
qntd_palavras_texto2 = texto_contem("lei",lista_texto2)
qntd_palavras_texto3 = texto_contem("lei",lista_texto3)
qntd_palavras_texto4 = texto_contem("lei",lista_texto4)

print(qntd_palavras_texto1)
print(qntd_palavras_texto2)
print(qntd_palavras_texto3)
print(qntd_palavras_texto4)

if qntd_palavras_texto1 > qntd_palavras_texto2:
    print("O texto escolhido será o texto 1")

if qntd_palavras_texto1 > qntd_palavras_texto3:
    print("O texto escolhido será o texto 1")
    
if qntd_palavras_texto1 > qntd_palavras_texto4:
    print("O texto escolhido será o texto 1")
    
if qntd_palavras_texto2 > qntd_palavras_texto3:
    print("O texto escolhido será o texto 2")
    
if qntd_palavras_texto2 > qntd_palavras_texto4:
    print("O texto escolhido será o texto 2")

if qntd_palavras_texto3 > qntd_palavras_texto4:
    print("O texto escolhido será o texto 3")

