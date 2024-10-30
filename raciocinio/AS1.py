dados = {'estudante': [], 'professor': [], 'turma': [], 'disciplina': [], 'matricula': []}

print('--- Gerenciamento Acadêmico ---')
print('-------------------------------')

def cadastro():
    print('Cadastre o dado desejado')
    print('1- Estudante')
    print('2- Professor')
    print('3- Turma')
    print('4- Disciplina')
    print('5- Matrícula')
    print('6- Sair')

def menuAction():
    print('Selecione o que deseja fazer')
    print('1- Incluir')
    print('2- Excluir')
    print('3- Listar')
    print('4- Modificar')

def cadastrarCategoria(categoria):
        ## funcao que vai pedir a acao do usuario para executar o crud
        print(f'\n-- Cadastro de {categoria} --\n')
        menuAction()
        try:
            action = int(input("Digite o número correspondente à sua escolha ->   "))
            if action == 1:
                print(f'\n{incluir(categoria)}')
            elif action == 2:
                print(f'\n{excluir(categoria)}')
            elif action == 3:
                print(f'\n{listar(categoria)}')
            elif action == 4:
                print(f'\n{modificar(categoria)}')
            else:
                print(f'\nAção invalida. Tente novamente.\n')
        except ValueError:
            print(f'\nEntrada inválida. Digite um numero.\n')
            
       
def geradorDeId(categoria):
        ## funcao para gerar um id unico baseado no ultimo id que se encontra dentro daquela categoria
        arr = dados[categoria] 
        if len(arr) == 0:
            return 1
        else:
            return arr[-1]['id'] + 1
            
############################         
def listar(categoria):
        ## lista a categoria informado pelo usuario
        try:
            if len(dados[categoria]) == 0:
                return f'\n-- Lista de {categoria} está vazia! --\n'
            ## vou listar os dados de cada categoria antes do usuario incluir, excluir e modificar para facilitar a visualizacao do que ja temos cadastrado no "banco".
            print(f'\n  --- Lista de {categoria} ---')
            print('-------------------------------')     
            print(f'{"ID":<5} | {"Nome":<20}')
            print('-------------------------------')
            for item in dados[categoria]:
                print(f'{item["id"]:<5} | {item["nome"]:<20}')
            print('-------------------------------')
        except Exception as e:
            return f'\nOcorreu um erro: {e}'
        
############################      
def incluir(categoria):
        ## inclui uma categoria
        try:     
            id_ = geradorDeId(categoria)
            nome = input(f'\ninforme o nome da(o) {categoria} ->  ')
            dadoCompleto = {'id': id_, 'nome': nome}
            dados[categoria].append(dadoCompleto)
            return f'\nCadastro atualizado com sucesso!\n'
        except Exception as e:
            return f'\nOcorreu um erro {e}'

############################ 
def excluir(categoria):
        # exclui uma categoria 
        return f'\nFuncionalidade em desenvolvimento - não é possivel excluir a {categoria}\n'
                     
############################     
def modificar(categoria):
        ## modifica uma categoria 
        return f'\nFuncionalidade em desenvolvimento - não é possivel modificar a {categoria}\n'

############################    
while True:
    '''
    loop infinito para definir qual o grupo de dados que sera atualizado pelo usuario

    ps: escolhi voltar para essa tela sempre que um dado é alterado no banco
    '''
    cadastro()
    try:
       escolha = int(input('Digite o número do item que deseja cadastrar ->  '))

       if escolha == 1:
            cadastrarCategoria('estudante')
       elif escolha == 2 or escolha == 3 or escolha == 4 or escolha == 5:
            print(f'\nOpção em desenvolvimento, volte em breve.\n')
       elif escolha == 6:
            print(f'\nSaindo do sistema\n')
            break
       else:
            print(f'\nOpção invalida. Tente novamente.\n')
    except ValueError:
        print(f'\nEntrada invalida. Digite um numero.\n')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')