express = input('Digite a expressão: ')
verific = []


for i in express:
    if i == '(':
        verific.append('(')

    elif i == ')':
        if len(verific) > 0:
            verific.pop()

        else:
            print('A expressão está errada')
            break


if len(verific) == 0:
    print('A expressão está válida')

else: 
    print('A expressão está errada')
        
