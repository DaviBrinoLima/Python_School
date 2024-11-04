class Inseto:
    def __init__(self,nome,venonoso):
        self.__nome = str(nome)
        self.__venom = bool(venonoso)


    #Explicando os métodos getter, setter e deleter e property
    
    
    #Os métodos getter, setter e deleter normalmente são utilizados para manipular e alterar atributos fechados de uma classe estando fora dela.

    #Eles podem estar associados a um atríbuto ou a uma propriedade. Se associado a um propriedade devem ser escritos como @propriedade.setter, 
    # @propriedade.getter ou @propriedade.deleter, mostrando assim que estão associados a uma determinada propriedade


    @property
    def nome(self):
        return self.__nome
    #@property é uma forma de transformar um método em uma propriedade, que basicamente é um atributo que é calculado dinamicamente ao invés de ser só armazenado. 
    # Uma propriedade é acessada como atributo, mas é executado como método.


    @nome.setter
    def nome(self, new_name):
        self.__nome = new_name
    #O setter é o método que define oq será feito ao modificar um atributo de um obeto
    #Para chamar o setter de uma propriedade é só fazer: obj.propriedade = 



    @nome.getter
    def nome(self):
        return self.__nome
    #O getter é o método acessor, serve para acessar um atributo do objeto
    #Para chamar o getter de uma propriedade é só fazer: obj.propriedade 


    @nome.deleter
    def nome(self):
        del self.__nome
    #O deleter é o método deletor, serve para deletar um atributo de um objeto
    # Para chamar o deleter de uma propriedade é só fazer: del obj.propriedade


#############################################################################################################################################################################
    #Para os métodos getter, setter e deleter estarem associados a um atributo e não a uma propriedade eles devem ser declarados como métodos da classe.

    #Ex:
    def set_nome(self,novo_nome):
        self.__nome = novo_nome

    #Chamando: self.set_nome(novo_nome) -> Método set_nome associado ao atributo __nome


    #O uso das propriedades (@property) torna o código mais limpo e claro, pois evita a criação de várips método set_atributo,get_atributo,del_atributo, 
    # tornando o código mais limpo e claro. Quando os métodos estão associados a uma propriedade, a declaração do set, get ou del se torna mais claro e
    #o chamamento se torna mais simples e prático.


##############################################################################################################################################################################

           