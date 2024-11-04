class Quadrado:
    lado = 0 #A classe pode seus atributos criados linha a linha com valores pré definidos.

    def area(self):
        return self.lado**2
    

class triangulo:
    def __init__(self,base,altura): #Ou podem ter seus atríbutos criados a partir de uma função construtura, que não possue valores pré definidos e que
        #precisam ser declarados quando o obj é instanciado.
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura)/ 2
    

q1 = Quadrado
q1.lado = 20


tri_1 = triangulo(5,8) #Se no construtor da classe tiver dois ou mais argumentos, a quantidade correta de argumentos devem ser passadas
#quando o objeto for declarado.


# print(tri_1.area())
# print(q1.lado)


##############################################################################################################################################
class Animal:
    def __init__(self,nome,peso):
        self.nome = str(nome)
        self.peso = float(peso)

    def mostra(self):
        print(f'Nome: {self.nome}')
        print(f'Peso: {self.peso}')
        
    def engordar(self,comida):
        self.peso += comida
        return self.peso
    
    def __str__(self):
        return f'Nome: {self.nome} \n Peso: {self.peso}'
    #Ao invés de criar 
    

class Zoo:
    acervo = []

    def add(self,animal):
        self.acervo.append(animal)

    def mostra(self):
        print('Animais do Zoo: ')

        for animal in self.acervo:
            animal.mostra() #Como meu atríbuto acervo é uma lista que está recebendo objetos da classe Animal, os elementos desta lista 
            # são objetos da classe Animal ou seja, as funções e atributos da classe Animal funcionam nos elementos da lista acerva, ou seja, 
            # esse método mostra citado no for, se refere ao método mostra da classe Animal, pois como os elementos da lista são da classe animal, 
            # eles só podem utilizar métodos e atrítubos da classe Animal.
    

gorila = Animal('Gorila', 300)
# macaco = Animal('Macaco', 80)


# aux = Zoo()
# aux.add(gorila)
# aux.add(macaco)


# aux.mostra()
print (gorila)


#############################################################################################################################################################
class Private:
    def __init__(self, public,protect,private):
        self.public = public #Atributo Público = Pode ser acessado e alterado de fora da classe
        self._protect = protect #Atributo Protegido = Pode ser acessado e alterado de fora da classe, mas está mais escondido e indica que está
        #envolvido em algo importante para o funcionamento da classe.
        self.__private = private #Atributo Privado = Não pode ser acessado e alterado de fora da classe (Em tese). Normalmente está oculto pq
        #envolve algo importante para o funcionamento da classe (Afinal se não envolvesse não faria sentido estar privado).


exemplo = Private(3,4,5) 

print("exemplo.__private") #Está printado para não quebrar o código.
#Se vc tentar acessar um atributo privado de fora da classe você obterá erro de atributo inexistente.


exemplo._Private__private = 15 #Para se acessar ou alterar um atributo privado de fora da classe se faz da seguinte forma --> self._class__private


exemplo.__private = 10 
print(exemplo.__private)
print(exemplo._Private__private)
print(dir (exemplo)) 
#Se vc tentar alterar um atributo privado de fora da classe da seguinte forma ---> self.__private = 3 (Vc estará criando um novo atributo
#para sua classe, que tera nome "__private", enquanto o original e verdadeiro se chama self.__private)


