from TSLista import TSLista


class FIPGenerator:
    def __init__(self, lexic):
        self.__tsIDList = TSLista()
        self.__tsCONSTList = TSLista()
        self.__lexic = lexic

    '''
    Genereaza FIP-ul impreuna cu codul atomului, iar in cazul atomilor ID sau CONST
    se ataseaza si codul atomului din TS
    '''
    def generateFIP(self, atoms):
        programAtoms = []
        for atom, atomType in atoms:
            if atomType == 'CONST':
                if self.__tsCONSTList.contains(atom):
                    programAtoms.append(self.__lexic['CONST'][1])
                else:
                    self.__tsCONSTList.add(atom)
                    programAtoms.append(self.__lexic['CONST'][1])
            elif atomType == 'ID':
                if self.__tsIDList.contains(atom):
                    programAtoms.append(self.__lexic['ID'][1])
                else:
                    self.__tsIDList.add(atom)
                    programAtoms.append(self.__lexic['ID'][1])
            else:
                programAtoms.append(self.__lexic[atomType][1])
        return self.__tsIDList, self.__tsCONSTList, programAtoms