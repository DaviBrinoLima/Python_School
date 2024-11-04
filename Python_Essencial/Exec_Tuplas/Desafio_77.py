palavras = ('arroz','sorvete','frango','batata','tomate','cenoura','abacate')


for i in palavras:
    print(f'\n Na palavra {i} temos as vogais ', end='')

    for letra in i:
        if letra in 'aeiou':
            print(letra, end=' ')