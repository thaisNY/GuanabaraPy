# verificar se expressão de parentes está correta.Deve verificar se os parenteses foram abertos fechados e na ordem correta
expr = str(input('Digite uma expressão :'))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')' :
        if len(pilha) > 0 :
            pilha.pop()
        else :
            pilha.append(')')
            break
if len(pilha) == 0 :
    print('Sua expressão está valida')
else :
    print('Sua expressão está errada')
