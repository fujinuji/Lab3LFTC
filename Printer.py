import xlsxwriter


class Printer:
    def __init__(self, fileName):
        self.__workbook = xlsxwriter.Workbook(fileName)
        self.__worksheet = self.__workbook.add_worksheet()

    def printConsoleStyle(self, fip, tsIDList, tsCONSTList):
        print("FIP: ", fip)
        print("")
        print("ID TS")
        for element in tsIDList.getTSList():
            print(element[1], " ", element[0])
        print("")
        print("CONST TS")
        for element in tsCONSTList.getTSList():
            print(element[1], " ", element[0])
        print("")

    '''
    Crearea fisierului excel impreuna cu haderele si datele 
    '''
    def writeFile(self, atoms, programAtoms, tsIDList, tsCONSTList):
        self.writeHeader()
        #self.writeAtoms(atoms)
        self.writeProgramAtoms(programAtoms)
        self.writeTS(tsIDList, tsCONSTList)

    '''
    Scrierea hederului pentru tabela
    '''
    def writeHeader(self):
        merge_format = self.__workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': 'yellow'})


        cell_format = self.__workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': 'orange'})

        #self.__worksheet.merge_range('A1:A2', "Atom lexical", merge_format)
        #self.__worksheet.merge_range('B1:B2', "Cod atom", merge_format)
        #self.__worksheet.merge_range('C1:C2', "Program", merge_format)
        self.__worksheet.merge_range('D1:E1', "FIP", merge_format)
        self.__worksheet.write('D2', 'Cod atom', cell_format)
        self.__worksheet.write('E2', 'Cod TS', cell_format)
        self.__worksheet.merge_range('F1:G1', 'Tabel TS', merge_format)
        self.__worksheet.write('F2', 'Simbol', cell_format)
        self.__worksheet.write('G2', 'Id', cell_format)

    '''
    Scrierea atomilor impreuna cu codurilor acestora ca informatii
    '''
    def writeAtoms(self, listOfAtoms):
        row = 3
        for atom in listOfAtoms:
            self.__worksheet.write_string('A' + str(row),  str(listOfAtoms[atom][0]))
            self.__worksheet.write_string('B' + str(row), str(listOfAtoms[atom][1]))

            row += 1

    '''
    Scrierea in fisier a atomilor programului impreuna cu codul
    de atom si codul din TS
    '''
    def writeProgramAtoms(self, programAtoms):
        row = 3
        print("FIP: ")
        for token in programAtoms:
            #self.__worksheet.write_string('C' + str(row), str(token[0]))
            #self.__worksheet.write_string('D' + str(row), str(token[1]))
            #self.__worksheet.write_string('E' + str(row), str(token[2]))
            print(token[1], end=" ")
            row += 1
        print()

    '''
        Scrierea in fisier a atomilor programului impreuna cu codul
        de atom si codul din TS
    '''
    def writeTS(self, tsIDList, tsConstList):
        cell_format = self.__workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': 'green'})

        self.__worksheet.merge_range('F2:G2', 'ID TS', cell_format)
        self.__worksheet.write('F3', 'Simbol', cell_format)
        self.__worksheet.write('G3', 'Id', cell_format)

        row=4

        for symbol, symbolId in tsIDList.getTSList():
            self.__worksheet.write('F' + str(row), symbol)
            self.__worksheet.write('G' + str(row), symbolId)

            row += 1

        self.__worksheet.merge_range('F' + str(row) + ':G' + str(row), 'CONST TS', cell_format)
        row += 1
        self.__worksheet.write('F' + str(row), 'Simbol', cell_format)
        self.__worksheet.write('G' + str(row), 'Id', cell_format)

        row += 1

        for symbol, symbolId in tsConstList.getTSList():
            self.__worksheet.write('F' + str(row), symbol)
            self.__worksheet.write('G' + str(row), symbolId)

            row += 1

        self.__workbook.close()