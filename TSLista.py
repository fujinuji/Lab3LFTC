class TSLista:
    def __init__(self):
        self.__tsList = []
        self.__index = 1

    def add(self, atom):
        self.__tsList.append((atom, self.__index))
        self.__index += 1
        self.__tsList.sort(key=lambda x: x[0])

        return self.__index - 1

    def contains(self, item):
        return item in [x[0] for x in self.__tsList]

    def getTsValue(self, item):
        for x in self.__tsList:
            if x[0] == item:
                return x[1]

    def getTSList(self):
        return self.__tsList