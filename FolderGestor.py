
class FolderGestor:
    def __init__(self, root):
        self.root = root
        self.banks = dict()

    def appendBank(self, bank):
        bank = bank.upper()
        if not bank in self.banks:
            self.banks.update({bank: dict()})

    def appendMonth(self, bank, month):
        bank = bank.upper()
        if not month in self.banks[bank]:
            self.banks[bank].update({month: list()})

    def appendDay(self, bank, month, day):
        bank = bank.upper()
        if not month in self.banks[bank][month]:
            self.banks[bank][month].append(day)


if __name__ == "__main__":
    path = '/home/ellian/Documents/lifecon/orgDocuments/fever/teste'
    folderObj = FolderGestor(path)
    bank = 'BB'
    folderObj.appendBank(bank)
    for month in ['01', '02', '03', '04']:
        folderObj.appendMonth(bank, month)
        folderObj.appendDay(bank, month, month)
    print(folderObj.banks)
