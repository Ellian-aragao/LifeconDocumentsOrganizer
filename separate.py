import os
import sys

pathArqTeste = '/home/ellian/Documents/lifecon/orgDocuments/fever/exemplo/teste'
array = os.listdir(pathArqTeste)
# array = sys.argv
# array.pop(0)
# print(array)
indice = 1

for nomeDoPdf in array:
    os.system('cd {};pwd'.format(pathArqTeste))
    stringArguments = 'pdfseparate -f {} -l {} \'{}\' \'%d-{}\''.format(indice,indice,nomeDoPdf,nomeDoPdf)
    print(stringArguments)
    os.system(stringArguments)
