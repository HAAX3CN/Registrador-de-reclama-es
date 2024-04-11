import pickle
class Manager_acc:
        

    def write_file(conta):
        conta = open()

#Classe que comporta as contas do usuario e seus metodos
class Conta(Manager_acc):

    def __init__(self, nome, email, senha):  #Instancia que inicia as variaveis
        self.nome = nome
        self.email = email
        self.senha = senha

    #getters e setters
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email

    @property    
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        self.__senha = senha
    
    def adicionar_conta(self, nome, email, senha):
        conta = {'nome': nome, 'email': email, 'senha': senha}
        return conta
