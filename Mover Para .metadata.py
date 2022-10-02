import os
import fnmatch
import shutil
import pathlib

print('|---------------------------------------------------------------------------------------------------------------------|')
print('|                                              MOVER PARA .METADATA v1.0                                              |')
print('|---------------------------------------------------------------------------------------------------------------------|')
print('')

# INPUTS
path = input('>>> Informe o Diretório: ')
pattern = input('>>> Informe a Extensão Checksum Para Procura (exemplo: *.md5): ')

print('')

# VARS
fileList = []

def move_dir(src: str, dst: str, pattern: str = '*'):
    if not os.path.isdir(dst):
        pathlib.Path(dst).mkdir(parents=True, exist_ok=True)
    for f in fnmatch.filter(os.listdir(src), pattern):
        shutil.move(os.path.join(src, f), os.path.join(dst, f))

# CREATE DIR ARRAY
for dName, sdName, fList in os.walk(path):
    for fileName in fList:
        if fnmatch.fnmatch(fileName, pattern):
            fileList.append(os.path.join(dName, fileName))

# AÇÕES
for i in fileList:
    workDir = i[:i.rstrip().rfind("\\")]
    newDir = workDir + str("\\.metadata\\")

    move_dir(workDir, newDir, "*.sfv")
    move_dir(workDir, newDir, "*.md5")
    move_dir(workDir, newDir, "*.sha1")
    move_dir(workDir, newDir, "*.sha2")

    print(str("Movendo Arquivos Para: ") + newDir)

print('')
print('|---------------------------------------------------------------------------------------------------------------------|')
print('|                                        NÃO RODE ESSE SCRIPT MAIS DE UMA VEZ                                         |')
print('|                                                      ATÉ MAIS!                                                      |')
print('|---------------------------------------------------------------------------------------------------------------------|')

print('')
input('Aperte Enter para sair...')