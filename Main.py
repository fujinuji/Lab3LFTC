from Analyzer import Analyzer
from FIPGenerator import FIPGenerator
from Printer import Printer
from Reader import Reader

from os import path

if __name__ == '__main__':
    fileName = ""

    while (True):
        reader = Reader()
        analyzer = Analyzer()
        lexic = analyzer.getFormattedLexic()
        printer = Printer("fip.xlsx")

        print("1. Dati fisierul")
        print("2. Afisati atomii lexicali")
        print("3. Generati FIP")
        print("4. Iesire")
        option = input("Optiune: ")

        try:
            if option == "1":
                fileName = input("Dati numele de fisier: ")

                if not path.exists(fileName):
                    print("Fisier inexistent")
                    continue
            elif option == "2":
                for line in reader.read(fileName):
                    analyzer.analyze(line)

                atoms = analyzer.getAtoms()

                for atom, _ in atoms:
                    print(atom)
            elif option == "3":
                for line in reader.read(fileName):
                    analyzer.analyze(line)

                atoms = analyzer.getAtoms()
                fipGenerator = FIPGenerator(lexic)
                tsIDList, tsCONSTList, programAtoms = fipGenerator.generateFIP(atoms)

                printer.printConsoleStyle(programAtoms, tsIDList, tsCONSTList)
            elif option == "4":
                break
            else:
                print("Optiune invalida")
        except Exception as e:
            print("ERROR: " + str(e))


