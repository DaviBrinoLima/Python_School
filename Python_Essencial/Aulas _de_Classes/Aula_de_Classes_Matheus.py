class Pessoa:
    age_diff = 18

    def __init__(self,nome, age):
        self.__nome = nome
        self.__age = age
    
    @property
    def nome(self):
        return  self.__nome.split(' ')[0] if self.__nome.count(' ') else self.__nome
    
    @nome.setter
    def nome(self,nnome):
        self.__nome = nnome

    @property
    def age(self):
        return self.__age
    
    def teste(self):
        if self.__nome.endswith('Davi Brino'):
            self.__nome = 'Zebu'

    def teste2(self):
        return self.__nome, self.nome

class Pessoa2:
    age = 18

    @classmethod
    def age_diff(cls, age):
        return age - cls.age
     
if __name__=='__main__':
    davi = Pessoa('Davi Brino', 19)
    # matheus = Pessoa('Matheus', 28)
    print(davi.nome)
    # davi.teste()
    print(davi.teste2())
    # print(davi.nome)
    davi.nome = 'muito zebu'
    print(davi.teste2())
    # print(davi.nome)
    # print(matheus.age)
    #print(Pessoa2.age_diff(matheus.age))