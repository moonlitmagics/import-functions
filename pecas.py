pecas = []
 
def cadastrar_peca():
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))
    fornecedor_cnpj = input("CNPJ do Fornecedor: ")
    data_compra = input("Data de Compra: ")
    garantia_meses = int(input("Garantia (meses): "))
    categoria = input("Categoria: ")
    marca = input("Marca: ")
    local_armazenamento = input("Local de Armazenamento: ")
    peca = {
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade,
        'fornecedor_cnpj': fornecedor_cnpj,
        'data_compra': data_compra,
        'garantia_meses': garantia_meses,
        'categoria': categoria,
        'marca': marca,
        'local_armazenamento': local_armazenamento,
        'observacoes': ''
    }
    pecas.append(peca)
    print("Peça cadastrada com sucesso!")
 
def excluir_peca():
    nome = input("Nome da peça a ser excluída: ")
    for peca in pecas:
        if peca['nome'] == nome:
            pecas.remove(peca)
            print("Peça excluída com sucesso!")
            return
    print("Peça não encontrada!")
 
def alterar_peca():
    nome = input("Nome da peça a ser alterada: ")
    for peca in pecas:
        if peca['nome'] == nome:
            peca['preco'] = float(input("Preço: "))
            peca['quantidade'] = int(input("Quantidade: "))
            peca['fornecedor_cnpj'] = input("CNPJ do Fornecedor: ")
            peca['data_compra'] = input("Data de Compra: ")
            peca['garantia_meses'] = int(input("Garantia (meses): "))
            peca['categoria'] = input("Categoria: ")
            peca['marca'] = input("Marca: ")
            peca['local_armazenamento'] = input("Local de Armazenamento: ")
            print("Peça alterada com sucesso!")
            return
    print("Peça não encontrada!")
 
def relatorio_pecas():
    for peca in pecas:
        print(peca)