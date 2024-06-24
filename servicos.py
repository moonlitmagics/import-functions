servicos = [] #criando uma lista vazia
 
def cadastrar_servico(): #Função cadastrar serviço
    descricao = input("Descrição: ")
    preco = float(input("Preço: "))
    modelo = input ("Modelo: ")
    tempo_estimado_horas = float(input("Tempo Estimado (horas): "))
    tecnico_responsavel = input("Técnico Responsável: ")
    data_inicio = input("Data de Início: ")
    data_fim = input("Data de Fim: ")
    veiculo_placa = input("Placa do Veículo: ")
    status = input("Status: ")
    observacoes = input("Observações: ")
    servico = {
        'descricao': descricao,
        'preco': preco,
        'modelo': modelo,
        'tempo_estimado_horas': tempo_estimado_horas,
        'tecnico_responsavel': tecnico_responsavel,
        'data_inicio': data_inicio,
        'data_fim': data_fim,
        'veiculo_placa': veiculo_placa,
        'status': status,
        'observacoes': observacoes
    }
    servicos.append(servico) # O append()método anexa um elemento ao final da lista.
    print("Serviço cadastrado com sucesso!")
 
def excluir_servico(): #Função excluir serviço
    descricao = input("Descrição do serviço a ser excluído: ")
    for servico in servicos:
        if servico['descricao'] == descricao:
            servicos.remove(servico)
            print("Serviço excluído com sucesso!")
            return # return palavra-chave é sair de uma função e retornar um valor.
    print("Serviço não encontrado!")
 
def alterar_servico(): # Função alterar serviço
    descricao = input("Descrição do serviço a ser alterado: ")
    for servico in servicos:
        if servico['descricao'] == descricao:
            servico['preco']

def relatorio_servico():
    for servico in servicos:
        print(servico)