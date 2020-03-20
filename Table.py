class Table():
    def __init__(self, gameCode = '', isOpen = False, slotsNeeded = 1, slotsUsed = 0, dealerName = ''):
        self.gameCode = gameCode
        self.isOpen = isOpen
        self.slotsNeeded = slotsNeeded
        self.slotsUsed = slotsUsed
        self.dealerName = dealerName
