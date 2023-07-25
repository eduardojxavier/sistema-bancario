def menu():
    
    print ('''
    
    [1] Criar Novo Usuário
    [2] Criar Nova Conta
    [3] Saque
    [4] Depósito
    [5] Extrato
    ''')


def testarConta (numConta, contas):
    for conta in contas:
            if conta == numConta:

                return conta

def deposito(contas, extrato):
    numConta=int(input("Digite o número da conta para depósito: \n"))
    conta = testarConta(numConta, contas)
    for conta in contas:
        if conta['numConta'] == numConta:
            saldo=conta['saldoConta']
            valor=int(input("Digite o valor do depósito: \n"))
            saldo=saldo+valor
            print("Valor depositado com sucesso.")
            print(f"Saldo atual: R$ {saldo:.2f}")
            extrato.append({"NumConta": numConta, "Depósito":valor})
            print(extrato)
            conta['saldoConta']=saldo
        else:
            print("Conta não existe.")
    return conta['saldoConta']

def saque(contas,limite_conta,limite_saque,extrato):
    numConta=int(input("Digite o número da conta para saque: \n"))
    conta = testarConta(numConta, contas)
    for conta in contas:
        if conta['numConta'] == numConta:
            saldo=conta['saldoConta']
            limiteConta=conta['limite_conta']
            limiteSaque=conta['limite_saques']
            
            valor=int(input("Digite o valor do saque: \n"))
            if saldo < valor:
                print("Saldo insuficiente.")
            elif valor > limite_conta:
                print("Saque excede o limite por operação.")
            elif limiteSaque == 0: 
                print("Quantidade limite de saques diários excedido.")

            else:
                saldo=saldo-valor
                print("Valor sacado com sucesso.")
                print(f"Saldo atual: R$ {saldo:.2f}")
                limiteSaque=limiteSaque-1
                extrato.append({"NumConta": numConta, "Saque":valor})
                conta['saldoConta']=saldo
                conta['limite_saques']=limiteSaque
                
        else:
            print("Conta não existe.")
    return conta['saldoConta']


def imprimirExtrato(contas, extrato):
    numConta = int(input("Digite o número da conta: \n")) 
    print("==========================================")
    print("================EXTRATO===================")
    
    conta = testarConta(numConta, contas)
    for conta in extrato:
        if conta == numConta:
            print(conta)
        #else:
            #print("Não há movimentações.")
    
def cadastroUsuario(usuarios):
    cpf = int(input("Digite o CPF (somente números): \n"))
    usuarioCadastrado = testarUsuario(cpf,usuarios)

    if usuarioCadastrado:
        print("CPF já existe cadastrado no sistema.\n")
        return
    
    nome = str(input("Digite o nome do cliente: \n"))
    endereco = str(input("Digite o endereço completo no formato RUA, Nº – BAIRRO - CIDADE/SIGLA DO ESTADO: \n"))
    dataNascimento = str(input("Digite a data de nascimento no formato DD/MM/AAAA: \n"))
    usuarios.append({"cpf":cpf, "nome":nome, "endereco":endereco, "dataNascimento":dataNascimento})
    print("Usuário cadastrado com sucesso!")
    print(usuarios)
    

def testarUsuario(cpf,usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            
            return usuario
        
def criarNovaConta (contas,usuarios,AGENCIA, limite_conta, limite_saques):
    cpf = int(input("Digite o CPF do cliente: \n"))
    usuario = testarUsuario(cpf,usuarios)

    if usuario:
        numConta = len(contas)+1
        contas.append({"cpf":cpf, 
                    "agencia":AGENCIA, 
                    "numConta":numConta, 
                    "limite_conta":limite_conta, 
                    "limite_saques":limite_saques,
                    "saldoConta": 0})
        print("Nova conta cadastrada com sucesso.")
        print(contas)

    else:
        print("Cliente não encontrado. Conta não cadastrada. Verifique os dados e tente novamente.")
    
    return contas, usuarios

            
def main():

    AGENCIA = '0001'
    usuarios = [{'cpf': 123, 'nome': 'fsadf', 'endereco': 'adfads', 'dataNascimento': 'asdfasd'}, {'cpf': 234, 'nome': 'fsadf', 'endereco': 'adfads', 'dataNascimento': 'asdfasd'}]
    contas = [{'cpf': 123, 'agencia': '0001', 'numConta': 1, 'limite_conta': 500, 'limite_saques': 3, 'saldoConta': 0}, {'cpf': 234, 'agencia': '0001', 'numConta': 2, 'limite_conta': 500, 'limite_saques': 3, 'saldoConta': 0}]
    limite_conta = 500
    limite_saques = 3
    extrato = [[{'NumConta': 2, 'Depósito': 1000}, {'NumConta': 1, 'Depósito': 500}]]

    while True:
        
        menu()
        opcao=int(input("Digite a opção desejada: \n"))

        if opcao == 1:
            cadastroUsuario(usuarios)

        if opcao == 2:
            criarNovaConta(contas, usuarios, AGENCIA, limite_conta, limite_saques)

        if opcao == 3:
            saque(contas, limite_conta, limite_saques,extrato)

        if opcao == 4:
            deposito(contas,extrato)     

        if opcao == 5:
            imprimirExtrato(contas, extrato)                  

main()