from Date import Date


class PdfAttributes:
    def __init__(self, bank, contract, description, cost, date):
        self.bank = bank
        self.contract = contract
        self.description = description
        self.cost = cost
        self.date = Date(date)
