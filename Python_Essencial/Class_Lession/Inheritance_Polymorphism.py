class Animal:
    def __init__(self,nome,peso):
        self.nome = str(nome)
        self.peso = float(peso)

    def __str__(self):
        return f'Nome: {self.nome} \nPeso: {self.peso}'
    

class Mamifero(Animal):
    tipo = str('Mamifero')
    
    #Uma classe pode ser herdeira de outra classe e isto é indicado nos paratenses da classe, ou seja, a class Mamifero(Animal) é uma classe herdeira da classe animal.
    #O que siginifica heranca e para que ela serve? Quando uma classe é herdeira de outra, ela recebe todos os atributos e metodos (incluido o def __init__) da classe mãe
    #+ seus proprios atributos e metodos.

    #Classes filhas podem ser herdeiras de mais de uma classe


    def __str__(self):
        return super().__str__() + '\nMamifero\n'
    #Classes filhas podem sobescrever metodos e atributos da classe mae, modificando assim seu funcionamento na classe filha.

    #Outra coisa importante sobre heranca mostrada neste metodo é a palavra super, que basicamente a palavra usada para se referir as classes mae da classe filha.
    #O super pode ser utilizado pode estar associado tanta a atributos, quanto a metodos, um otimo exemplo é a sobescricao do metodo __str__, onde ele esta retornando
    #uma concatenacao entre o metodo __str__ da classe + a palavra Mamifero, mas basicamente é isso, o super serve para se referir a classe mae.

class Anfibio(Animal):
    tipo = str('Anfibio')

    def __str__(self):
        return super().__str__() + '\nAnfíbios\n'

########################################################################################################################################################################
class Zoo:
    acervo = []

    def add(self,animal):
        self.acervo.append(animal)

    def imprimir(self):
        print('Animais do Zoo: ')

        for animal in self.acervo:
            print(animal)

gorila = Mamifero('Gorila Albino', 160)
sapo = Anfibio('Sapo Cururu', 0.02)


bichos = Zoo()
bichos.add(gorila)
bichos.add(sapo)

bichos.imprimir()

#O que está acontecendo aqui é um polimorfismo, que basicamente é o seguinte: Originalmente a class Zoo servia para guardar animais da classe Animal e tinha um método
#que printava os atributos destes animais que foram guardados na class Zoo. Como a classe Mamífero e a classe Anfíbio são filhos da classe Animal, elas são interpretados
#como membros da Classe Animal pela Classe Zoo e podem ser utilizadas nos métodos da classe Zoo, sem ter o sentido dos métodos alterados.

#Polimorfismo basicamente é oq permite as classes filhas serem utilizadas e interpretadas como se fossem a classe mãe.