class Date:
    def __init__(self, strDate):
        strDate = strDate.split('.')
        self.day = strDate[0]
        self.month = strDate[1]
        self.year = strDate[2]
