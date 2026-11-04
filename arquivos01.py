#abrindo um arquivo
# No modo R, ele abri um arquivo. Caso o arquivo não exista no diretório ele retorna um erro!.


#PROCURA O ARQUIVO APENAS NA PASTA ATUAL
#arquivo = open('meu_arquivo.txt', 'r', encoding='utf-8')

#RELATIVE PATH jeito mais seguro[]
arquivo = open('arquivos\\pasta02\\meu_arquivo.txt', 'r', encoding='utf-8')

#FULL PATH
#arquivo = open('C:\\Users\\salustiano.oliveira\\Python\\aula24\\arquivos\\pasta02\\meu_arquivo.txt', 'r', encoding='utf-8')
conteudo = arquivo.read()

print(conteudo)

#fechando um arquivo
arquivo.close()