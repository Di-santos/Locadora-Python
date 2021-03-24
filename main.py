import json

# Instanciação dos objetos
clientes = {}
fornecedores = {}
produtos = {}
vendas = {}

# Import nos objetos já existentes
try:
    with open('./clientes.json') as data:
        clientes = json.load(data)

    with open('./fornecedores.json') as data:
        fornecedores = json.load(data)

    with open('./produtos.json') as data:
        produtos = json.load(data)

    with open('./vendas.json') as data:
        vendas = json.load(data)

except:
    pass

# Funções
def clear():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


# Menu inicial
while True:

    print("\n\n\n1 - Venda")
    print("2 - Cadastro")
    print("3 - Consulta")
    print("4 - Edição")
    print("5 - Exclusão")
    print("6 - Sair")

    escolha1 = int(input("\n"))

    if escolha1 == 1:
        clear()
        print("1 - Cadastrar clientes")
        print("2 - Cadastrar fornecedores")
        print("3 - Cadastrar produtos")
        print("4 - Voltar")

        escolha2 = int(input("\n"))

        if escolha2 == 1:
            print("ALALAL")
            break

        if escolha2 == 2:
            print("ALALAL")
            break

        if escolha2 == 3:
            print("ALALAL")
            break

        if escolha2 == 4:
            print("ALALAL")
            break
    
    elif escolha1 == 2:
        clear()
        print("Aba de cadastro")
    
    elif escolha1 == 3:
        clear()
        print("Aba de consulta")
    
    elif escolha1 == 4:
        clear()
        print("Aba de edição")
    
    elif escolha1 == 5:
        clear()
        print("Aba de exclusão")
    
    elif escolha1 == 6:
        break
        