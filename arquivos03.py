#Criando um arquivo um arquivo

#NO PYTHON, na escrita ele não adiciona QUEBRA DE LINHAS (\n)

# No modo W, Abre um arquivo para adicionar conteúdo. O novo texto será inserido no final do arquivo. 
# Cria o arquivo se ele não existir.

arquivo = open('arquivos\\pasta02\\outro_arquivo_02.txt', 'a', encoding='utf-8')

while True:
    msg = input('Nome do aluno: ')

    if msg == 'fechar!':
        break

    arquivo.write(msg + '\n')
arquivo.close()