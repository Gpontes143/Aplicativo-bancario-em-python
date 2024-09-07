from time import sleep
import os


escolha = 0
dinheiro_total = 0
saques_diarios = 0
ciclo_deposito = 0
ciclo_saque = 0
lista_deposito = []
lista_saque = []

def limpar_terminal():
    # Se estiver no Windows
    if os.name == 'nt':
        os.system('cls')
    # Se estiver no Linux ou macOS
    else:
        os.system('clear')


def soma(numero1,numero2):  # sourcery skip: inline-immediately-returned-variable
    
    return numero1 + numero2

def subtracao(numero1,numero2): 
    return numero1 - numero2
#começando a operação deposito

def deposito():
    global dinheiro_total
    global ciclo_deposito

    
    valor_para_depositar = float(input("Digite um valor para depositar\n\nDigite um 0 para cancelar a operação\n\n:"))

    if (valor_para_depositar == 0):
        voltando_para_aplicativo("\nCancelando a operação.... \n", 2)
    else:
        dinheiro_total = soma(dinheiro_total , valor_para_depositar)
        print(f"\nDepositando ${valor_para_depositar}\n\nSeu saldo atual é ${dinheiro_total}")
        lista_deposito.append(f"${valor_para_depositar:.2f}")
        ciclo_deposito +=1
        sleep(3)

        voltando_para_aplicativo("Voltando para o menu...", 1)
        return dinheiro_total, valor_para_depositar



def voltando_para_aplicativo(arg0, arg1):
    print(arg0)

    sleep(arg1)

    limpar_terminal()

    sleep(0.5)

    aplicativo() 
        
        
        

#inciando saque
def saque():
    global dinheiro_total
    global saques_diarios
    global ciclo_saque
    max_saque = 500
    if saques_diarios >= 3:
        print("Você chegou no seu limite diario\n\n")
        voltando_para_aplicativo("voltando para o menu....",1)
   
    
    else:
        saque_escolhido = int(input("\nQuanto deseja sacar?\n"))
        if saque_escolhido > max_saque:
            print("O limite do saque é 500")
            saque()
        else:
            if saque_escolhido < (dinheiro_total):
                dinheiro_total = subtracao(dinheiro_total,saque_escolhido)
                lista_saque.append(f"${saque_escolhido:.2f}")
                ciclo_saque +=1
                saques_diarios +=1
                print(f"\nSacando ${saque_escolhido}\n\nSeu total é ${dinheiro_total}")
                sleep(3)

                voltando_para_aplicativo("voltando para o menu....",1)
            else:
                print("\nVocê não tem o valor necessario para realizar o saque\n")
                voltando_para_aplicativo("voltando para o menu....",1)
    
    
    return dinheiro_total


#iniciando extrato
def extrato():
    global lista_deposito
    global lista_saque
    global ciclo_deposito
    global ciclo_saque
    
    if ciclo_deposito or ciclo_saque > 0:
        
        print(f"\nVocê realizou {ciclo_deposito} depositos, \nos valores de cada depositos estão aqui{lista_deposito}")
        
        print(f"\nVocê realizou {ciclo_saque} saques \nos valores de cada saque estão aqui{lista_saque}")
        
        print(f"\nSeu Saldo atual é {dinheiro_total}")
        
        voltando_para_aplicativo("voltando para o menu....",5)
    else:
        print(f"\nVocê não realizou nenhum processo\n")
        
        voltando_para_aplicativo("voltando para o menu....",1)

#interface do sistema
def interface():
    
    
    global escolha
    
    menu = print(
    """ 

    ---------Menu----------             

    1-Deposito
    2-Saque
    3-Extrato
    4-Sair      

    v = 0.1             
    -----------------------             
    """)
    
    
    while menu != 4:
        menu = int(input(":"))

        #Checando as escolhas
        
        if menu == 1:
            print("Mudando para o deposito...\n")
            sleep(1)
            escolha = 1
            break
        
        elif menu == 2:
            print("Mudando para o saque...")
            sleep(1)
            escolha = 2
            break        
        elif menu == 3:
            print("Mudando para o Extrato....")
            sleep(1)
            escolha = 3
            break
                
        elif menu == 4:
            print("Saindo....")
            
        else:
            print("desconhecido")
    return escolha


#Sistema do aplicativo 
def aplicativo():
    interface()

    global escolha
    if escolha == 1:
        deposito()
    elif escolha == 2:
        saque()
    elif escolha == 3:
        extrato()
    else:
        print("Opção não reconhecida")
        



aplicativo()