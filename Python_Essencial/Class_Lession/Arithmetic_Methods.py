class Plantas:
    def __init__(self,nome,tipo,peso):
        self.nome = str(nome)
        self.tipo = str(tipo)
        self.peso = float(peso)

    #Os Métodos aritméticos servem para definir o que será feito quando objetos da classe forem operados. Igualmente dos métodos Built-in, eles podem ser
    #definidos na classe ou serem chamados como método do objeto, mas o mais recomendado é definir eles na classes, pois torna sua utilização mais prática.


    #Outra vantagem de definir um método aritmético na classe é poder alterar seu funcionamento, pois assim você garante a operação feita quando dois ou mais
    #obj forem somados, multiplicados ou afins.


    #Exemplificando a definição do método __add__, método da soma "+":

    def __add__(self,other):
        return Plantas(self.nome + ',' + other.nome, self.tipo + "," + other.tipo, self.peso + other.peso)
    #Basicamente agora quando for feito obj_1 + obj_2 será gerado um novo objeto_3 que é a soma dos atributos do obj_1 e do obj_2


    #Como são muitos métodos, vou citar os mais importantes e seus operadores correspondentes. Não vale a pena definir cada um deles, pois cada método terá uma
    #definição específica para o código em questão.


    #Citando os outros métodos:
    

    #def __mod__(self,other) ---> obj_1 % obj_2
    #def __mul__(self,other) ---> obj_1 * obj_2
    #def __neg__(self) ---> not obj_1
    #def __pow__(self,other) ---> obj_1 ** obj_2
    #def __sub__(self,other) ---> obj_1 - obj_2
    #def __truediv__(self,other) ---> obj_1 / obj_2
    #def __floordiv__(self,other) ---> obj_1 // obj_2

    
    #Obs importante: Quando utilizamos os métodos operatórios, basicamente quando fazemos obj_1 (operador) obj_2, estamos fazendo obj_1.__operador__(obj_2)
    #Usando de exemplo o __add__:

    #Se fazemos A + B, neste caso estamos chamando A.__add__(B), se fazemos B + A, estamos chamando B.__add__(A). SIM ISTO TEM DIFERENÇA, É SÓ ANALISAR
    #MATEMATICAMENTE.

    #Detalhe importante: se a classe de A não tiver o método __add__definido, então será chamado B.__iadd__(A). O i indica que A+B está sendo chamado pelo
    #operador da direita (B) e não pelo da esquerda (A).

    #Analisando o detalhe importante, chegamos a uma conclusão importante, o obj A e o obj B podem ser de classes diferentes, o que é importa é um dos obj
    #terem em suas classes o métodos __add__ definidos, importanndo obviamente em qual deles está definido o método.
