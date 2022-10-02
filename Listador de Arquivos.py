from os import listdir

print('|---------------------------------------------------------------------------------------------------------------------|')
print('|                                              LISTADOR DE ARQUIVOS v1.0                                              |')
print('|---------------------------------------------------------------------------------------------------------------------|')
print('')

diretorio = listdir(input('>>> Informe o Diretório: '))
extensao = input('>>> Informe a Extensão: ')

print('')

a = -1
b = 0

for cont in range (0, len(diretorio)):
    a += 1
    b = diretorio[a]
    print(b[0:(((len(extensao.replace(".", ""))) * (-1)) - 1)])

print('')
input('Aperte Enter para sair...')