import os

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
    opcao_escolhida = int(input('Escolha uma opção: '))
    if opcao_escolhida == 1:
        cadastrar_local()
    elif opcao_escolhida == 2:
        listar_local()
    elif opcao_escolhida == 3:
        ativar_local()
    else: encerar_app()   

def cadastrar_local():
    print('Cadastrar Restaurantes')

def listar_local():
    print('Listar Restairantes')

def ativar_local():
    print('Ativar Restaurantes')

def encerar_app():
    os.system('cls')



def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes

if __name__ == '__main__':
    main()