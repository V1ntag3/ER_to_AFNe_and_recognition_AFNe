from project.AFNe.RecognitionAFNe import RecognitionAFNe
from automataLib.fa.nfa import NFA

recogObj = RecognitionAFNe()

# Reconhece +, e *
expReg = input('Entre com sua expressão regular: ')
expReg = expReg.replace('+', '|')

print(expReg)
symbols = []
for item in expReg:
    teste = item in symbols 
    if item != '|' and item != '*' and item != '()' and item != ')' and teste == False:
        symbols.append(item)
    

nfa = NFA.from_regex(expReg, input_symbols=set(symbols))
print(nfa)

# conveObj.convertRegex(str(expReg))



print('O autômato gerado tem os seguintes dados: ')

separator = ', '
separator2 = 'q'

states = []
for item in nfa.states:
    states.append('q' + str(item)) 
inicialState = 'q' + str(nfa.initial_state)
finalStates = []
for item in nfa.final_states:
    finalStates.append('q' + str(item)) 
for item in nfa.transitions:
    print(item)
print('Alfabeto: ' + str(list(nfa.input_symbols)))
print('Estados: ' + str(states))
print('Estado Inicial: ' + inicialState)
print('Estado Final: ' + str(finalStates))
print('Trasições: ')
transicoes = {}
for item in nfa.transitions:
    print('q' + str(item) + ':', end='') 
    
    for item2 in nfa.transitions[item]:
        
        print(item2, end='') if item2 != '' else print('epsilon', end='')
        
        print(' --> ' + str(set(nfa.transitions[item][item2])))
        
        transicoes[(item, item2)] = set(nfa.transitions[item][item2])       
print('\n')

recogWord = input("Entre com a cadeia de caracteres: ")
print('\n')

verification = RecognitionAFNe.VerificationAFe(list(nfa.states), symbols, transicoes, nfa.initial_state, nfa.final_states, recogWord)

print('Palavra é aceita') if verification else print('Palavra não é aceita')



