veiculos = []
 
def cadastrar_veiculo():
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = int(input("Ano: "))
    placa = input("Placa: ")
    cor = input("Cor: ")
    km_rodados = int(input("Km Rodados: "))
    chassi = input("Chassi: ")
    proprietario_cpf = input("CPF do Proprietário: ")
    data_aquisicao = input("Data de Aquisição: ")
    veiculo = {
        'marca': marca,
        'modelo': modelo,
        'ano': ano,
        'placa': placa,
        'cor': cor,
        'km_rodados': km_rodados,
        'chassi': chassi,
        'proprietario_cpf': proprietario_cpf,
        'data_aquisicao': data_aquisicao,
        'observacoes': ''
    }
    veiculos.append(veiculo)
    print("Veículo cadastrado com sucesso!")
 
def excluir_veiculo():
    placa = input("Placa do veículo a ser excluído: ")
    for veiculo in veiculos:
        if veiculo['placa'] == placa:
            veiculos.remove(veiculo)
            print("Veículo excluído com sucesso!")
            return
    print("Veículo não encontrado!")
 
def alterar_veiculo():
    placa = input("Placa do veículo a ser alterado: ")
    for veiculo in veiculos:
        if veiculo['placa'] == placa:
            veiculo['marca'] = input("Marca: ")
            veiculo['modelo'] = input("Modelo: ")
            veiculo['ano'] = int(input("Ano: "))
            veiculo['cor'] = input("Cor: ")
            veiculo['km_rodados'] = int(input("Km Rodados: "))
            veiculo['chassi'] = input("Chassi: ")
            veiculo['proprietario_cpf'] = input("CPF do Proprietário: ")
            veiculo['data_aquisicao'] = input("Data de Aquisição: ")
            print("Veículo alterado com sucesso!")
            return
    print("Veículo não encontrado!")
 
def relatorio_veiculos():
    for veiculo in veiculos:
        print(veiculo)