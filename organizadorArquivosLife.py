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


def testForMakedirMoveFile(base_path, pdfObject):
    
    """
    arqName = 'teste.txt'
    pathArqTeste = '/home/ellian/code/LifeconDocumentsOrganizer/'
    try:
        print('criado o diretório')
        mkdir('teste')
        input()
        print('movendo pasta')
        move('{}{}'.format(pathArqTeste, arqName),
             '{}{}'.format(pathArqTeste, 'teste/'))
        input()
        removedirs('../teste')
    except Exception as identifier:
        print('erro -> {}'.format(identifier))
    rename('{}{}'.format(pathArqTeste, arqName), 'teste2.txt')
    move('{}{}'.format(pathArqTeste, 'teste2.txt'),
         '{}{}'.format(pathArqTeste, 'teste/'))
    """


def createArrayPdfsObjects(arrayPaths):
    arrayObjects = []
    for pathPdf in arrayPaths:
        arrayObjects.append(createPdfObject(pathPdf))
    return arrayObjects


def createPdfObject(pathPdf):
    try:
        return FilesPdf(pathPdf)
    except Exception as erro:
        print('ERRO -> {}'.format(erro))


if __name__ == "__main__":
    path = '/home/ellian/Documents/lifecon/orgDocuments'
    # mkdir('{}/fileByPython'.format(path))
    arrayPaths = findFiles(path)
    arrayPdfs = createArrayPdfsObjects(arrayPaths)
