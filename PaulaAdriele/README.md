# PROJETO REPROGRAMA S04 - DESCOBRE TEXTO

`Turma Online On34 | Python | Semana 04 | 2024 | Professora Eduarda Arduini`

Esta semana tivemos a oportunidade de aprender sobre **Iteração**

>## O que é iteração?

A iteração é o processo de percorrer os elementos de uma sequência (como listas, tuplas, strings) um por um, executando um bloco de código para cada elemento.

> Exemplos

Loop for: O loop for é usado para iterar sobre cada item de uma sequência.

frutas = ["maçã", "banana", "uva"] 
    for fruta in frutas:
    print(fruta)

>## Listas

 Uma estrutura de dados que armazena uma sequência ordenada de itens. Os itens podem ser de diferentes tipos de dados, como números, strings, booleanos, ou mesmo outras listas.

 Para criar uma lista, basta colocar os elementos entre colchetes [], separados por vírgulas.

 > Funções:


append(): Adiciona um elemento ao final da lista.

insert(): Insere um elemento em uma posição específica.

remove(): Remove a primeira ocorrência de um elemento.

index(): Retorna o índice do primeiro elemento encontrado.

    Strings como listas: As strings podem ser tratadas como listas de caracteres.


> Exemplo:

frutas = ["maçã", "banana", "uva"]

>## Tuplas

Definição: Tuplas são sequências **ordenadas e imutáveis** de elementos. 

São definidas entre parênteses ().

> Exemplos:

coordenadas = (10, 20)

>## Conjuntos

Definição: Conjuntos são coleções **desordenadas e mutáveis** de elementos únicos. São definidos entre chaves {}.

> Exemplos:

frutas = {"maçã", "banana", "uva"}

>## Dicionários

Definição: Dicionários são coleções de pares chave-valor. As chaves devem ser imutáveis (strings, números, tuplas).

> Exemplos:

dicionario = {"nome": "João", "idade": 30}

>## Loops

> Loop while

Executa um bloco de código enquanto uma condição for verdadeira.

> Loop for

Percorre cada elemento de uma sequência, executando um bloco de código para cada elemento.



# Atividade realizada: 

## Exercício de Casa 🏠 

### Qual o assunto do texto?

A atividade consistiu em desenvolver um programa em Python que identifica, entre um conjunto de textos, aquele que mais se relaciona com o tema "leis". Para isso, o código conta quantas vezes a palavra "lei" aparece em cada texto e, então, escolhe o texto com maior ocorrência.

**Comandos utilizados:**

- **`def`**: Define uma função para encapsular o código e facilitar a reutilização.
- **`for`**: Passa por cada item de uma sequência, executando um bloco de código para cada item.
- **`.count()`**: Conta o número de ocorrências de uma substring dentro de uma string.
- **`max()`**: Encontra o valor máximo em uma sequência.
- **`.index()`**: Retorna o índice (posição) de um elemento específico em uma lista.
- **`print()`**: Imprime texto no terminal.


## Dúvidas e processos da atividade:

Para criar o código eu fui descobrindo as funções no decorrer do processo.

Iniciei o código com o que tínhamos aprendido em sala que foi o loop "for" assim sendo a primeira linha do meu código foi:

    for texto in lista_textos:

Em seguida voltei para estudar o material disponibilizado pela professora para relembrar algumas funções. 
Me deparei com a função .count e fui me aprofundar mais sobre como poderia utilizar a função.
Utilizei a função .append, que já tínhamos visto em aula antes para adicionar cada item da lista em uma nova variável que chamei de "quantidade_lei".

Após este processo, eu imprimi a variável "quantidade_lei" para entender o que o código faria. Percebi que o código imprimiu a quatidade de vezes que achou a palavra "Lei" em cada um dos textos.  

Eu conclui que eu precisava gerar um novo código para encontrar qual texto tinha o maior número e mandar imprimeir o maior número. 

Voltei para os slides de apresentação da professora para verificar mais funções e encontrei a função "max.". Fui buscar no Google AI Studio mais informações sobre esta função e como utilizar ela, mas ao colocar a função para rodar notei que ela só estava me retornando o maior número e neste momento não consegui identificar como imprimir o texto que tinha o maior número. 

Voltei ao Google AI Studio e perguntei como imprimir o maior elemento de uma lista e ele me retornou a seguinte resposta:

    "Para encontrar o índice do maior elemento em uma sequência, você pode usar max para encontrar o valor máximo e index para encontrar o índice desse valor.

> Exemplo:

    **temperaturas = [25, 30, 28, 32, 27]**

### Encontrando o índice da maior temperatura em uma linha

**`indice_maior_temperatura = temperaturas.index(max(temperaturas))`**

**`print("O índice da maior temperatura é:", indice_maior_temperatura)`**

Após atualizar o código inserindo o ".index" eu imprimi no terminal e notei que o código me devolveu a posição do texto com maior número.
Me recordei que em aula aprendermos como imprimir um elemento específico e fiz um teste mandando imprimir uma posição aleatória.

Por fim, no local de colocar o número da posição, coloquei a variável e mandei imprimir para verificar se iria funcionar. 



> Local do arquivo:

O arquivo da atividade, PaulaAdriele_DescobreTexto.py, pode ser encontrado na pasta PaulaAdriele.

># Concluindo:
O código final do programa, disponível no arquivo PaulaAdriele_DescobreTexto.py, usa a combinação de funções e loops para realizar a contagem de "lei" em cada texto e, então, imprimir o texto que possui a maior quantidade de ocorrências. A atividade demonstrou a capacidade de utilizar loops, funções e estruturas de dados (listas) em Python para resolver um problema específico. A experiência foi enriquecedora por ter me permitido explorar novas funções e aprimorar meus conhecimentos em Python.