# Classe que representa o automato generico
class AFNe:

    # Inicializadores da classe
    def __init__(self, language=set(['a', 'b'])):
        self.states = set()
        self.startState = None
        self.finalStates = []
        self.transitions = dict()
        self.language = language

    def setStartState(self, state):
        self.startState = state
        self.states.add(state)

    def addFinalStates(self, state):
        if isinstance(state, int):
            state = [state]
        for s in state:
            if s not in self.finalStates:
                self.finalStates.append(s)

    def addTransition(self, fromState, toState, symbol):
        if isinstance(symbol, str):
            symbol = set([symbol])
        self.states.add(fromState)
        self.states.add(toState)
        if fromState in self.transitions:
            if toState in self.transitions[fromState]:
                self.transitions[fromState][toState] = self.transitions[fromState][toState].union(symbol)
            else:
                self.transitions[fromState][toState] = symbol
        else:
            self.transitions[fromState] = {toState : symbol}

    def addTransitionDict(self, transitions):
        for fromState, toStates in transitions.items():
            for state in toStates:
                self.addTransition(fromState, state, toStates[state])

    def getTransitions(self, state, key):
        if isinstance(state, int):
            state = [state]
        trstates = set()
        for st in state:
            if st in self.transitions:
                for tns in self.transitions[st]:
                    if key in self.transitions[st][tns]:
                        trstates.add(tns)
        return trstates

    def display(self):
        print("language: {" + ", ".join(self.language) + "}\n")
        print("states:", self.states)
        print("start state: ", self.startState)
        print("final states:", self.finalStates)
        print("transitions:")
        for fromState, toStates in self.transitions.items():
            for state in toStates:
                for char in toStates[state]:
                    print("  ", fromState ,"->", state, "on '"+char+"'")

    def newBuildFromNumber(self, startNum):
        translations = {}
        for i in list(self.states):
            translations[i] = startNum
            startNum += 1
        rebuild = AFNe(self.language)
        rebuild.setStartState(translations[self.startState])
        rebuild.addFinalStates(translations[self.finalStates[0]])
        for fromState, toStates in self.transitions.items():
            for state in toStates:
                rebuild.addTransition(translations[fromState], translations[state], toStates[state])
        return [rebuild, startNum]



class AFNeStruct:

    @staticmethod
    def basicStruct(symbol):
        state1 = 1
        state2 = 2
        basic = AFNe()
        basic.setStartState(state1)
        basic.addFinalStates(state2)
        basic.addTransition(1, 2, symbol)
        return basic

    @staticmethod
    def plusStruct(a, b):
        [a, m1] = a.newBuildFromNumber(2)
        [b, m2] = b.newBuildFromNumber(m1)
        state1 = 1
        state2 = m2
        plus = AFNe()
        plus.setStartState(state1)
        plus.addFinalStates(state2)
        plus.addTransition(plus.startState, a.startState, "epsilon")
        plus.addTransition(plus.startState, b.startState, "epsilon")
        plus.addTransition(a.finalStates[0], plus.finalStates[0], "epsilon")
        plus.addTransition(b.finalStates[0], plus.finalStates[0], "epsilon")
        plus.addTransitionDict(a.transitions)
        plus.addTransitionDict(b.transitions)
        return plus

    @staticmethod
    def dotStruct(a, b):
        [a, m1] = a.newBuildFromNumber(1)
        [b, m2] = b.newBuildFromNumber(m1)
        state1 = 1
        state2 = m2-1
        dot = AFNe()
        dot.setStartState(state1)
        dot.addFinalStates(state2)
        dot.addTransition(a.finalStates[0], b.startState, "epsilon")
        dot.addTransitionDict(a.transitions)
        dot.addTransitionDict(b.transitions)
        return dot

    @staticmethod
    def starStruct(a):
        [a, m1] = a.newBuildFromNumber(2)
        state1 = 1
        state2 = m1
        star = AFNe()
        star.setStartState(state1)
        star.addFinalStates(state2)
        star.addTransition(star.startState, a.startState, "epsilon")
        star.addTransition(star.startState, star.finalStates[0], "epsilon")
        star.addTransition(a.finalStates[0], star.finalStates[0], "epsilon")
        star.addTransition(a.finalStates[0], a.startState, "epsilon")
        star.addTransitionDict(a.transitions)
        return star