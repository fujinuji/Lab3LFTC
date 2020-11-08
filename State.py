class State:
    def __init__(self, description):
        self.__finalState = False
        self.__description = description
        self.__destinations = {}

    def addDestination(self, alphabetItem, state):
        if alphabetItem not in self.__destinations.keys():
            self.__destinations[alphabetItem] = [state]
        else:
            self.__destinations[alphabetItem].append(state)

    def isFinalState(self):
        return self.__finalState

    def setFinalState(self, state):
        self.__finalState = state

    def getDescription(self):
        return self.__description

    def getDestinations(self):
        return self.__destinations
