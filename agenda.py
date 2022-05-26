def menu():
    voltarMenu = 's'
    while voltarMenu == 's':
        opcao = input('''
            AGENDA EM PYTHON
            MENU:
        
            [1] CADASTRAR CONTATO
            [2] LISTAR CONTATO
            [3] DELETAR CONTATO
            [4] BUSCAR CONTATO PELO NOME
            [5] SAIR

        ''')
        if opcao == "1":
            cadastrarContato()
        elif opcao == "2":
            listarContato()
        elif opcao == "3":
            deletarContato()
        elif opcao == "4":
            buscarContato()
        else:
            sair()
        voltarMenu = input("Deseja voltar ao menu principal? (s/n) ").lower

def cadastrarContato():
    idContato = input("Escolha o ID do contato: ")
    nome = input("Nome do contato: ")
    telefone = input("Telefone do contato: ")
    email = input("Email do contato: ")
    try:
        agenda = open("agenda.txt", "a")
        dados = f'{idContato};{nome};{telefone};{email}\n'
        agenda.write(dados)
        agenda.close()
        print(f'Contato gravado com sucesso!!!')
    except:
        print("Erro na gravação do contato!")

def listarContato():
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        print(contato)
    agenda.close()

def deletarContato():
    nomeDeletado = input("Digite o nome do contato para ser deletado: ").lower()
    agenda = open("agenda.txt", "r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomeDeletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open("agenda.txt", "w")
    for i in aux2:
        agenda.write(i)
    print(f'O Contato foi deletado com sucesso!')
    listarContato()
    
def buscarContato():
    nome = input(f'Digite o nome do contato: ').upper()
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        if nome in (contato.split(";")[1]).upper():
            print(contato)
        
    agenda.close()

def sair():
    print(f'Até logo!')
    exit()



def main():
    menu()

main()