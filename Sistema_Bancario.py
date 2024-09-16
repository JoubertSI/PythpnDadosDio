menu = """

(0)Depositar
(1)Sacar
(2)Extratp
(3)Sair 

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "0":
        valor = float(input("Informe o valor a ser depositado:"))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O Valor informado é inválido.")    
        
        
    elif opcao == "1":
        print("Saque")
        
    elif opcao == "2":
        print("extrato")
    
    elif opcao == "3":
        break            

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        
        
        print(saldo)