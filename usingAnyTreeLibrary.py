from os import mkdir, listdir
from os.path import isdir
from anytree import *


class FolderGestor:
    def __init__(self, rootPath):
        self.rootPath = rootPath
        self.rootPathNode = Node('root', parent=None)
        self.createNodesPaths(rootPath, parentPrev=self.rootPathNode)

    def createNodesPaths(self, absolute_path, parentPrev):
        node = Node(absolute_path.split('/')[-1], parent=parentPrev)
        arrayDirOrFiles = listdir(absolute_path)
        for oneFileOrDir in arrayDirOrFiles:
            fullPath = '{}/{}'.format(absolute_path, oneFileOrDir)
            if isdir(fullPath):
                self.createNodesPaths(fullPath, node)
            else:
                Node(oneFileOrDir, parent=node)


def renderTree(decedents):
    itens = decedents.descendants
    for i in itens:
        if i.is_leaf:
            renderTree(i.descendants)
        else:
            print('nao tem filhos')


if __name__ == "__main__":
    path = '/home/ellian/Documents/lifecon/orgDocuments/bb/fev_april'
    testeNode = FolderGestor(path)
    renderTree(testeNode)
