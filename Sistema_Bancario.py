menu = """

(1)Depositar
(2)Sacar
(3)Extrato
(0)Sair 

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor a ser depositado:"))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso.")
        else:
            print("Operação falhou! O Valor informado é inválido.")    
        
        
    elif opcao == "2":
        if LIMITE_SAQUE > 0:
            valor = float(input("Informe o valor a ser sacado:"))

            if valor > saldo:
                print("Saldo Insuficiente.")
            else:
                if valor > 0 and valor <= limite:
                    saldo -= valor
                    LIMITE_SAQUE -= 1
                    extrato += f"Saque R$ {valor:.2f}\n"
                    print("Saque realizado com sucesso.")
                else:
                    print("Valor de saque inválido.")  
        else:
            print("Limite de saque excedido.")
        
    elif opcao == "3":
        if extrato == "":
            print("Não foram realizados movimentações.")
        else:
            print (extrato)
            print (f"Saldo atual: R$ {saldo:.2f}")    
    
    elif opcao == "0":
        break            

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")