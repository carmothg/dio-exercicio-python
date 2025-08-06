def exibi_menu():
    menu='''
-------------------------Menu-------------------------
(d) Depositar           (s) Sacar          (e) Extrato
 
(u) Criar usuário       (c) Criar conta corrente  

(lu) Listar usuários    (lc) Listar Contas  (q) Sair
------------------------------------------------------
Escolha a operação:'''
    return input(menu)

def deposito(saldo,valor,extrato,/):
    if valor>0:
        saldo+=valor
        extrato+=f'[ + ] R$ {valor_deposito:.2f} (depósito)\n'
        print('\n')
        print(' Depósito realizado com sucesso '.center(50,'#'))
    else:
        print(' Valor inválido, refaça a operação '.center(50,'#'))
    return saldo,extrato

def saque(*,saldo,extrato,limite_valor_saque,qtd_saques_realizados):
    valor_saque=float(input('Informe o valor do saque: '))
    if valor_saque > 0 and valor_saque<=limite_valor_saque:
        if valor_saque<=saldo:
            saldo-=valor_saque
            extrato+=f'[ - ] R$ {valor_saque:.2f} (saque)\n'
            qtd_saques_realizados+=1
            print(' Saque realizado com sucesso '.center(50,'='))
        else:
            print(' Saldo insuficiente para o saque'.center(50,'='))
    else:
        print(' Valor inválido para a operação ou o valor do saque excede o limite máximo de R$ 500,00\n')
    return saldo,extrato,qtd_saques_realizados

def exibir_extrato(saldo,/,*,extrato):
    print(' Extrato '.center(50,'~'))
    print('\n')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print('\n')
    print(f' Saldo da conta: R$ {saldo:.2f} '.center(50,'~'))

def existe_usuario(cpf,usuarios):
    return [usuario for usuario in usuarios if cpf in usuario]

def criar_usuario(usuarios):
    novo_cpf=input("Digite o numero do CPF (somente números):")
    if existe_usuario(novo_cpf,usuarios):
        print("Usuario já cadastrado")
    else:
        nome=input("Digite o nome completo: ")
        data_nascimento=input("Digite a data de nascimento (dd-mm-aaaa): ")
        endereco=input("Digite o endereço (logradouro, nº - bairro - cidade/UF): ")
        usuarios.append({
            novo_cpf:{
                "nome":nome,
                "data_nascimento":data_nascimento,
                "endereco":endereco
            }
        })
        print("Usuário criado com sucesso")
    return usuarios

def listar_usuarios(usuarios):
    if usuarios:
        mensagem = '\n'.join(f'Nome: {dados["nome"]}\nCPF: {cpf}\nData de nascimento: {dados["data_nascimento"]}\nEndereço: {dados["endereco"]}\n\n' for usuario in usuarios for cpf,dados in usuario.items())
        print(mensagem)
    else:
        print("\nNenhum usuário cadastrado")

def criar_conta(contador_numero_conta,usuarios,contas,NUMERO_AG):
    cpf_titular=input("Digite o CPF do titular da conta: ")
    dados_usuario=existe_usuario(cpf_titular,usuarios)
    if dados_usuario:
        contas.append({"agencia":NUMERO_AG,"numero_conta":contador_numero_conta,"cpf_titular":cpf_titular,"dados_usuario":dados_usuario[0][cpf_titular]})
        contador_numero_conta+=1
        print("Conta criada com sucesso")
    else:
        print("Usuário não cadastrado")
    return contas,contador_numero_conta

def listar_contas(contas):
    if contas:
        mensagem = '\n'.join(f'CPF Titular: {conta["cpf_titular"]}\nNome Titular: {conta["dados_usuario"]["nome"]}\nAgência: {conta["agencia"]}\nNúmero da conta: {conta["numero_conta"]}\n\n' for conta in contas)
        print(mensagem)
        print('\n')
    else:
        print("\nNenhuma conta cadastrada")


LIMITE_VALOR_SAQUE=500
LIMITE_DIARIO=3
NUMERO_AG = '0001'

saldo=0.00
extrato=''''''
qtd_saques_realizados=0
usuarios=[]
contas_correntes=[]
contador_numero_conta=1

while True:

    opcao=exibi_menu()

    if opcao=='d':
        print("\n")
        print(' Depósito '.center(50,'#'))
        valor_deposito=float(input('Informe o valor do depósito: '))
        saldo,extrato=deposito(saldo,valor_deposito,extrato)

    elif opcao=='s':
        print('\n')
        print(' Saque '.center(50,"="))
        if qtd_saques_realizados<LIMITE_DIARIO:
            saldo,extrato,qtd_saques_realizados=saque(saldo=saldo,extrato=extrato,qtd_saques_realizados=qtd_saques_realizados,limite_valor_saque=LIMITE_VALOR_SAQUE)
        else:
            print("Limite de saque diário excedido".center(50,'='))

    elif opcao=='e':
        exibir_extrato(saldo,extrato=extrato)
    
    elif opcao=='u':
        usuarios=criar_usuario(usuarios)

    elif opcao=='c':
        contas,contador_numero_conta=criar_conta(contador_numero_conta,usuarios,contas_correntes,NUMERO_AG)

    elif opcao=='lu':
        listar_usuarios(usuarios)
    
    elif opcao=='lc':
        listar_contas(contas_correntes)

    elif opcao=='q':
        break
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')

