import json

CADASTROS_JSON = 'cadastrosAcademicos.json'
CATEGORIAS = ('estudante', 'professor', 'turma', 'disciplina', 'matricula')
dados_iniciais = {categoria: [] for categoria in CATEGORIAS}

def carregar_dados():
    ## carregar os dados do json ou cria um novo se o arquivo não existir no momento
    try:
        with open(CADASTROS_JSON, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo no encontrado! Criação de arquivo em andamento...')
        salvar_dados(dados_iniciais)
        return dados_iniciais

def salvar_dados(dados):
    with open(CADASTROS_JSON, 'w') as arquivo:
        json.dump(dados, arquivo)


carregar_dados()

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

def manipularCategoria(categoria):
        ## funcao que vai pedir a acao do usuario para executar o crud
        print(f'\nCadastro de {categoria}')
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
                print('Ação invalida. Tente novamente.')
        except ValueError:
            print('Entrada inválida. Digite um numero.')
            
       
def geradorDeId(categoria):
        ## funcao para gerar um id unico baseado no ultimo id que se encontra dentro daquela categoria
        ## dessa forma vai ser gerado um codigo para cada cadastro 
        dados = carregar_dados()
        arr = dados[categoria] 
        if len(arr) == 0:
            return 1
        else:
            return arr[-1]['id'] + 1
            
############################         
def listar(categoria):
        ## lista a categoria informado pelo usuario
        try:
            dados = carregar_dados()
            if len(dados[categoria]) == 0:
                return f'Lista de {categoria} está vazia!'
            ## vou listar os dados de cada categoria antes do usuario incluir, exluir ou modificar para facilitar a visualizacao antes da alteração.
            print(f'\n  --- Lista de {categoria} ---')
            print('-------------------------------')     
            print(f'{"ID":<5} | {"Nome":<20}')
            print('-------------------------------')
            for item in dados[categoria]:
                print(f'{item["id"]:<5} | {item["nome"]:<20}')
            print('-------------------------------')
        except Exception as e:
            return f'Ocorreu um erro: {e}'
        
############################      
def incluir(categoria):
        ## inclui uma categoria
        try:     
            dados = carregar_dados()
            id_ = geradorDeId(categoria)
            nome = input(f'informe o nome da(o) {categoria} ->  ')
            dadoCompleto = {'id': id_, 'nome': nome}
            dados[categoria].append(dadoCompleto)
            salvar_dados(dados)
            return 'Cadastro atualizado com sucesso!'
        except Exception as e:
            return f'Ocorreu um erro {e}'

############################ 
def excluir(categoria):
        # exclui uma categoria 
        try:     
            dados = carregar_dados()
            listar(categoria)
            idSelecionado = int(input('Digite o ID do item que deseja EXCLUIR ->   '))
            for item in dados[categoria]:
                if item['id'] == idSelecionado:
                    dados[categoria].remove(item)
                    salvar_dados(dados)
                    return 'Cadastro atualizado com sucesso!'
            return 'ID não encontrado!'
        except ValueError:
            return  'ID invalido! Digite um numero'
        except Exception as e:
            return f'Ocorreu um erro: {e}'
                     
############################     
def modificar(categoria):
        ## modifica uma categoria 
        try:
            dados = carregar_dados()
            listar(categoria)
            idSelecionado = int(input("Digite o ID que deseja MODIFICAR ->   "))
            for item in dados[categoria]:
                if item['id'] == idSelecionado:
                    novoDado = input('Digite o novo nome ->   ')
                    item['nome'] = novoDado
                    salvar_dados(dados)
                    return 'Cadastro atualizado com sucesso!'
            return 'ID não encontrado!'
                
        except ValueError:
            return  'ID invalido! Digite um numero'
        except Exception as e:
            return f'Ocorreu um erro: {e}'

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
            manipularCategoria(CATEGORIAS[0])
       elif escolha == 2:
            manipularCategoria(CATEGORIAS[1])
       elif escolha == 3:
            manipularCategoria(CATEGORIAS[2])
       elif escolha == 4:
            manipularCategoria(CATEGORIAS[3])
       elif escolha == 5:
            manipularCategoria(CATEGORIAS[4])
       elif escolha == 6:
            print('Saindo do sistema')
            break
       else:
            print('Opção invalida. Tente novamente.')
    except ValueError:
        print('Entrada invalida. Digite um numero.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')



        '''
            Aluno -> Vinicius Eduardo Ribeiro Ramos
            Curso -> Analise e desenvolvimento de sistemas
            
        '''