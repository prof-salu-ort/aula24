
#Fecha o arquivo automaticamente assim que ele sai do bloco de execução
with(open('novo_arquivo.txt', 'a')) as arquivo:
    while True:
        msg = input('Nome do aluno: ')

        if msg == 'fechar!':
            break

        arquivo.write(msg + '\n')