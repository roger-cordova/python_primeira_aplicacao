import os
locais = []

def exibir_nome_do_programa():
    print('''
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═════╝░╚═════╝░
      
      ''')
def exibir_opcoes():    
    print('1 - Cadastrar Restuarante')
    print('2 - Listar Restaurantes')
    print('3 - Ativar Restaurante')
    print('4 - Sair')

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_local()
        elif opcao_escolhida == 2:
            listar_local()
        elif opcao_escolhida == 3:
            ativar_local()
        elif opcao_escolhida == 4:
            encerar_app()
        else: opcao_invalida()
    except:
        opcao_invalida()

def cadastrar_local():
    os.system('cls')
    print('Cadastro de novos locais\n')
    nome_do_local = input('Informe o nome do estabelecimento: ')
    locais.append(nome_do_local)
    print(f'O Estabelecimento {nome_do_local} foi cadastrado com sucesso\n')
    input('Pressione uma tecla para voltar ao menu principal: ')
    main()

def listar_local():
    print('Listar Restairantes')

def ativar_local():
    print('Ativar Restaurantes')

def encerar_app():
    os.system('cls')

def opcao_invalida():
    print('Opção Inválida, por favor infore um valor de 1 a 4\n')
    input('Pressione uma tecla para voltar ao menu principal: ')
    main()
    

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()