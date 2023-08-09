# Função cria uma lista de estados que nao foram visitados para que estados repetidos nao sejam considerados,
# dai verifica se e existe uma transicao vazia e ela leva a um estado que nao estava no fechamento e assim o estado passa a estar no fechamento
def _closure(states, delta):
    S = set(states)
    notVisited = list(states)
    while len(notVisited) > 0:
        q = notVisited.pop()
        if (q, 'epsilon') in delta:
            new = delta[(q, 'epsilon')].difference(S)
            S.update(new)
            notVisited.extend(new)
    return S


class RecognitionAFNe():

    def __init__(self):
        self.message = "Recognizer AFNe"

    # Funcao serve para converte o conjunto de estados finais de um AFe para o conjunto de estados finais do AFN correspondente.
    # Para isso, apenas adicionamos ao nosso conjunto F todos os estados
    # que chegam a um estado final por meio de transicoes vazias
    def convertFeToFN(states, delta, F):
        notVisited = list(states)
        while len(notVisited) > 0:
            q = notVisited.pop()
            if (q, 'epsilon') in delta and F.intersection(_closure({q}, delta)):
                F.update({q})
        return F

    # Essa função converte as funções de transição de um Autômato Finito Determinístico (AFD) para o conjunto de funções de transição do Autômato Finito Não-Determinístico (AFND) correspondente.
    # Para fazer isso, itera-se por cada estado e tenta-se definir as transições desse estado para cada símbolo do alfabeto.
    # Para isso, busca-se todas as transições com o mesmo símbolo que partem do conjunto de estados alcançáveis pelo fechamento epsilon a partir do estado em questão.
    # Se essas transições existirem, cria-se a correspondente transição no formato (estado, símbolo): {conjunto de estados alcançados pelo fechamento epsilon através das transições encontradas}.
    def convertFeToFNDelta(states, delta, alphabet):
        newDelta = dict()
        for (state, symbol) in delta:
            if symbol != 'epsilon':
                newDelta.update({(state, symbol): delta[(state, symbol)]})

        for state in states:
            reachableSates = _closure({state}, delta)
            for symbol in alphabet:
                s = set()
                for achievableState in reachableSates:
                    if (achievableState, symbol) in delta:
                        x = _closure(delta[(achievableState, symbol)], delta)
                        s.update(x)
                        s.update(delta[(achievableState, symbol)])
                if len(s) > 0:
                    newDelta.update({(state, symbol): s})

        return newDelta

    # Essa função avalia se uma cadeia é aceita ou não por um Autômato Finito Determinístico (AFD) ou Não-Determinístico (AFND).
    def AFe(Q, sigma, delta, q0, F, chainOfCharacters):
        activeStates = _closure({q0}, delta)
        for symbol in chainOfCharacters:
            new = set()
            for q in activeStates:
                if (q, symbol) in delta:
                    new.update(_closure(delta[(q, symbol)], delta))
            activeStates = new
        return len(activeStates.intersection(F)) != 0
