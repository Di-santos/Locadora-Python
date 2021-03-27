# Falta concluir os processos de locação 

import json
import pprint

# Instanciação dos objetos
clientes = {}
veiculos = {}
locacoes = {}

# Import nos objetos já existentes
try:
    with open('./clientes.json') as data:
        clientes = json.load(data)

    with open('./veiculos.json') as data:
        veiculos = json.load(data)

    with open('./locacoes.json') as data:
        locacoes = json.load(data)

except:
    pass

#--------------------------------------------------- Funções -------------------------------------------------
def clear():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

# Cadastro
def cadastrar_cliente(num_clientes):
    for i in range(num_clientes):
        clear()
        print(f"\nCliente número: {i+1}\n")
        CPF = str(input("CPF: "))
        nome = str(input("Nome: "))
        telefone = str(input("Telefone: "))
        email = str(input("Email: "))
        endereco = str(input("Endereço: "))
        
        clientes[CPF] = {
            "nome":nome,
            "telefone":telefone,
            "email": email,
            "endereco": endereco,
            "veiculo" : ""
        }

    with open('clientes.json', 'w') as outfile:
        json.dump(clientes, outfile)

    print("Cadastro efetuado com sucesso!")

def cadastrar_veiculo(num_veiculos):
    for i in range(num_veiculos):
        clear()
        print(f"\nVeículo número: {i+1}\n")
        placa = str(input("Placa: "))
        modelo = str(input("Modelo: "))
        diaria = int(input("Valor da Diária: "))
        
        veiculos[placa] = {
            "modelo":modelo,
            "diaria": diaria,
            "alugado":False,
            "cpf_aluguel" : ""
        }

    with open('veiculos.json', 'w') as outfile:
        json.dump(veiculos, outfile)

    print("Cadastro efetuado com sucesso!")

# Consulta
def consultar_cliente(cpf):
    try:
        clear()
        print(f"\nCliente de CPF: {cpf}\n\n")
        pprint.pprint(clientes[cpf])
    
    except:
        print("Ops, algo deu errado!")

def consultar_veiculo(placa):
    try:
        clear()
        print(f"\nVeículo de placa: {placa}\n\n")
        pprint.pprint(veiculos[placa])
    
    except:
        print("Ops, algo deu errado!")

# Edição
def editar_cliente(cpf):
    try:
        clear()
        print(f"\nInformações atuais do cliente de CPF: {cpf}\n\n")
        pprint.pprint(clientes[cpf])
        novo_nome = str(input("\nNovo nome: "))
        novo_telefone = str(input("Novo telefone: "))
        novo_email = str(input("Novo email: "))
        novo_endereco = str(input("Novo endereço: "))

        clientes[cpf]["nome"] = novo_nome
        clientes[cpf]["telefone"] = novo_telefone
        clientes[cpf]["email"] = novo_email
        clientes[cpf]["endereco"] = novo_endereco

        with open('clientes.json', 'w') as outfile:
            json.dump(clientes, outfile)

        print("\nEdição efetuada com sucesso!")

    except:
        print("\nOps, algo deu errado!")

def editar_veiculo(placa):
    try:
        clear()
        print(f"\nInformações atuais do veiculo de placa: {placa}\n\n")
        pprint.pprint(veiculos[placa])
        nova_diaria = str(input("\nNovo valor da diária: "))

        veiculos[placa]["diaria"] = nova_diaria

        with open('veiculos.json', 'w') as outfile:
            json.dump(veiculos, outfile)

        print("\nEdição efetuada com sucesso!")

    except:
        print("\nOps, algo deu errado!")

# Exclusão
def excluir_cliente(cpf):
    try:
        clear()
        print(f"\nInformações atuais do cliente de CPF: {cpf}\n\n")
        pprint.pprint(clientes[cpf])
        confirmacao = input("Deseja mesmo excluir este cliente? (S/N): ")

        if confirmacao.lower() == "s":
            del clientes[cpf]
        
        else:
            return

        with open('clientes.json', 'w') as outfile:
            json.dump(clientes, outfile)

        print("\nExclusão efetuada com sucesso!")

    except:
        print("\nOps, algo deu errado!")

def excluir_veiculo(placa):
    try:
        clear()
        print(f"\nInformações atuais do veiculo de placa: {placa}\n\n")
        pprint.pprint(veiculos[placa])
        confirmacao = input("Deseja mesmo excluir este veículo? (S/N): ")

        if confirmacao.lower() == "s":
            del veiculos[placa]
        
        else:
            return

        with open('veiculos.json', 'w') as outfile:
            json.dump(veiculos, outfile)

        print("\nExclusão efetuada com sucesso!")

    except:
        print("\nOps, algo deu errado!")

# Evento
def lancar_locacao(data):
    try:
        clear()
        placa_veiculo = str(input("Placa do veículo: "))
        cpf_cliente = str(input("CPF do cliente: "))
        duracao = int(input("Duração da locação (dias): "))

        # Split na data
        data_split = data.split('/')
        dia = data_split[0]
        mes = data_split[1]
        ano = data_split[2]

        # Alterações nas entidades
        veiculos[placa_veiculo]["alugado"] = True
        veiculos[placa_veiculo]["cpf_aluguel"] = cpf_cliente
        clientes[cpf_cliente]["veiculo"] = placa_veiculo

        # Criação da locação
        locacoes[ano][mes][dia] = {
            "status": "aberto",
            "cpf_cliente":cpf_cliente,
            "placa_veiculo":placa_veiculo,
            "duracao": duracao,
            "valor": duracao * veiculos[placa_veiculo]["diaria"]
        }

        with open('clientes.json', 'w') as outfile:
            json.dump(clientes, outfile)

        with open('veiculos.json', 'w') as outfile:
            json.dump(veiculos, outfile)

        with open('locacoes.json', 'w') as outfile:
            json.dump(locacoes, outfile)
        
        print("Cadastro efetuado com sucesso!")

    except:
        print("\nOps, algo deu errado!")


