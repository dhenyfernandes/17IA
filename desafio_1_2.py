import os
import re
from collections import Counter


def ler_arquivo(nome):
    try:
        arquivo = open(nome, encoding='UTF-8')
    except:
        return (False, '')
    return (True, arquivo.read())


class ExtractTextInformation():
    def __init__(self, arquivo) -> None:
        self.arquivo = arquivo

    def achar_datas(self):
        return re.findall('\d{2}/\d{2}/\d{4}|\d/\d/\d{2}', self.arquivo)

    def contar_caracteres(self):
        return Counter(re.findall('.', self.arquivo))


os.system('cls')
print('Bem vindo ao teste de arquivos Desafio 1')
while(True):
    nome = input('\nEntre com o nome do arquivo (digite sair para terminar): ')
    if(nome == 'sair'):
        print('\nSempre um prazer te ajudar! Até breve!\n')
        exit()
    teste, arquivo = ler_arquivo(nome)
    if (teste):
        info = ExtractTextInformation(arquivo)
        print('Datas encontradas:\n')
        datas = info.achar_datas()
        for data in datas:
            print(data, end=' | ')
        print('\nQuantidade por caracter:\n')
        qtd = info.contar_caracteres().most_common()
        for key, qtd in qtd:
            print('%s -> %d' % (key, qtd), end=' | ')
    else:
        print('\nArquivo não encontrado\n')
