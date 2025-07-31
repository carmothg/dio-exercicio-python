saldo=0.00
LIMITE_VALOR_SAQUE=500
LIMITE_DIARIO=3
qtd_saques_realizados=0
extrato=''''''
menu='''
-----------------------Menu-----------------------
(d) Depositar   (s) Sacar   (e) Extrato (q) Sair
--------------------------------------------------
Escolha a operação:
'''

while True:

    opcao=input(menu)

    if opcao=='d':
        print("\n")
        print(' Depósito '.center(50,'#'))
        valor_deposito=float(input('Informe o valor do depósito: '))
        if valor_deposito>0:
            saldo+=valor_deposito
            extrato+=f'[ + ] R$ {valor_deposito:.2f} (depósito)\n'
            print('\n')
            print(' Depósito realizado com sucesso '.center(50,'#'))
        else:
            print(' Valor inválido, refaça a operação '.center(50,'#'))

    
    elif opcao=='s':
        print('\n')
        print(' Saque '.center(50,"="))
        if qtd_saques_realizados<LIMITE_DIARIO:
            valor_saque=float(input('Informe o valor do saque: '))
            if valor_saque > 0 and valor_saque<=LIMITE_VALOR_SAQUE:
                if valor_saque<=saldo:
                    saldo-=valor_saque
                    extrato+=f'[ - ] R$ {valor_saque:.2f} (saque)\n'
                    print(' Saque realizado com sucesso '.center(50,'='))
                    qtd_saques_realizados+=1
                else:
                    print(' Saldo insuficiente para o saque'.center(50,'='))
            else:
                print(' Valor inválido para a operação ou o valor do saque excede o limite máximo de R$ 500,00\n')
        else:
            print("Limite de saque diário excedido".center(50,'='))
        print('\n')


    elif opcao=='e':
        print(' Extrato '.center(50,'~'))
        print('\n')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print('\n')
        print(f' Saldo da conta: R$ {saldo:.2f} '.center(50,'~'))

        
    elif opcao=='q':
        break
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')

