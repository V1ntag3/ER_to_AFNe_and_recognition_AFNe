from project import RecognitionAFNe as recognizer


# exemplo de reconhecimento de cadeia para uma linguagem em que o antipenúltimo elemento == 1
delta = {('q1', '0'): {'q1'}, ('q1', '1'): {'q1', 'q2'}, ('q2', '0'): {'q3'}, ('q2', '1'): {'q3'},
         ('q3', '0'): {'q4'}, ('q3', '1'): {'q4'}}

# Usando a cadeia '01001010101101011001001000', o resultado deve ser false pois o antepenultimo
# numero e '0'
print("reconhecimento  para um automato que reconhece cadeias com antepenultimo elemento igual a 1")
print("cadeia 01001010101101011001001000", recognizer.RecognitionAFNe.AFe(
    ['q1', 'q2', 'q3', 'q4'], ['0', '1'], delta, 'q1', {'q4'}, '01001010101101011001001000'))


# exemplo de reconhecimento de cadeia para uma linguagem do tipo a^x b^y a^z, em que x,y,z >= 0
delta = {('q0', 'a'): {'q0'}, ('q0', 'epsilon'): {'q1'},  ('q1', 'b'): {'q1'}, ('q1', 'epsilon'): {'q2'},
         ('q2', 'a'): {'q2'}, ('q2', 'epsilon'): {'q3'}}

print("reconhecimento de cadeia para uma linguagem do tipo a^x b^y a^z, em que x,y,z >= 0")
print("cadeia bbbbbb", recognizer.RecognitionAFNe.AFe(
    ['q0', 'q1', 'q2'], ['a', 'b'], delta, 'q0', {'q2'}, 'bbbbbb'))
print("cadeia abbaa", recognizer.RecognitionAFNe.AFe(
    ['q0', 'q1', 'q2'], ['a', 'b'], delta, 'q0', {'q2'}, 'abbaa'))
print("cadeia bbaab", recognizer.RecognitionAFNe.AFe(
    ['q0', 'q1', 'q2'], ['a', 'b'], delta, 'q0', {'q2'}, 'bbaab'))
print("cadeia vazia", recognizer.RecognitionAFNe.AFe(
    ['q0', 'q1', 'q2'], ['a', 'b'], delta, 'q0', {'q2'}, ''))


# Convertendo as funcoes de transicao de um AFe para um AFN
print("Convertendo as funcoes de transicao de um AFe para um AFN")
delta = {('q0', 'a'): {'q0'}, ('q0', 'epsilon'): {'q1'}, ('q1', 'b'): {'q1'}, ('q1', 'epsilon'): {'q2'},
         ('q2', 'a'): {'q2'}}
F = {'q2'}
print(delta)
print("delta convertido:")
print(recognizer.RecognitionAFNe.convertFeToFNDelta(
    ['q0', 'q1', 'q2'], delta, ['a', 'b']))
print("conjunto final do AFe:", F)
print("conjunto de estados finais do AFN correspondente:",
      recognizer.RecognitionAFNe.convertFeToFN(['q0', 'q1', 'q2'], delta, F))


# AFe(Q, sigma, delta, q0, F, cadeia):
# Agora abrimos espaco para o usuario criar e testar seus AFE/AFN(s)...
print("===============================================================")
op = "1"
while op == "1":
    print("Entre com um AFE, depois, voce podera converte-lo em um AFN ou testar o reconhecimento de",
          "alguma cadeia")
    s = input("Entre com o conjunto de estados(Q) do AFE, ex: q1,q2,q3,q4 ")
    Q = s.split(",")

    s = input(
        "Entre com o conjunto de simbolos do alfabeto(Sigma) do AFE, ex: a,b,c ")
    sigma = s.split(",")

    # delta = input("Entre com as funcoes de transicao(delta) do AFE")
    print("Agora entre com as regras de transicao do AFe, uma a uma")
    op2 = "1"
    delta = dict()
    while op2 == "1":
        print("Entre com a parte esquerda de uma regra de transicao, no formato: estado,simbolo lido")
        print("exemplo: q1,a ")
        s = input()
        simbolo, estado = s.split(",")

        print("Entre com a parte direita de uma regra de transicao, no formato: conjunto de estados alcancados")
        print("exemplo: q2,q3,q4,q5 ")
        s = input()
        direita_transicao = set()
        for x in s.split(","):
            direita_transicao.add(x)
        delta.update({(simbolo, estado): direita_transicao})
        op2 = input(
            "digite 1 para entrar com mais uma regra de transicao, digite 0 para finalizar as regras ")

    print(delta)

    q0 = input("Entre com o estado inicial do AFE, ex: q0 ")

    s = input("Entre com o conjunto de estados finais(F) do AFE, ex: q3,q4 ")
    x = s.split(",")
    F = set()
    for elemento in x:
        F.add(elemento)

    processa_cadeias = "1"
    while processa_cadeias == "1":
        cadeia = input("Entre com a cadeia a ser processada, ex: 10101010 ")
        if (recognizer.RecognitionAFNe.AFe(Q, sigma, delta, q0, F, cadeia)):
            print("A cadeia", cadeia, "foi reconhecida")
        else:
            print("A cadeia", cadeia, " nao foi reconhecida")
        processa_cadeias = input(
            "Digite 1 para continuar testando mais cadeias, ao contrario, digite zero ")

    op3 = input("Digite 1 para converter o AFe em AFN, ao contrario, digite 0 ")
    if op3 == "1":
        novoDelta = recognizer.RecognitionAFNe.convertFeToFNDelta(
            Q, delta, sigma)
        novoF = recognizer.RecognitionAFNe.convertFeToFN(Q, delta, F)
        print("Funcoes de transicao do AFN: ", novoDelta)
        print("Conjunto de estados finais do AFN: ", novoF)
        op4 = "1"
        while op4 == "1":
            op4 = input(
                "Digite 1 para testar uma cadeia no novo AFN, digite 0 ao contrario ")
            if op4 == "1":
                cadeia = input("Entre com uma cadeia valida ")
                if (recognizer.RecognitionAFNe.AFe(Q, sigma, novoDelta, q0, novoF, cadeia)):
                    print("A cadeia", cadeia, "foi reconhecida")
                else:
                    print("A cadeia", cadeia, " nao foi reconhecida")

    op = input(
        "Digite 0 para finalizar o programa, Digite 1 para entrar com outro AFe ")
