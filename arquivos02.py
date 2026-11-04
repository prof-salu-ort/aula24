#Criando um arquivo um arquivo

#NO PYTHON, na escrita ele não adiciona QUEBRA DE LINHAS (\n)

lista_times = ['Flamengo\n', 'Vasco\n', 'Botafogo\n', 'Fluminense\n']

# No modo W, ele cria um arquivo novo. Caso já exista o arquivo ele o sobreescreve!
arquivo = open('arquivos\\pasta02\\outro_arquivo.txt', 'w', encoding='utf-8')

arquivo.write('Hello World Python.\n') #escreve no arquivo (sem pular linhas)
arquivo.write('Trabalhando com arquivos.\n') #escreve no arquivo (sem pular linhas)

arquivo.writelines(lista_times)

#fechando um arquivo
arquivo.close()