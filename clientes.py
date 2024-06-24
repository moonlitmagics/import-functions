clientes = []  #criando uma lista vazia

def cadastrar_cliente(): # Função cadastrar cliente
    nome = str(input("Nome: "))
    telefone = int(input("Telefone: "))
    email = input("Email: ")
    endereco = input("Endereço: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    cep = input("Cep: ")
    cpf = input("Cpf: ")
    rg = input("Informe seu RG: ")
    data_nascimento = input("Data de Nascimento (AAAA/MM/DD): ")
    
    cep_formatado = f"{cep[:5]}-{cep[5:]}" #insere o hifen apos os 5 digitos.
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    rg_formatado = f"{rg[:2]}.{rg[2:5]}.{rg[5:8]}-{rg[8:]}"
    data_nascimento_formatado = f"{data_nascimento[6:8]}/{data_nascimento[4:6]}/{data_nascimento[:4]}" # 2006/11/17

    # criação de um dicionario para armazenar os dados dos clientes
    cliente = {
        'nome': nome,
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
        'cidade': cidade,
        'estado': estado,
        'cep': cep_formatado,
        'cpf': cpf_formatado,
        'rg': rg_formatado,
        'data_nascimento': data_nascimento_formatado,
    }
    clientes.append(cliente) #  O append() método anexa um elemento ao final da lista.
    print("Cliente cadastrado com sucesso!")
 
def excluir_cliente():
    cpf = input("CPF do cliente a ser excluído: ")
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            clientes.remove(cliente)
            print("Cliente excluído com sucesso!")
            return # return palavra-chave é sair de uma função e retornar um valor.
    print("Cliente não encontrado!")
 
def alterar_cliente():
    cpf = input("CPF do cliente a ser alterado: ")
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            cliente['nome'] = input("Nome: ") # Solicita ao usuario que digite o nome e armazena essa entrada no dicionario sob a chave 'nome', alterando como estava antes.
            cliente['telefone'] = input("Telefone: ")
            cliente['email'] = input("Email: ")
            cliente['endereco'] = input("Endereço: ")
            cliente['cidade'] = input("Cidade: ")
            cliente['estado'] = input("Estado: ")
            cliente['cep'] = input("CEP: ")
            cliente['data_nascimento'] = input("Data de Nascimento: ")
            cliente['sexo'] = input("Sexo: ")
            print("Cliente alterado com sucesso!")
            return
    print("Cliente não encontrado!")
 
def relatorio_clientes(): # Mostra todos os dados dos clientes.
    for cliente in clientes:
        print(cliente)