# -------------------------------------------------- Código ---------------------------------------------------

# Menu inicial
while True:

    clear()
    print("1 - Evento")
    print("2 - Cadastro")
    print("3 - Consulta")
    print("4 - Edição")
    print("5 - Exclusão")
    print("6 - Panorama")
    print("7 - Sair")

    escolha1 = int(input("\n"))

    if escolha1 == 1:
        clear()
        print("\nAba de Evento\n")
        print("1 - Lançar locação")
        print("2 - Lançar devolução")
        print("3 - Voltar")

        escolha2 = int(input("\n"))

        if escolha2 == 1:
            clear()
            data = input("Digite a data de início da locação (xx/yy/zzzz): ")
            lancar_locacao(data)
         
    elif escolha1 == 2:
        clear()
        print("\nAba de Cadastro\n")
        print("1 - Cadastrar clientes")
        print("2 - Cadastrar veiculos")
        print("3 - Voltar")

        escolha2 = int(input("\n"))

        if escolha2 == 1:
            clear()
            num_clientes = int(input("Quantos clientes você deseja cadastrar?: "))
            cadastrar_cliente(num_clientes)
            clear()
        
        if escolha2 == 2:
            clear()
            num_veiculos = int(input("Quantos veiculos você deseja cadastrar?: "))
            cadastrar_veiculo(num_veiculos)
            clear()
        
        if escolha2 == 3:
            clear()

    elif escolha1 == 3:
        clear()
        print("\nAba de Consulta\n")
        print("1 - Consultar cliente")
        print("2 - Consultar veículo")
        print("3 - Consultar locacao")
        print("4 - Voltar")

        escolha2 = int(input("\n"))

        if escolha2 == 1:
            clear()
            cpf = input("Digite o CPF do cliente a ser consultado: ")
            consultar_cliente(cpf)
            again = input("\n\nDeseja consultar novamente? (S/N): ")

            while again.lower() == "s":
                cpf = input("\n\nDigite o CPF do cliente a ser consultado: ")
                consultar_cliente(cpf)
                again = input("\n\nDeseja consultar novamente? (S/N): ")


        if escolha2 == 2:
            clear()
            placa = input("Digite a placa do veículo a ser consultado: ")
            consultar_veiculo(placa)
            again = input("\n\nDeseja consultar novamente? (S/N): ")

            while again.lower() == "s":
                placa = input("Digite a placa do veículo a ser consultado: ")
                consultar_veiculo(placa)
                again = input("\n\nDeseja consultar novamente? (S/N): ")

    elif escolha1 == 4:
        clear()
        print("\nAba de Edição\n")
        print("1 - Editar cliente")
        print("2 - Editar veículo")
        print("3 - Voltar")
    
        escolha2 = int(input("\n"))

        if escolha2 == 1:
            clear()
            cpf = input("Digite o CPF do cliente a ser editado: ")
            editar_cliente(cpf)
            again = input("\n\nDeseja editar novamente? (S/N): ")

            while again.lower() == "s":
                cpf = input("Digite o CPF do cliente a ser editado: ")
                editar_cliente(cpf)
                again = input("\n\nDeseja editar novamente? (S/N): ")
        
        if escolha2 == 2:
            clear()
            placa = input("Digite a placa do veículo a ser editado: ")
            editar_veiculo(placa)
            again = input("\n\nDeseja editar novamente? (S/N): ")

            while again.lower() == "s":
                placa = input("Digite a placa do veículo a ser editado: ")
                editar_veiculo(placa)
                again = input("\n\nDeseja editar novamente? (S/N): ")

    elif escolha1 == 5:
        clear()
        print("\nAba de exclusão\n")
        print("1 - Excluir clientes")
        print("2 - Excluir veículo")
        print("3 - Voltar")
    
        escolha2 = int(input("\n"))

        if escolha2 == 1:
            clear()
            cpf = input("Digite o CPF do cliente a ser excluído: ")
            excluir_cliente(cpf)
            again = input("\n\nDeseja excluir outro cliente? (S/N): ")

            while again.lower() == "s":
                cpf = input("Digite o CPF do cliente a ser excluído: ")
                excluir_cliente(cpf)
                again = input("\n\nDeseja excluir outro cliente? (S/N): ")
        
        if escolha2 == 2:
            clear()
            placa = input("Digite a placa do veículo a ser excluído: ")
            excluir_veiculo(placa)
            again = input("\n\nDeseja excluir outro veiculo? (S/N): ")

            while again.lower() == "s":
                placa = input("Digite a placa ser excluído: ")
                excluir_veiculo(placa)
                again = input("\n\nDeseja excluir outro veiculo? (S/N): ")

    elif escolha1 == 6:
        clear()
        print("\nAba de Panorama\n")
        print("1 - Panorama: clientes")
        print("2 - Panorama: veículos")
        print("2 - Panorama: locacoes")
        print("3 - Voltar")

    elif escolha1 == 7:
        break

    else:
        clear()
        print("digite uma opção válida!")
        
    
    
