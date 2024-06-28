## PROJETO REPROGRAMA S03 - 
## PALAVRA "LEI"

No projeto desta semana, pudemos aprender mais sobre Loops e Estruturas de Dados, isso inclui palavras reservadas da linguagem para realizar operações. 
Cronograma da aula: 

 - [x] Iteração
 - [x] Listas
 - [x] Tuplas
 - [x] Sets Conjuntos
 - [x] Dicionários
 - [x] Loop While
 - [x] Loop For

 A aula foi ministrada pela professora Eduarda Arduini👧🏻.

## Objtivo da semana: 



Teremos alguns textos e queremos descobrir qual deles fala sobre leis. Para isso iremos contar a quantidade de vezes que a palavra “lei” ocorre em cada um deles, o que tiver mais ocorrências dessa palavra será o escolhido.  
  
Utilizar os conteúdos aprendidos em sala de aula(for, while, listas/tuplas/dicionários/conjuntos e suas funções).  
  
Na resposta deverá ser impresso quais dos textos foi escolhido.

*Caso queira testar a atividade praticada neste repositório, basta apenas:* 
- Clonar o mesmo na sua máquina
- Abrir o terminal 
- Navegar até o diretório com o nome Lethicia
- Executar cada arquivo no terminal através do comando `"python nome-do-arquivo.py"` e divirta-se. 
Lembrando que o projeto é livre para ser modificado e aberto á melhorias caso lhe interessar. 

## COLAS E CONSULTAS
*Esse espaço está sendo reservado para colas e anotações importantes que possam ser utilizadas sempre que precisar.* 

## Listas Funções

| **Método**   | **Descrição**                                                                           | **Exemplo**                      |
|--------------|-----------------------------------------------------------------------------------------|----------------------------------|
| `append`     | Adiciona um elemento no final da lista                                                   | `lista.append(5)`                |
| `clear`      | Apaga todos os elementos de uma lista                                                    | `lista.clear()`                  |
| `copy`       | Retorna uma cópia dos elementos da lista                                                 | `copia = lista.copy()`           |
| `count`      | Retorna a quantidade de ocorrências de um elemento na lista                              | `qt = lista.count(5)`            |
| `extend`     | Adiciona os elementos de outra lista passada por parâmetro                               | `lista.extend(outra_lista)`      |
| `index`      | Retorna o índice do elemento passado por parâmetro (primeira posição)                    | `pos5 = lista.index(5)`          |
| `insert`     | Adiciona um elemento em uma posição passada por parâmetro (adiciona no final caso a posição não exista) | `lista.insert(3, "João")`        |
| `pop`        | Remove o elemento na posição passada por parâmetro (provoca um erro caso a posição não exista) | `elemento = lista.pop(3)`        |
| `remove`     | Remove o elemento passado por parâmetro (provoca um erro caso o elemento não exista)     | `lista.remove(5)`                |
| `reverse`    | Inverte a ordem dos elementos de uma lista                                               | `lista.reverse()`                |
| `sort`       | Ordena os objetos de uma lista                                                           | `lista.sort(reverse=True)`       |
| `len`      | Retorna a quantidade de elementos de uma lista    | `print(len(lista))`      |
| `max`      | Retorna o maior elemento de uma lista             | `maior = max(lista)`     |
| `min`      | Retorna o menor elemento de uma lista             | `menor = min(lista)`     |
| `sum`      | Retorna o somatório dos elementos de uma lista    | `soma = sum(lista)`      |

## Conjuntos - Sets

| **Método**              | **Descrição**                                                                          | **Exemplo**                      |
|-------------------------|----------------------------------------------------------------------------------------|----------------------------------|
| `add`                   | Adiciona um elemento ao conjunto                                                        | `conj1.add(5)`                   |
| `clear`                 | Apaga todos os elementos de um conjunto                                                 | `conj1.clear()`                  |
| `copy`                  | Retorna uma cópia dos elementos de um conjunto                                          | `conj_copia = conj1.copy()`      |
| `difference`            | Retorna o conjunto de elementos de conj1 que não pertencem a conj2                      | `conj1.difference(conj2)`        |
| `intersection`          | Retorna o conjunto de elementos presentes tanto em conj1 quanto em conj2                | `conj1.intersection(conj2)`      |
| `isdisjoint`            | Retorna True se conj1 e conj2 forem disjuntos (ou seja, não possuem elementos em comum) | `conj1.isdisjoint(conj2)`        |
| `issubset`              | Retorna True se conj1 for um subconjunto de conj2 (conj1 está contido em conj2)         | `conj1.issubset(conj2)`          |
| `issuperset`            | Retorna True se conj1 for um superconjunto de conj2 (conj1 contém conj2)                | `conj1.issuperset(conj2)`        |
| `remove` e `discard`    | Removem um elemento do conjunto                                                         | `conj1.remove(5)` ou `conj1.discard(5)` |
| `symmetric_difference`  | Retorna o conjunto de elementos que não são comuns aos dois conjuntos (o contrário da interseção) | `conj1.symmetric_difference(conj2)` |
| `union`                 | Retorna a união entre 2 conjuntos                                                       | `conj1.union(conj2)`             |

## Dicionários

| **Método**         | **Descrição**                                                                                      | **Exemplo**                                 |
|--------------------|----------------------------------------------------------------------------------------------------|---------------------------------------------|
| `clear`            | Apaga todos os elementos de um dicionário                                                          | `dic.clear()`                               |
| `copy`             | Retorna uma cópia dos elementos de um dicionário                                                   | `dic_copia = dic.copy()`                    |
| `fromkeys`         | Retorna um dicionário a partir de uma sequência de chaves                                          | `exemplo = dic.fromkeys(["k1", "k4", "k5"])`|
| `get`              | Retorna o valor associado a uma chave                                                              | `dic.get("k1")`                             |
| `items`            | Retorna uma visão dos pares chave/valor de um dicionário                                           | `dic.items()`                               |
| `keys`             | Retorna uma visão das chaves de um dicionário                                                      | `dic.keys()`                                |
| `pop`              | Remove e retorna o elemento associado à chave passada por parâmetro (provoca erro se a chave não existir) | `dic.pop(2)`                                |
| `popitem`          | Remove e retorna o último elemento adicionado ao dicionário                                        | `dic.popitem()`                             |
| `setdefault`       | Retorna o valor associado a uma chave (se a chave existir). Caso não exista, insere a chave com o valor (opcional) no dicionário | `dic.setdefault(2, "dois")`                 |
| `update`           | Adiciona ao dicionário os pares de chave/valor de outro dicionário passado por parâmetro           | `dic.update(dic2)`                          |
| `values`           | Retorna uma visão dos valores de um dicionário                                                     | `dic.values()`                              |


## Checklist

 - [x] Dar um Fork no repositório da aula original 
 - [x] Clonar o repositório para a própria máquina
 - [x] Criar uma pasta com o seu nome 
 - [x] Criar um arquivo README.md
 - [x] Criar os respectivos arquivos das atividades para entrega
 - [x] Subir as alterações para o repositóro
 - [x] Criar um Pull Request
 - [x] Criar a descrição do pull request 