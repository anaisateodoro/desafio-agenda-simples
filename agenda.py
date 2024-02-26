# Agenda simples - Lista de contatos

#Adicionando contato
def adicionar_contato(contatos):
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    favorito = input("Marcar como favorito? (s/n): ")
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": favorito.lower() == "s"}
    contatos.append(contato)
    print(f"Contato {nome} foi adicionado com sucesso!")

# Visualizar contato
def ver_contatos(contatos):
    print("\nLista de Contatos:")   
    for indice, contato in enumerate(contatos, start=1):
        status_favorito = "✓" if contato["favorito"] else " "
        print(f"{indice}. {status_favorito} {contato['nome']} - {contato['telefone']} - {contato['email']}")

#Editar contato
def editar_contato(contatos):
    ver_contatos(contatos)
    indice_contato = input("Digite o número do contato que deseja editar: ")
    indice_contato = int(indice_contato) -  1
    if  0 <= indice_contato < len(contatos):
        print("1. Nome")
        print("2. Telefone")
        print("3. Email")
        print("4. Favorito")
        escolha = input("Digite a opção que deseja editar: ")
        if escolha == "1":
            novo_nome = input("Novo nome: ")
            contatos[indice_contato]["nome"] = novo_nome
        elif escolha == "2":
            novo_telefone = input("Novo telefone: ")
            contatos[indice_contato]["telefone"] = novo_telefone
        elif escolha == "3":
            novo_email = input("Novo email: ")
            contatos[indice_contato]["email"] = novo_email
        elif escolha == "4":
            novo_favorito = input("Marcar como favorito? (s/n): ")
            contatos[indice_contato]["favorito"] = novo_favorito.lower() == "s"
        else:
            print("Opção inválida.")
        print("Contato editado com sucesso.")
    else:
        print("Índice de contato inválido.")

# Marcar e desmarcar contato favorito
def marcar_desmarcar_favorito(contatos):
    ver_contatos(contatos)
    indice_contato = input("Digite o número do contato que deseja marcar/desmarcar como favorito: ")
    indice_contato = int(indice_contato) -  1
    if  0 <= indice_contato < len(contatos):
        contatos[indice_contato]["favorito"] = not contatos[indice_contato]["favorito"]
        print("Status de favorito alterado com sucesso.")
    else:
        print("Índice de contato inválido.")
       
#Visualizar Favoritos
def ver_favoritos(contatos):
    print("\nLista de Contatos Favoritos:")
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            print(f"{indice}. {contato['nome']} - {contato['telefone']} - {contato['email']}")

#Apagar Contato
def apagar_contato(contatos):
    ver_contatos(contatos)
    indice_contato = input("Digite o número do contato que deseja apagar: ")
    indice_contato = int(indice_contato) -  1
    if  0 <= indice_contato < len(contatos):
        contatos.pop(indice_contato)
        print("Contato apagado com sucesso.")
    else:
        print("Índice de contato inválido.")

# Menu Principal
contatos = []

while True:
    print("*************************************")
    print("Agenda Simples - Lista de Contatos:")
    print("***********************************")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Editar contato")
    print("4. Marcar/Desmarcar favorito")
    print("5. Ver favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    try:
        escolha = int(input("Digite a sua escolha:"))
        if escolha <  1 or escolha >  7:
            print("***********************************")
            raise ValueError("Escolha inválida. Por favor, escolha um número entre  1 e  7.")
        print("***********************************")
    except ValueError as e:
        print(f'Erro: {e}')
        continue  # Volta para o início do loop sem executar o código abaixo

    if escolha ==  1:
        adicionar_contato(contatos)
    elif escolha ==  2:
        ver_contatos(contatos)
    elif escolha ==  3:
        editar_contato(contatos)
    elif escolha ==  4:
        marcar_desmarcar_favorito(contatos)
    elif escolha ==  5:
        ver_favoritos(contatos)
    elif escolha ==  6:
        apagar_contato(contatos)
    elif escolha ==  7:
        break

print("""
\n******************************
Programa finalizado!
******************************
""")
