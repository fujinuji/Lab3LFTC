from State import State


class AutomatFinit:
    def __init__(self, fileName):
        self.__alphabet = []
        self.__state = {}
        self.__initialState = State("")
        file = open(fileName, 'r')
        self.__setAF(file)


    def __setAF(self, file):
        index = 0
        for line in file:
            line = line.strip()
            if index == 0:
                self.__createStates(line)
                index += 1
            elif index == 1:
                self.__createAlphabet(line)
                index += 1
            elif index == 2:
                self.__setInitialState(line)
                index += 1
            elif index == 3:
                self.__setFinalStates(line)
                index += 1
            else:
                self.__setTransitions(line)

    def __createStates(self, line):
        for state in line:
            if not state in self.__state.keys():
                self.__state[state] = State(state)

    def __createAlphabet(self, line):
        for letter in line:
            if not letter in self.__alphabet:
                self.__alphabet.append(letter)

    def __setInitialState(self, line):
        if line in self.__state.keys():
            self.__initialState = self.__state[line]

    def __setFinalStates(self, line):
        for letter in line:
            for state in self.__state.values():
                if letter == state.getDescription():
                    state.setFinalState(True)

    def __setTransitions(self, line):
        start = line[0]
        end = line[2]
        transit = line[1]
        self.__state[start].addDestination(transit, self.__state[end])

    def __isRoad(self, state, letter):
        return letter in state.getDestinations().keys()

    def checkSequence(self, line):
        line = line.strip()

        i = 0
        result = ""
        buffer = ""

        s = self.__initialState

        while i < len(line) and self.__isRoad(s, line[i]):
            s = s.getDestinations()[line[i]][0]
            buffer += line[i]

            if s.isFinalState():
                result = buffer
            i += 1

        return len(result) == len(line)
