#Tentei criar uma função, mas não tive muito sucesso. Tentei puxar ela e não rolou. Na verdade acho que ainda tenho bastante dúvida com sintaxe e lógica da sintaxe de funções


def identifica (texto,texto_extraido):
    texto = []
    texto_extraido = texto [0]
    for procura in texto:
        texto = texto_extraido.split()
        contagem = texto.count ("lei")

        if contagem > 0:
            print ("A palavra lei aparece no texto", contagem, "vezes")

        else:
            print ("A palavra lei não aparece no texto")

    return        

#Como não consegui criar a função, tive que colocar o mesmo código para todos os textos individualmente. Também não consegui trabalhar com eles diretamente na lista "textos", e por isso tive que transformar cada str em uma lista

texto1 = ["Uma infecção curada de dengue confere ao paciente imunidade contra o tipo de vírus responsável. Por existirem quatro tipos diferentes de vírus, para estar totalmente imunizado, é necessário ter tido contato com todos eles. Caso contrário, a cada contágio com um novo tipo de vírus, os sintomas são mais intensos e o risco de desenvolver a dengue grave é mais alto."]
texto2 = ["Já num sentido amplo, lei é somente a regra jurídica escrita, excluindo-se dessa aceção, portanto, o costume jurídico. Por fim, numa aceção técnica e específica, a palavra lei designa uma modalidade de regra escrita, que apresenta determinadas características; no direito brasileiro, são técnicas apenas a lei complementar e a lei ordinária."]
texto3 = ["Na linha do tempo do futebol feminino brasileiro, ele passou tanto tempo proibido quanto regulamentado: 38 anos. De 1941 a 1979, a lei nacional não permitia a prática do esporte por mulheres devido às “condições da sua natureza”. Já o regulamento da modalidade, que permanece válido até 2021, só foi feito em 1983. "]
texto4 = ["A lei dos cossenos é uma expressão matemática que relaciona os três lados de um triângulo qualquer. Por não estar restrita ao triângulo retângulo, a lei dos cossenos pode ser entendida como uma generalização do teorema de Pitágoras."]
    
textos = [texto1, texto2, texto3, texto4]

#Não sei como impedir que a mensagem do código apareça tantas vezes, até joguei um break e ele deu uma amenizada, mas não resolveu. Além disso, o if e o else não estão se excluindo entre si. Nos textos onde "lei" aparece tá rolando print de ambos, até tentei impedir com o break mas parece que não rolou

#texto1

for busca in textos:
    texto_extraido = texto1[0]
    for procura in texto1:
        texto1 = texto_extraido.split()
        contagem1 = texto1.count ("lei")

        if contagem1 > 0:
            print ("A palavra lei aparece no texto 1", contagem1, "vezes")
            break

        else:
            print ("A palavra lei não aparece no texto 1")
            break

print ("______________________________________________________________\n")            
            
#texto2

for busca in textos:
    texto_extraido = texto2[0]
    for procura in texto2:
        texto2 = texto_extraido.split()
        contagem2 = texto2.count ("lei")
 
        if contagem2 > 0:
            print ("A palavra lei aparece no texto 2", contagem2, "vezes")
            break

        else:
            print ("A palavra lei não aparece no texto 2")
            break    

print ("______________________________________________________________\n")  

#texto3

for busca in textos:
    texto_extraido = texto3[0]
    for procura in texto3:
        texto3 = texto_extraido.split()
        contagem3 = texto3.count ("lei")

        if contagem3 > 0:
            print ("A palavra lei aparece no texto 3", contagem3, "vezes")
            break

        else:
            print ("A palavra lei não aparece no texto 3")
            break

print ("______________________________________________________________\n")  

#texto4

for busca in textos:
    texto_extraido = texto4[0]
    for procura in texto4:
        texto4 = texto_extraido.split()
        contagem4 = texto4.count ("lei")

        if contagem4 > 0:
            print ("A palavra lei aparece no texto 4", contagem4, "vezes")
            break

        else:
            print ("A palavra lei não aparece no texto 4")
            break    

print ("______________________________________________________________\n")  


#Aqui tentei colocar os resultados em uma lista na tentativa de ordená-los para imprimir o de maior resultado. Também não rolou :(

resultado = [contagem1, contagem2, contagem3, contagem4]
max_resultados = resultado.index(max(resultado))
print (max_resultados)


   