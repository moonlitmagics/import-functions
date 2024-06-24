fornecedores = []
 
def cadastrar_fornecedor():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    endereco = input("Endereço: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    cep = input("CEP: ")
    cnpj = input("CNPJ: ")
    nome_representante = input("Nome do Representante: ")
    telefone_representante = input("Telefone do Representante: ")
    fornecedor = {
        'nome': nome,
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
        'cidade': cidade,
        'estado': estado,
        'cep': cep,
        'cnpj': cnpj,
        'nome_representante': nome_representante,
        'telefone_representante': telefone_representante,
        'observacoes': ''
    }
    fornecedores.append(fornecedor)
    print("Fornecedor cadastrado com sucesso!")
 
def excluir_fornecedor():
    cnpj = input("CNPJ do fornecedor a ser excluído: ")
    for fornecedor in fornecedores:
        if fornecedor['cnpj'] == cnpj:
            fornecedores.remove(fornecedor)
            print("Fornecedor excluído com sucesso!")
            return
    print("Fornecedor não encontrado!")
 
def alterar_fornecedor():
    cnpj = input("CNPJ do fornecedor a ser alterado: ")
    for fornecedor in fornecedores:
        if fornecedor['cnpj'] == cnpj:
            fornecedor['nome'] = input("Nome: ")
            fornecedor['telefone'] = input("Telefone: ")
            fornecedor['email'] = input("Email: ")
            fornecedor['endereco'] = input("Endereço: ")
            fornecedor['cidade'] = input("Cidade: ")
            fornecedor['estado'] = input("Estado: ")
            fornecedor['cep'] = input("CEP: ")
            fornecedor['nome_representante'] = input("Nome do Representante: ")
            fornecedor['telefone_representante'] = input("Telefone do Representante: ")
            print("Fornecedor alterado com sucesso!")
            return
    print("Fornecedor não encontrado!")
 
def relatorio_fornecedores():
    for fornecedor in fornecedores:
        print(fornecedor)