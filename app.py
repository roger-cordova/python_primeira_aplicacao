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
            troca_status_local()
        elif opcao_escolhida == 4:
            encerar_app()
        else: opcao_invalida()
    except:
        opcao_invalida()

def cadastrar_local():
    menu_principal = 1
    while (menu_principal == 1):
        exibir_subtitulos('Cadastro de novos locais')

        nome_do_local = input(f'Informe o nome do estabelecimento: ')

        categoria = input(f'Informe a categoria de {nome_do_local}: ')

        dados_do_local = {'nome':nome_do_local,'categoria':categoria,'status':False}

        locais.append(dados_do_local)

        print(f'\nO Estabelecimento {nome_do_local} foi cadastrado com sucesso\n')        

        menu_principal = int(input('Pressione 1 para cadastrar um novo locao ou pressione outra tecla para sair: '))
    else:    
        main()

def listar_local():
    exibir_subtitulos('Listando os locais cadastrados')
    espacamento = 0
    print(f'Espaçamento: {espacamento}\n')
    for tamanho_local in locais:
        if (len(tamanho_local['nome']) > espacamento):
            print(f'Espaçamento: {espacamento} -- {tamanho_local['nome']} -- len(tamanho_local[nome]): {len(tamanho_local['nome'])}\n')
            espacamento = len(tamanho_local['nome'])
        elif (len(tamanho_local['categoria']) > espacamento):
             print(f'Espaçamento: {espacamento} -- {tamanho_local['categoria']} -- len(tamanho_local[categoria]): {len(tamanho_local['categoria'])}\n')
             espacamento = len(tamanho_local['categoria'])       
        

    print(f'{'Nome do Local'.ljust(espacamento)} | {'Categoria'.ljust(espacamento)} | Status')
    for local in locais:
        nome_do_local = local['nome']
        categoria_do_local = local['categoria']
        status_do_local = 'ativado' if local['status'] else 'desativado'
        print(f'{nome_do_local.ljust(espacamento)} | {categoria_do_local.ljust(espacamento)} | {status_do_local}')

    input('\nPressione uma tecla para voltar ao menu principal: ')
    main()

def troca_status_local():    
    exibir_subtitulos('Troca Status Local')

    nome_local = input('Informe o nome do local que deseja trocar o status: ')
    local_encontrado = False

    for local in locais:
        if nome_local == local['nome']:
           local_encontrado = True
           local['status'] = not local['status']
           mensagem = f'O local {nome_local} foi ativado com sucesso' if local['status'] else f'O local {nome_local} foi desativado com sucesso'
           print(mensagem)
    if not local_encontrado:
        print(f'O local {nome_local} não foi encontrado')

    input('\nPressione uma tecla para voltar ao menu principal: ')
    main()            

def encerar_app():
    os.system('cls')

def exibir_subtitulos(texto):    
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)

    print()

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