class FolderGestor:
    def __init__(self, root):
        self.root = root
        self.banks = dict()

    def appendBank(self, bank):
        bank = bank.upper()
        self.banks.update({bank: dict()})
        return bank

    def appendMonth(self, bank, month):
        bank = self.appendBank(bank)
        self.banks[bank].update({month: dict()})
        return bank

    def appendDay(self, bank, month, day):
        bank = self.appendMonth(bank, month)
        self.banks[bank][month].update({day: list()})
        return bank

    def appendFile(self, bank, month, day, file):
        bank = self.appendDay(bank, month, day)
        if not day in self.banks[bank][month][day]:
            self.banks[bank][month][day].append(file)

    def bankToArray(self):
        return self.banks.keys()

    def monthToArray(self, bank):
        return self.banks[bank].keys()

    def dayToArray(self, bank, month):
        return self.banks[bank][month].keys()

    def fileToArray(self, bank, month, day):
        return self.banks[bank][month][day]


if __name__ == "__main__":
    path = '/home/ellian/Documents/lifecon/orgDocuments/fever/teste'
    folderObj = FolderGestor(path)
    bank = 'BB'
    for month in ['01', '02', '03']:
        folderObj.appendDay(bank, month, month)
        folderObj.appendDay(bank, month, month)
    # listArray = folderObj.fileToArray(bank, '01', '01')
    print(folderObj.banks)
