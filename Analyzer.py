import re

from AutomatiFinit import AutomatFinit


class Analyzer:
    def __init__(self):
        self.__rules = [
            ('MAIN', r'main'),  # main
            ('INT', r'int'),  # int
            ('FLOAT', r'float'),  # float
            ('STRUCT', r'struct'),  # struct
            ('CIN', r'cin'),  # cin
            ('COUNT', r'cout'),  # cout
            ('CIN_OP', r'>>'),  # >>
            ('COUT_OP', r'<<'),  # <<
            ('WHILE', r'while'),  # while
            ('IF', r'if'),  # if
            ('ELSE', r'else'),  # else
            ('LBRACKET', r'\('),  # (
            ('RBRACKET', r'\)'),  # )
            ('LBRACE', r'\{'),  # {
            ('RBRACE', r'\}'),  # }
            ('COMMA', r','),  # ,
            ('PCOMMA', r';'),  # ;
            ('EQ', r'=='),  # ==
            ('NE', r'!='),  # !=
            ('LE', r'<='),  # <=
            ('GE', r'>='),  # >=
            ('OR', r'\|\|'),  # ||
            ('AND', r'&&'),  # &&
            ('ATTR', r'\='),  # =
            ('LT', r'<'),  # <
            ('GT', r'>'),  # >
            ('PLUS', r'\+'),  # +
            ('MINUS', r'-'),  # -
            ('MULT', r'\*'),  # *
            ('DIV', r'\/'),  # /
            # ('ID', r'[a-zA-Z]\w*'),                 # IDENTIFIERS
            # ('FLOAT_CONST', r'\d(\d)*\.\d(\d)*'),  # FLOAT
            # ('INTEGER_CONST', r'\d(\d)*'),          # INT
            ('NEWLINE', r'\n'),  # NEW LINE
            ('SKIP', r'[ \t]+'),  # SPACE and TABS
            ('MISMATCH', r'.'),  # ANOTHER CHARACTER
        ]

        self.tokens = '|'.join('(?P<%s>%s)' % x for x in self.__rules)
        self.line = 0
        self.atoms = []

    '''
        Optine toti atommi lexicali impreuna cu codurile acestora    
    '''

    def analyze(self, code):
        is_mismatch = False
        mismatch = ""
        for match in re.finditer(self.tokens, code):
            token_type = match.lastgroup
            atom = match.group(token_type)

            if token_type == 'NEWLINE':
                if is_mismatch:
                    is_accepted, type_token = self.checkAtomWithAutomate(mismatch)

                    if is_accepted:
                        self.atoms.append((mismatch, type_token))
                        is_mismatch = False
                        mismatch = ""
                    else:
                        raise Exception("Atom ", mismatch, " is not accepted")

                self.line += 1
            elif token_type == 'SKIP':
                if is_mismatch:
                    is_accepted, type_token = self.checkAtomWithAutomate(mismatch)

                    if is_accepted:
                        self.atoms.append((mismatch, type_token))
                        is_mismatch = False
                        mismatch = ""
                    else:
                        raise Exception("Atom ", mismatch, " is not accepted")

                continue
            elif token_type == 'MISMATCH':
                if not is_mismatch:
                    mismatch = atom
                    is_mismatch = True
                else:
                    mismatch += atom

                # raise RuntimeError('%r unexpected on line %d' % (atom, self.line))
            else:
                if is_mismatch:
                    is_accepted, type_token = self.checkAtomWithAutomate(mismatch)

                    if is_accepted:
                        self.atoms.append((mismatch, type_token))
                        is_mismatch = False
                        mismatch = ""
                    else:
                        raise Exception("Atom ", mismatch, " is not accepted")

                self.atoms.append((atom, token_type))

    def getAtoms(self):
        return self.atoms

    '''
        Itereaza lista de atomi si asigneaza fiecarui atom un id
    '''

    def getFormattedLexic(self):
        atomId = 1
        listOfAtoms = {}
        for token, atom in self.__rules:
            if token == 'ID':
                listOfAtoms['ID'] = ('ID', atomId)
            elif token == 'FLOAT_CONST' or token == 'INTEGER_CONST':
                listOfAtoms['CONST'] = ('CONST', atomId)
            elif token == 'NEWLINE' or token == 'SKIP' or token == 'MISMATCH':
                continue
            else:
                listOfAtoms[token] = (atom.replace("\\", ""), atomId)
            atomId += 1
        listOfAtoms['ID'] = ('ID', 150)
        listOfAtoms['CONST'] = ('CONST', 151)

        return listOfAtoms

    def checkAtomWithAutomate(self, atom):
        identificatoriAF = AutomatFinit("v.txt")
        constatnte = AutomatFinit("s.txt")

        if identificatoriAF.checkSequence(atom):
            return [True, "ID"]
        if constatnte.checkSequence(atom):
            return [True, "CONST"]

        return [False, ""]
