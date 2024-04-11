#bibloiotecas
import keyboard
from time import sleep
import os
from datetime import datetime

#Função que me da a hora e data da reclamação
def time() -> str:
    now: datetime = datetime.now()
    tempo = now.strftime("%d.%m.%y - %H:%M")
    return tempo

#Expressão lambda para limpar o console
clear = lambda: os.system('cls')

#Função que pausa o loop até que a tecla enter seja pressionada
def waitter() -> None:
    while True:
        if keyboard.is_pressed('b'):
            break

#Função que pega os inputs e os destina ao arquivo txt
def resistrador_reclamacao(cpf, reclamacao) -> str:
    try:
        with open("reclames.txt", "a") as file:
            file.write(f"{cpf}, {reclamacao}, {time()}\n")
    except FileNotFoundError:
        print("Arquivo não encontrado")

#Função que exibe a lista de reclamações
def leitor_reclamação() -> None:
    try:
        with open("reclames.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)
    except FileNotFoundError:
        print('|!| Arquivo não encontrado.')


#Função de menu que executa os comandos
def menu() -> None:
   var: str = 'menu'
   while True:
        clear()
        print(f"{var:_^23}")
        print("[1]Registrar reclamação")
        print("[2]Exibir reclamações")
        print("[0]Fechar")
        escolha = input("Opção: ")

        if escolha == "1":
            clear()
            cpf = input("Digite seu cpf: ")
            reclamacao = input("Digite sua Reclamação\n")
            sleep(1.5)
            print("Reclamação registrada...")
            resistrador_reclamacao(cpf, reclamacao)
        if escolha == "2":
            clear()
            leitor_reclamação()
            print("Pressione Enter para continuar...")
            waitter()
            
        elif escolha == "0":
            break
        else:
            print("Escolha invalida, Tente novamente!")

#chamada do programa
def main():
    #time()
    #waitter()
    #registrador_reclamacao()
    #leitor_reclamação()
    menu()