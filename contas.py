contas = []
 
def cadastrar_conta():
    descricao = input("Descrição: ")
    valor = float(input("Valor: "))
    vencimento = input("Data de Vencimento: ")
    status = input("Status (Pendente/Pago): ")
    fornecedor_cnpj = input("CNPJ do Fornecedor: ")
    data_emissao = input("Data de Emissão: ")
    data_pagamento = input("Data de Pagamento (se houver): ")
    forma_pagamento = input("Forma de Pagamento: ")
    observacoes = input("Observações: ")

    conta = {
        'descricao': descricao,
        'valor': valor,
        'vencimento': vencimento,
        'status': status,
        'fornecedor_cnpj': fornecedor_cnpj,
        'data_emissao': data_emissao,
        'data_pagamento': data_pagamento,
        'forma_pagamento': forma_pagamento,
        'observacoes': observacoes,
    }
    contas.append(conta)
    print("Conta a pagar cadastrada com sucesso!")
 
def excluir_conta():
    descricao = input("Descrição da conta a ser excluída: ")
    for conta in contas:
        if conta['descricao'] == descricao:
            contas.remove(conta)
            print("Conta a pagar excluída com sucesso!")
            return
    print("Conta não encontrada!")
 
def alterar_conta():
    descricao = input("Descrição da conta a ser alterada: ")
    for conta in contas:
        if conta['descricao'] == descricao:
            conta['valor'] = float(input("Valor: "))
            conta['vencimento'] = input("Data de Vencimento: ")
            conta['status'] = input("Status (Pendente/Pago): ")
            conta['fornecedor_cnpj'] = input("CNPJ do Fornecedor: ")
            conta['data_emissao'] = input("Data de Emissão: ")
            conta['data_pagamento'] = input("Data de Pagamento (se houver): ")
            conta['forma_pagamento'] = input("Forma de Pagamento: ")
            print("Conta a pagar alterada com sucesso!")
            return
    print("Conta não encontrada!")
 
def relatorio_conta():
    for conta in contas:
        print(conta)