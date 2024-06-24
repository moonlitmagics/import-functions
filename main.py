import clientes
import pecas
import servicos
import contas
import veiculos
import fornecedor

def main():
    while True:
        print("---"*20)
        print("Bem vindo a oficina mecânica!!")
        print("---"*20)
        print("Escolha uma opção para uso\n 1- Cliente\n 2- Veículos\n 3- Peças\n 4- Serviços\n 5- Contas a pagar\n 6- Fornecedor\n 0-sair ")

        a=input("Qual você deseja usar: ")
        
        if a=="1":
            print("Escolha uma opção você deseja usar\n 1-Cadastro\n 2-Alterar\n 3-Excluir\n 4-Relatório")
            b=input("O que você gostaria de usar:")
 
            if b=="1":
                clientes.cadastrar_cliente()
            elif b=="2":    
                clientes.alterar_cliente()
            elif b=="3":    
                clientes.excluir_cliente()
            elif b=="4":    
                clientes.relatorio_clientes()
 
        if a=="2":
            print("Escolha uma opção você deseja usar\n 1-Cadastro\n 2-Alterar\n 3-Excluir\n 4-Relatório")
            b=input("\nO que você gostaria de usar:")
 
            if b=="1":
                veiculos.cadastrar_veiculo()
            elif b=="2":    
                veiculos.alterar_veiculo()
            elif b=="3":    
                veiculos.excluir_veiculo()
            elif b=="4":    
                veiculos.relatorio_veiculos()
 
        if a=="3":
            print("Escolha uma opção você deseja usar\n 1-Cadastro\n 2-Alterar\n 3-Excluir\n 4-Relatório")
            b=input("\nO que você gostaria de usar:\n")
 
            if b=="1":
                pecas.cadastrar_peca()
            elif b=="2":
                pecas.alterar_peca()
            elif b=="3":
                pecas.excluir_peca()
            elif b=="4":
                pecas.relatorio_pecas()
 
        if a=="4":
            print("Escolha uma opção você deseja usar\n 1-Cadastro\n 2-Alterar\n 3-Excluir\n 4-Relatório")
            b=input("\nO que você gostaria de usar:")
 
            if b=="1":
                servicos.cadastrar_servico()
            elif b=="2":
                servicos.alterar_servico()
            elif b=="3":
                servicos.excluir_servico()
            elif b=="4":
                servicos.relatorio_servico()

        if a=="5":
            print("Escolha uma opção você deseja usar\n 1-Cadastro\n 2-Alterar\n 3-Excluir\n 4-Relatório")
            b=input("\nO que você gostaria de usar:")

            if b=="1":
                contas.cadastrar_conta()
            elif b=="2":
                contas.alterar_conta()
            elif b=="3":
                contas.excluir_conta()
            elif b=="4":
                contas.relatorio_conta()

        if a=="6":
            print("Escolha uma opção você deseja usar\n 1-Cadastro\n 2-Alterar\n 3-Excluir\n 4-Relatório")
            b=input("\nO que você gostaria de usar:")

            if b =="1":
                fornecedor.cadastar_fornecedor()
            elif b=="2":
                fornecedor.alterar_fornecedor()
            elif b=="3":
                fornecedor.excluir_fornecedor()
            elif b=="4":
                fornecedor.relatorio_fornecedor()

 
        elif a=="0":
            print("Você saiu.")
            break
   
 
 
 
main()