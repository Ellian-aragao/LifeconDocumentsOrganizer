from PdfAttributes import Date,PdfAttributes
from Error import FileNameError

class FilesPdf:

    def __init__(self, fullPath):
        self.fullPath = fullPath
        self.pdf = PdfAttributes()
        self.pathFileSeparate()
        self.fileAttributesExtractor()


    def pathFileSeparate(self):
        arrayFullPath = self.fullPath.rsplit('/', 1)
        self.nameFile = arrayFullPath[-1]
        arrayFullPath.pop(-1)
        self.pathDir = '/'.join(arrayFullPath)
    
    def strToDate(self, strDate):
        infoDate = strDate.split('.')
        self.pdf.date.day = infoDate[0]
        self.pdf.date.month = infoDate[1]
        self.pdf.date.year = infoDate[2]


    def fileAttributesExtractor(self):
        arrayAttributes = self.nameFile.split('-')
        lenAtttributes = len(arrayAttributes)
        if lenAtttributes == 5:
            self.pdf.bank = arrayAttributes[0]
            self.pdf.contract = arrayAttributes[1]
            self.pdf.description = arrayAttributes[2]
            self.pdf.cost = arrayAttributes[3]
            self.strToDate(arrayAttributes[4])

        elif lenAtttributes == 4:
            self.pdf.bank = arrayAttributes[0]
            self.pdf.contract = ''
            self.pdf.description = arrayAttributes[1]
            self.pdf.cost = arrayAttributes[2]
            self.strToDate(arrayAttributes[3])
        else:
            raise FileNameError(self.fullPath)

if __name__ == "__main__":
    path = '/home/ellian/Documents/lifecon/orgDocuments/arqu/exemplo/(?) - DANFE - PRESTACAO DE SERVICO - 45.263,16 - 01.02.2017.pdf'
    pdf = FilesPdf(path)
    print(pdf)
