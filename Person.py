''' Class Person: an individual to be scheduled on the road map. @name: the Persons name. @startTime: the time the
    individual is scheduled to work. @outTime: the time the individual is meant to leave work. @gamesKnow: a list of
    table games that the individual is capable of dealing.
'''


class Person:
    def __init__(self, name, startTime, outTime, gamesKnown):
        self.name = name
        self.startTime = startTime
        self.outTime = outTime
        self.gamesKnown = gamesKnown


print("tests")

