''' Class Person: an individual to be scheduled on the road map. @name: the Persons name. @startTime: the time the
    individual is scheduled to work. @outTime: the time the individual is meant to leave work. @gamesKnow: a list of
    table games that the individual is capable of dealing.
'''


class Person:
    def __init__(self, name, startTime, endTime):
        self.name = name
        self.startTime = startTime
        self.endTime = endTime
       # self.shifts = shifts
        #   self.gamesKnown = gamesKnown
        #self.slots = slots

    def assign(self, slot):
        assert slot in self.slots
        self.shifts -= 1
        self.slots.remove(slot)