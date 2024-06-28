def compare_textos():
    texto1 = "Uma infecção curada de dengue confere ao paciente imunidade contra o tipo de vírus responsável. Por existirem quatro tipos diferentes de vírus, para estar totalmente imunizado, é necessário ter tido contato com todos eles. Caso contrário, a cada contágio com um novo tipo de vírus, os sintomas são mais intensos e o risco de desenvolver a dengue grave é mais alto."
    texto2 = "Já num sentido amplo, lei é somente a regra jurídica escrita, excluindo-se dessa aceção, portanto, o costume jurídico. Por fim, numa aceção técnica e específica, a palavra lei designa uma modalidade de regra escrita, que apresenta determinadas características; no direito brasileiro, são técnicas apenas a lei complementar e a lei ordinária."
    texto3 = "Na linha do tempo do futebol feminino brasileiro, ele passou tanto tempo proibido quanto regulamentado: 38 anos. De 1941 a 1979, a lei nacional não permitia a prática do esporte por mulheres devido às “condições da sua natureza”. Já o regulamento da modalidade, que permanece válido até 2021, só foi feito em 1983. "
    texto4 = "A lei dos cossenos é uma expressão matemática que relaciona os três lados de um triângulo qualquer. Por não estar restrita ao triângulo retângulo, a lei dos cossenos pode ser entendida como uma generalização do teorema de Pitágoras."

    todos_os_textos = [ texto1 , texto2, texto3, texto4 ]

    quantidade_lei = []
    conte_texto = 0

    for texto in todos_os_textos:
        texto_splitado = texto.split()
        conte_texto += 1

        conte_palavra_lei = texto_splitado.count("lei")
        quantidade_lei.append(conte_palavra_lei)

        print(f" TEXTO {conte_texto} ")
        print(f" A palavra lei aparece {conte_palavra_lei} vezes") 


    maior_index = quantidade_lei.index(max(quantidade_lei))
    maior_lei = max(quantidade_lei)
    print(f" O texto jurídico é o texto {maior_index+1} \n {todos_os_textos[maior_index]}")

    
compare_textos()