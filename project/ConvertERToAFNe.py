# Converte uma Expressão Regular em Automato Finito de estados Vazios
class ConvertERToAFNe:

    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.transitions = {}
        self.startState = None
        self.finalStates = set()

    def addState(self, state, isStart=False, isFinal=False):
        self.states.add(state)
        if isStart:
            self.startState = state
        if isFinal:
            self.finalStates.add(state)

    def addTransition(self, fromState, toState, symbol):
        if fromState not in self.transitions:
            self.transitions[fromState] = []
        self.transitions[fromState].append((toState, symbol))
        if symbol != 'epsilon':
            self.alphabet.add(symbol)

    def epsilonClosure(self, state):
        closure = set([state])
        if state in self.transitions and None in [symbol for _, symbol in self.transitions[state]]:
            for nextState, symbol in self.transitions[state]:
                if symbol is None and nextState not in closure:
                    closure |= self.epsilonClosure(nextState)
        return closure

    def convertRegex(self, expression):
        currentState = 0
        self.addState(currentState, isStart=True)
        for char in expression:
            if char == '*':
                prevState = currentState - 1
                currentState += 1
                self.addState(currentState)
                print(currentState)
                self.addTransition(currentState-1, prevState, 'epsilon')
                self.addTransition(prevState, currentState, 'epsilon')
                self.addTransition(currentState, prevState, 'epsilon')

            else:
                currentState += 1
                self.addState(currentState)
                self.addTransition(currentState - 1, currentState, char)

        self.addState(currentState, isFinal=True)

    def getStates(self):
        statesArray = []

        for state in self.states:
            statesArray.append('q' + str(state))

        return statesArray

    def getAlphabet(self):
        aphabetArray = []

        for alph in self.alphabet:
            aphabetArray.append(alph)

        return aphabetArray

    def getTransitions(self):
        transitionsDict = dict()
        for fromState, transitions in self.transitions.items():
            print(fromState)
            for toState, symbol in transitions:
                transitionsDict[('q' + str(fromState), symbol)
                                ] = {'q' + str(toState)}
        return transitionsDict

    def getStartState(self):
        return 'q' + self.startState

    def getFinalState(self):
        return 'q' + self.finalStates

    def print_info(self):
        print("States:", self.states)
        print("Alphabet:", self.alphabet)
        print("Transitions:")
        for fromState, transitions in self.transitions.items():
            for toState, symbol in transitions:
                print(f"{fromState} -> {toState} : {symbol}")
        print("Start State:", self.startState)
        print("Final States:", self.finalStates)


expression = "abb*"
afne = ConvertERToAFNe()
afne.convertRegex(expression)
afne.print_info()
print(afne.getTransitions())
