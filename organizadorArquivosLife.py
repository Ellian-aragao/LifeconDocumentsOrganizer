from os.path import isdir
from os import mkdir, removedirs, listdir, rename
from shutil import move
from FilePdf import FilesPdf, PdfAttributes, Date


def findFiles(absolute_path):
    arrayDirOrFiles = listdir(absolute_path)
    files = []
    for oneFileOrDir in arrayDirOrFiles:
        if 'backup' == oneFileOrDir.lower():
            continue
        fullPath = '{}/{}'.format(absolute_path, oneFileOrDir)
        if isdir(fullPath):
            array = findFiles(fullPath)
            for item in array:
                files.append(item)
        else:
            files.append(fullPath)
    return files


def testForMakedirMoveFile():
    arqName = 'teste.txt'
    pathArqTeste = '/home/ellian/code/LifeconDocumentsOrganizer/'
    # try:
    #     print('criado o diretório')
    #     mkdir('teste')
    #     input()
    #     print('movendo pasta')
    #     move('{}{}'.format(pathArqTeste, arqName),
    #          '{}{}'.format(pathArqTeste, 'teste/'))
    #     input()
    #     removedirs('../teste')
    # except Exception as identifier:
    #     print('erro -> {}'.format(identifier))
    rename('{}{}'.format(pathArqTeste, arqName), 'teste2.txt')
    move('{}{}'.format(pathArqTeste, 'teste2.txt'),
         '{}{}'.format(pathArqTeste, 'teste/'))

if __name__ == "__main__":
    path = '/home/ellian/Documents/lifecon/orgDocuments/fever'
    arrayPaths = findFiles(path)
    arrayObjects = []
    for pathPdf in arrayPaths:
        # print(pathPdf)
        try:
            arrayObjects.append(FilesPdf(pathPdf))
        except Exception as erro:
            print('ERRO -> {}'.format(erro))

