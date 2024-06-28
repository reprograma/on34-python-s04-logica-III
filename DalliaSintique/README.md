## Ações realizadas
- Realizado fork do repositório <https://github.com/reprograma/on34-python-s04-logica-III>
- Repositório remoto forkado <https://github.com/DalliaSintique/on34-python-s04-logica-III> clonado no repositório local.
- Criado a pasta DalliaSintique, dentro da pasta principal para a entrega da atividade.
- Criado os arquivos entrega_exercicio.py e README.md dentro da pasta DalliaSintique. 
- Add e comitado as alterações. 
- Enviado as alterações para o repositório remoto (Push).
- Solicitado Pull Request.

## Sobre o código
Criado a função <compare_textos>, onde rodaremos o código. Temos os texto1 texto2, texto3 e texto4. Criado a variável <todos_os_texto> para armazenar os quatro textos em uma lista.
-Criado a variável <quantidade_lei> que a princípio recebe uma lista vazia. 
-Criado a variável <conte_texto> que recebe o valor 0 e será nosso contador. 

Iniciado com "for" e a variável <texto> para rodarmos dentro da lista <todos_os_textos>
-Realizado o "split" de <texto> e armazenado dentro da variável <texto_splitado>
-Realizado a contagem da palavra 'lei' em cada texto, usando texto_splitado.count("lei") e armazenado a contagem na variável <conte_palavra_lei>
A contagem da palavra lei é adicionada a lista <quantidade_lei> usando o comando append.

Para saber qual texto consta a maior ocorrência da palavra lei, usamos  .index(max), para retornarmos o maior índice de contagem da palavra 'lei', dentro da lista que armazena a contagem em cada texto <quantidade_lei>

Por fim, printamos na tela, o número vez que a palavra lei aparece em cada texto. Printamos o texto escolhido - texto jurídico, usando o maior índice encontrado, adicionando +1 ao indice <maior_index+1> apenas para que o índice na lista iguale-se ao número do texto e fique de melhor visualização, ex: índice 1 - texto 1. 