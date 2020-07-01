from PdfAttributes import Date, PdfAttributes
from Error import FileNameError


class FilesPdf:

    def __init__(self, fullPath):
        self.fullPath = fullPath
        self.pathFileSeparate()
        self.fileAttributesExtractor()

    def pathFileSeparate(self):
        arrayFullPath = self.fullPath.rsplit('/', 1)
        self.nameFile = arrayFullPath[-1]
        arrayFullPath.pop(-1)
        self.pathDir = '/'.join(arrayFullPath)

    def strToDate(self, strDate):
        strDate = strDate.split('.')
        strDate.pop(-1)
        return'.'.join(strDate)

    def fileAttributesExtractor(self):
        arrayAttributes = self.nameFile.split('-')
        lenAtttributes = len(arrayAttributes)
        if lenAtttributes == 5:
            self.pdf = PdfAttributes(
                arrayAttributes[0],
                arrayAttributes[1],
                arrayAttributes[2],
                arrayAttributes[3],
                self.strToDate(arrayAttributes[4])
            )

        elif lenAtttributes == 4:
            self.pdf = PdfAttributes(
                arrayAttributes[0],
                '',
                arrayAttributes[1],
                arrayAttributes[2],
                self.strToDate(arrayAttributes[3])
            )

        else:
            raise FileNameError(self.fullPath)
