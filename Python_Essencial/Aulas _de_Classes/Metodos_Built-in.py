class Animal:
    def __init__(self,nome,peso,oculto):
        self.nome = str(nome)
        self.peso = float(peso)
        self.__oculto =  bool(oculto)
    

    ##Em python possuimos algumas funções chamadas de Built-in, que são funções nativas e integradas a linguagem. Essas funções podem ser utilzadas em objetos
    #de uma classe ou podem ter seu funcionamento modificado se definadas em uma determinada classe.

    #Para usar uma função Built-in em obj da classe basta fazer: "obj.__funcao__(self)"


    #Para exemplificar a modificação de uma função deste tipo, usei usar de exemplo a função __str__. Existem várias outras funções, mas vou exemplifciar somente
    #uma delas, pois é muita perda de tempo exemplificar todos, é só olhar na net se tiver dúvida.


    def mostra(self):
        print(f'Nome: {self.nome}')
        print(f'Peso: {self.peso}')
    #Para printar os atributos de um objeto, normalmente é criado um método que realiza os print dos atributos ao ser chamado pelo obj.

    def __str__(self):
        return f'Nome: {self.nome} \n Peso: {self.peso}'
    #Uma forma mais eficiente de realizar estes prints é utilizar o método __str__, que é o método do print.
    #Ele basicamente é acionado quando no código o obj é chamado como uma str: "str(obj)".


    #O método __str__ é muito usado para printar os atributos de um obj, pois quando a função print é chamada, ela basicamente faz:
    #print(str(obj)), chamando assim o método __str__.
    
    
    #Definir as funções Built-in dentro da classe serve para facilitar o chamamento das mesmas, pois se a função __str__ não estivesse definida na classe, teria que ser
    #chamada como "obj.__str__(self)", mas como a função __str__ foi definida nesta classe, basta fazer str(obj) que a função é chamada.


    #As outros funções possuem funcionamento muito semelhante ao __str__, elas são chamadas por: obj.__funcao__(), literalmente igual ao __str__. Do mesmo modo, se definidas
    #dentro da classe, as funções são chamadas por: funcao(obj)


    #Citando as funções / métodos:


    #def __round__(self,[ndigits]) ou obj.__round__(self,[ndigits])
    #def __len__(self) ou obj.__len__(self)
    #def __trunc__(self) ou obj.__trunc__(self)
    #def __floor__(self) ou obj.__floor__(self)
    #def __ceil__(self) ou obj.__ceil__(self)
    #def __complex__(self) ou obj.__complex__(self)
    #def __int__(self) ou obj.__int__(self)
    #def __float__(self) ou obj.__float(self)

gorila = Animal('Gorila', 500)
