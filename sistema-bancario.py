

menu = '''
Bem vindos. Escolha a a opção abaixo:
1 - Saque
2 - Depósito
3 - Extrato
0 - Sair

Digite a opção desejada: '''


saldo_conta = 0
extrato = ""
numero_saques = 0
limite_diario = 500


while True:

    opcao = int(input(menu))

    if opcao == 1:
        print("\nBem vindo a opção SAQUE.\n")
        valor_saque = int(input("Digite o valor do saque e aperte ENTER: R$ "))
        if (saldo_conta > valor_saque) and (valor_saque <= limite_diario) and (numero_saques < 3):
            saldo_conta = saldo_conta - valor_saque
            numero_saques = numero_saques + 1 
            extrato = extrato + (f"Saque: R$ {valor_saque:.2f}\n".format(valor_saque))
            print (f"Saque de R$ {valor_saque:.2f} realizado com sucesso. Valor disponível em conta de R$ {saldo_conta:.2f}".format(valor_saque, saldo_conta))
        elif numero_saques >= 3:
            print ("Limite de saque diário excedido.")
        elif valor_saque >= limite_diario:
            print("Valor máximo diário de saque excedido. Revise o valor e refaça a operação.")
        elif valor_saque > saldo_conta:
            print(f"Valor do saque acima do disponível em conta. Valor disponível R${saldo_conta:.2f}".format(saldo_conta))


    elif opcao == 2:
        print ("\nBem vindo a opção de DEPÓSITO.\n")
        valor_deposito = int(input("Digite o valor do depósito e aperte ENTER: R$ "))
        if valor_deposito < 0:
            print("Valor mínimo para depósito de R$ 1.00")
        else:
            saldo_conta = saldo_conta + valor_deposito
            extrato = extrato + (f"Depósito: R$ {valor_deposito:.2f}\n".format(valor_deposito))
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso. Valor disponível em conta: R$ {saldo_conta:.2f}" .format(saldo_conta))

    elif opcao == 3:
        print("**********************************************")
        print ("\nBem vindo a opção de EXTRATO.\n")
        print(extrato)
        print(f"Saldo em conta: R$ {saldo_conta:.2f}".format(saldo_conta))
        print("**********************************************")

    elif opcao == 0:
        print("\nVocê saiu.\n")
        break

    else:
        print("Opção inválida.")
