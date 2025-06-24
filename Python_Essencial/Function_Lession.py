def cont(*num):
    for i in num:
        print(i)

#Desenpacotamento de funções


#########################################################################################################################################
def function(lista :list):
    for i in lista:
        print(i)

#Paramétros de funções podem ser: str, int, float e também variáveis compostas


##########################################################################################################################################
def contador(i,f,p):
    """
    --> Faz uma contagem e mostra na tela
    parameter i: Início da contagem (O início está incluso)
    parameter f: Fim da contagem (O fim está incluso)
    parameter p: step da contagem
    """

    #Isto é um docstring, que basicamente é a documentação / help de uma função. Funções nativas do python já possuem sua própria docstring,
    #mas funções criadas por terceiros não possuem uma docstring, então caso queira criar uma documentação para sua função, é assim que se faz.


    while i <= f:
        print(f'{i}', end='..')
        i += p
    print('FIM!')


##########################################################################################################################################
def somar(a,b,c = 0):
    print(f'A soma é{a+b+c}')

#Funções podem ter parâmetros opcionais, ou seja, podem ter parametros que não precisam ser passados, pois já possuem um valor associado a eles.
#Parâmetros opcionais caso recebam um valor no seu chamamento, recebem o valor definido no chamamento, caso não recebam nada no chamamento, utilizam
# o valor já associado a eles.


##########################################################################################################################################
if __name__ == '__main__':
    cont(5,4,3,2,1)


    a = [5,4,3,2,1]
    function(a)


# OBS IMPORTANTE: Variáveis declaradas dentro da função {variáveis locais}, só funcionam dentro da função, não podem ser usadas fora da função.


#Variáveis declaradas fora da função {variáveis globais}, podem ser usadas e chamadas dentro da função, porém para serem alteradas dentro de uma função
#devem ser declaradas na função como: global {varíavel}. 


#OBS IMPORTANTE: Imports de bibliotecas podem ser locais e globais, vou pode importar uma biblioteca globamente no script ou importar uma biblioteca
#dentro de uma função e chamar junto e somente com sua função.


#OBS IMPORTANTE: Passar uma variável como paramêtro de uma função, não altera o valor da variável quando o paramêtro for operado, eles são independentes.
