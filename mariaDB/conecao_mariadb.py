import mariadb
import sys

try:
    conecao = mariadb.connect(
        user="user01",  #usuário criado no mariaDB
        password="pi",  #Senha Criada no mariaDB para o usuário 'user01'
        host="localhost",
        database="teste_mariadb"    #Nome do banco de teste criado no mariaDB
    )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB: {e}")
    sys.exit(1)



def imprimir_dados():
    cursor.execute("select * from produtos")

    print(f"id:   nome:     Preço:") 
    for(id,nome,preco,data_cadastro) in cursor:
        print(f"{id}-\t{data_cadastro}  - R$ {preco} \t- {nome}")

def inserir_produtos(nome,preco):
    cursor.execute("INSERT INTO produtos (nome,preco) VALUES (?,?)",(nome,preco)) ##Insere os valores de "nome" e "preco" na tabela 'produtos' do banco de dados

#inserir_produtos("Notebook",3500.85)
#imprimir_dados()
cursor = conecao.cursor()   #Chama o cursor do banco de dados
condicao = True
while condicao:
    print(f"Escolha uma das opções:\n"
          "1 - Imprimir produtos:\n"
          "2 - Inserir produtos:\n"
          "3 - Sair\n")
    
    opcao = int(input("Digite a opão escolhida: "))

    if opcao == 1:
        print("Imprimir Produtos:")
        imprimir_dados()
        print()
    elif opcao ==2:
        print("Inserir novos produtos:")
        nome = input("Digite o nome do Produto: ")
        preco = float(input("Digite o preço desse Produto: "))
        inserir_produtos(nome,preco)
        print()
    elif opcao ==3:
        print("Saindo.....")
        condicao = False
    else:
        print("Valor inválido! DIgite um novo valor.")
        print()

conecao.commit() ##Salva as alterações feitas no banco de dados
print(f"Last Inserted ID: {cursor.lastrowid}")
cursor.close()  #Fecha o cursor do banco de dados
conecao.close() #Encerra a coneção com o banco de dados
