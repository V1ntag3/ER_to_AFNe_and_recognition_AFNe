import AFNe.AFNeClass as afne

AFNe = afne.AFNeStruct()


class AFNefromExpReg:

    def __init__(self, expReg):
        self.star = '*'
        self.plus = '+'
        self.dot = '.'
        self.openingBracket = '('
        self.closingBracket = ')'
        self.operators = [self.plus, self.dot]
        self.expReg = expReg
        self.alphabet = [chr(i) for i in range(65,91)]
        self.alphabet.extend([chr(i) for i in range(97,123)])
        self.alphabet.extend([chr(i) for i in range(48,58)])
        self.buildAFNe()

    def displayAFNe(self):
        self.nfa.display()

    def buildAFNe(self):
        language = set()
        self.stack = []
        self.automata = []
        previous = "::e::"
        for char in self.expReg:
            if char in self.alphabet:
                language.add(char)
                if previous != self.dot and (previous in self.alphabet or previous in [self.closingBracket,self.star]):
                    self.addOperatorToStack(self.dot)
                
                self.automata.append(AFNe.basicStruct(char))
            elif char  ==  self.openingBracket:
                if previous != self.dot and (previous in self.alphabet or previous in [self.closingBracket,self.star]):
                    self.addOperatorToStack(self.dot)
                self.stack.append(char)
            elif char  ==  self.closingBracket:
                while(1):
                    o = self.stack.pop()
                    if o == self.openingBracket:
                        break
                    elif o in self.operators:
                        self.processOperator(o)
            elif char == self.star:
                self.processOperator(char)
            elif char in self.operators:
                if previous in self.operators or previous  == self.openingBracket:
                    raise BaseException("Error processing '%s' after '%s'" % (char, previous))
                else:
                    self.addOperatorToStack(char)
            previous = char
        while len(self.stack) != 0:
            op = self.stack.pop()
            self.processOperator(op)
        self.nfa = self.automata.pop()
        self.nfa.language = language

    def addOperatorToStack(self, char):
        while(1):
            if len(self.stack) == 0:
                break
            top = self.stack[len(self.stack)-1]
            if top == self.openingBracket:
                break
            if top == char or top == self.dot:
                op = self.stack.pop()
                self.processOperator(op)
            else:
                break
        self.stack.append(char)

    def processOperator(self, operator):
        if operator == self.star:
            a = self.automata.pop()
            self.automata.append(AFNe.starStruct(a))
        elif operator in self.operators:
            a = self.automata.pop()
            b = self.automata.pop()
            if operator == self.plus:
                self.automata.append(AFNe.plusStruct(b,a))
            elif operator == self.dot:
                self.automata.append(AFNe.dotStruct(b,a))




er = "aa"
nfaObj = AFNefromExpReg(er)
nfa = nfaObj.displayAFNe()

print(nfa)