from project import RecognitionAFNe as recognizer
from project import ConvertERToAFNe as converter

conveObj = converter.ConvertERToAFNe()
recogObj = recognizer.RecognitionAFNe()

expReg = input('Entre com sua expressão regular: ')
conveObj.convertRegex(str(expReg))
print('O autômato gerado tem os seguintes dados: ')
conveObj.printInfo()

recogWord = input("Entre com a cadeia de caracteres: ")

verification = recogObj.VerificationAFe(conveObj.getStates(), conveObj.getAlphabet(), conveObj.getTransitions(), conveObj.getStartState(), conveObj.getFinalState(), recogWord)

print('Palavra é aceita') if verification else print('Palavra não é aceita')



