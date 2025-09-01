'''
/*******************************************************************************
Autor: João Pedro da Silva Ferreira
Componente Curricular: MI - Algoritmos
Concluido em: 25/10/2024
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************/

-Código feito e testado no sistema operacional Windows 11, utilizando a versão 3.12.6 do Python

Bibliotecas utilizadas:
random - Parte da biblioteca padrão, não precisa ser instalada.
time - Parte da biblioteca padrão, não precisa ser instalada.
os - Parte da biblioteca padrão, não precisa ser instalada.
msvcrt - Parte da biblioteca padrão, não precisa ser instalada.
keyboard - Precisa ser instalada (você pode usar pip install keyboard).
pyfiglet - Precisa ser instalada (use pip install pyfiglet).

'''
import os
import random
import time
import keyboard
import pyfiglet
import msvcrt as m

# Limpa a tela do terminal. A função os.system('cls') é usada para limpar a tela, e o tempo de espera (time.sleep) é usado antes e depois de limpar a tela, caso ti e tf sejam passados como argumentos.
def limpar(ti=0, tf=0):
    time.sleep(ti)
    os.system('cls')
    time.sleep(tf)
    
# Retorna uma string colorida com estilo e fundo configuráveis pelos parametros. As cores e estilos são mapeados em dicionários e são usados para gerar o código ANSI que aplica a cor no texto exibido no terminal.
def colorir_txt(txt, cor_txt='padrao', cor_fundo='padrao', estilo='padrao'):
    cores = {
        "padrao": 39, "preto": 30, "vermelho": 31, "verde": 32, "amarelo": 33,
        "azul": 34, "magenta": 35, "ciano": 36, "branco": 37,
        "preto_claro": 90, "vermelho_claro": 91, "verde_claro": 92,
        "amarelo_claro": 93, "azul_claro": 94, "magenta_claro": 95,
        "ciano_claro": 96, "branco_claro": 97
    }

    fundos = {
        "padrao": 49, "preto": 40, "vermelho": 41, "verde": 42, "amarelo": 43,
        "azul": 44, "magenta": 45, "ciano": 46, "branco": 47,
        "preto_claro": 100, "vermelho_claro": 101, "verde_claro": 102,
        "amarelo_claro": 103, "azul_claro": 104, "magenta_claro": 105,
        "ciano_claro": 106, "branco_claro": 107
    }

    estilos = {
        "padrao": 0, "negrito": 1, "opaco": 2, "italico": 3, "sublinhado": 4,
        "piscar": 5, "invertido": 7, "oculto": 8, "tachado": 9
    }

    cod_txt = cores.get(cor_txt, cores["padrao"])
    cod_fundo = fundos.get(cor_fundo, fundos["padrao"])
    cod_estilo = estilos.get(estilo, estilos["padrao"])

    cod_cor = f'\033[{cod_estilo};{cod_txt};{cod_fundo}m'
    cod_limpar = '\033[0m'

    return f"{cod_cor}{txt}{cod_limpar}"

# Puxa os dados do arquivo de questões.
def puxar_questoes(arq):
    trocar = {
        'Questions =': '',
        'category:': '"category":',
        'value:': '"value":',
        'questionPath:': '"questionPath":',
        'questionText:': '"questionText":',
        'option1:': '"option1":',
        'option2:': '"option2":',
        'option3:': '"option3":',
        'option4:': '"option4":',
        'option5:': '"option5":',
        'answer:': '"answer":',
        'explanation:': '"explanation":',
        'hint:': '"hint":'
    }
    with open(arq, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
    
    # Utiliza um dicionario para auxiliar ao colocar aspas nas chaves dos dicionarios do arquivo e eliminar partes que não serão necessarias.
    for k, v in trocar.items():
        conteudo = conteudo.replace(k, v)
    
    # Retorna o conteudo do arquivo com a função eval, transformando ele em uma lista de dicionarios.
    return eval(conteudo.strip())
                
# Verifica se o jogador respondeu corretamente, comparando a alternativa correspondende ao indice selecionado com a resposta da questão.
def verificar_acerto(lista, resp, ind):
    if lista[ind][f'option{resp}'] == lista[ind]['answer']:
        return True
    else:
        return False

# Formatação do menu inicial do jogo. Que dependendo do parametro passado destaca alguma opção.
def menu(destac=''):
    modos = {'1': 'Jogar', '2': 'Guia', '3': 'Hall da Fama'}

    print(colorir_txt(pyfiglet.figlet_format('AskMe'), 'azul', estilo='negrito'))
    print(colorir_txt('Bem vindo ao AskMe!!', 'azul'))
    print(colorir_txt('O que deseja fazer?\n', 'amarelo'))
    for n, m in modos.items():
        if destac == n:
            print(colorir_txt(f'[{n}] >> {m} <<', 'magenta'))
        else:
            print(f'[{n}]    {m}')
    print()
    print(colorir_txt('[ENTER] - Para confirmar\n[ESC] - Fechar o programa', 'amarelo'))

# Formatação do menu dos modos de jogo. Que dependendo do parametro passado destaca algum deles.
def modos(destac=''):
    modos = {'1': 'Número de questões fixas', '2': 'Limite de tempo', '3': 'Tente não errar'}

    print(colorir_txt(pyfiglet.figlet_format('Modos De Jogo'), 'azul', estilo='negrito'))
    print(colorir_txt('Qual modo deseja jogar?\n', 'amarelo'))
    for n, m in modos.items():
        if destac == n:
            print(colorir_txt(f'[{n}] >> {m} <<', 'magenta'))
        else:
            print(f'[{n}]    {m}')

    print(colorir_txt('\n[ENTER] - Para confirmar\n[ESC] - Para voltar ao menu', 'amarelo'))

# Exibe as ajudas disponiveis para o usuario. Destacando alguma a depender do parametro.
def ajudas(tipo, disp):
    tipos = {'7': 'Dica', '8': 'Pular Questão', '9': 'Eliminar Alternativas Erradas'}
    for n, m in tipos.items():
        if n in disp and disp[n] == True:
            if tipo == n:
                print(colorir_txt(f'[{n}] >> {m} <<', 'magenta'))
            else:
                print(f'[{n}]    {m}')

# Exibe um questão ao jogador, com enunciado, alternativas e ajudas disponiveis. Tambem destaca alguma das alternativas caso passado o parametro.
def mostrar_questao(lista, ind, opcs, destac = '', ajuda='', ajuda_disp = {}):
    for k, v in lista[ind].items():
        if k == 'questionText':
            print('>', colorir_txt(v, 'amarelo'))
            print()
        if k in opcs:
            if destac == k[6]:
                print(colorir_txt(f'[{k[6]}] >> {v} <<', cor_txt='magenta'))
            else:
                print(f'[{k[6]}]    {v}')

    print()

    match ajuda:
        case '7':
            hint = random.choice(quests[ind]['hint'])
            print(colorir_txt(f'Dica: {hint}', 'amarelo'))
        case '9':
            print(colorir_txt('Duas alternativas incorretas foram removidas.', 'amarelo'))
    
    print()
    ajudas(destac, ajuda_disp)      

# Faz a leitura da tecla pressionada pelo usuario retornando-a caso esteja dentro das opções desejadas.
def captar_tecla(opcoes, atual=''):
    tecla = keyboard.read_key(True)
    if tecla not in opcoes and atual in opcoes:
        return atual
    while tecla not in opcoes:
        tecla = keyboard.read_key(True)
    return tecla
              
# utiliza as outras funções para captar a resposta do usuario à alguma pergunta. Retornando a resposta caso esteja dentro das opções e 'enter' for pressionado ou fechando o modo de jogo caso 'esc' seja pressionado.
def captar_resposta(quests, teclas, indic, opcs, ajud='', ajuda_disp = {}):
    resp_final = ''
    novas_teclas = teclas+['esc']
    limpar()
    mostrar_questao(quests, indic, opcs, ajuda=ajud, ajuda_disp=ajuda_disp)
    resp = captar_tecla(novas_teclas)
    while resp != 'enter' or resp_final not in novas_teclas:
        if resp == 'esc':
            return resp
        if resp in novas_teclas:
            resp_final = resp
        limpar()
        mostrar_questao(quests, indic, opcs, resp_final, ajud, ajuda_disp)
        resp = captar_tecla(novas_teclas+['enter'], resp_final)

    return resp_final
    
# Remove 2 alternativas incorretas das opções com o auxilio da função sample, que escolhe um determinado numero de itens numa lista.
def remover_erradas(questoes, ind):
    alternativas = ['option1', 'option2', 'option3', 'option4', 'option5']
    for n, m in questoes[ind].items():
        if n in alternativas and questoes[ind]['answer'] == m:
            alternativas.remove(n)
            opcs = random.sample(alternativas, k=2)
            return opcs + [n]

# Exibe a tela da reposição de ajudas que ja foram utilizadas
def repor_ajudas_txt(indisp, destac=''):
    tipos = {'7': 'Dica', '8': 'Pular Questão', '9': 'Eliminar Alternativas Erradas'}
    print(colorir_txt('Qual ajuda deseja repor?', 'amarelo'))
    for n, m in tipos.items():
        if n in indisp:
            if destac == n:
                print(colorir_txt(f'[{n}] >> {m} <<', 'magenta'))
            else:
                print(f'[{n}]    {m}')

# Repoem as ajudas gastas dependendo das teclas pressionadas pelo usuario.
def repor_ajudas(ajudas):
        indisponiveis = [a for a in ajudas if not ajudas[a]]
        resp_final = ''
        limpar()
        repor_ajudas_txt(indisponiveis)
        resp = captar_tecla(indisponiveis)
        while resp != 'enter' or resp_final not in indisponiveis:
            if resp in indisponiveis:
                resp_final = resp
            limpar()
            repor_ajudas_txt(indisponiveis, resp_final)
            resp = captar_tecla(indisponiveis+['enter'], resp_final)
        ajudas[resp_final] = True


# Remove das opções de tecla os indices das ajudas ja utilizadas e alternativas incorretas se for passado o parametro de opcs.
def atualizar_teclas(teclas, ajudas, opcs = []):
    novas_teclas = [t for t in teclas if t not in ajudas or (t in ajudas and ajudas[t] == True)]
    if opcs:
        return [t for t in teclas if t in novas_teclas and (t in opcs or t in ajudas)]
    return novas_teclas  

# Gerencia as respostas do usuario, reposição de ajudas e utilização das ajudas de indice 7 e 9 (dica e remover alternativas erradas).
def responder(questoes, indic, alternativas, teclas, pontos_acumulados, ajudas_disponiveis):
    opcs = alternativas

    # A cada 60 pontos acumulados o jogador tem direito a restaurar uma ajuda gasta.
    if pontos_acumulados >= 60 and any(valor == False for valor in ajudas_disponiveis.values()):
        repor_ajudas(ajudas_disponiveis)
        pontos_acumulados = 0
            
    teclas_atuais = atualizar_teclas(teclas, ajudas_disponiveis)

    resp = captar_resposta(questoes, teclas_atuais, indic, opcs, ajuda_disp = ajudas_disponiveis)
        
    while resp in ['7', '9']:
        # toda vez  que uma ajuda é utilizada seu valor muda para False. impedindo o playes de usa-la ate que seja recuperada.
        ajudas_disponiveis[resp] = False

        teclas_atuais = atualizar_teclas(teclas, ajudas_disponiveis)
            
        match resp:
            case '7':
                resp = captar_resposta(questoes, teclas_atuais, indic, opcs, resp, ajudas_disponiveis)
            case '9':
                opcs = remover_erradas(questoes, indic)
                teclas_atuais = atualizar_teclas(teclas, ajudas_disponiveis, [n[6] for n in opcs])
                resp = captar_resposta(questoes, teclas_atuais, indic, opcs, resp, ajudas_disponiveis)

    return pontos_acumulados, resp

# Modo de jogo 1: numero de questões fixas. A partida vai continuar rodando até que o jogador responda 15 questões.
# O modo retorna a pontuação e uma lista com as questões apresentadas.
def modo_1(questoes, teclas, alternativas):
    pontuacao = 0
    pontos_acumulados = 0
    tot_quest = 15
    num_quest = 0

    # Explicar guarda as questões apresentadas ao player e ajudas_disponiveis como o nome diz guarda as ajudas e seu valor, True para liberada e False para gasta.
    explicar = []
    ajudas_disponiveis = {'7': True, '8': True, '9': True}

    while num_quest < tot_quest:
        # A questões são escolhidas pelo indice, que é gerado aleatoriamente com a função randint
        indic = random.randint(0, len(questoes)-1)
        num_quest += 1

        pontos_acumulados, resp = responder(questoes, indic, alternativas, teclas, pontos_acumulados, ajudas_disponiveis)
        
        # Caso a resposta esteja dentro dos indices de alternativa ele verifica se acertou ou não. Caso a resposta seja de indice 8, o jogo pula a questão.
        if resp in teclas[:5]:
            if verificar_acerto(questoes, resp, indic):
                ganho = int(questoes[indic]['value'])
                pontuacao += ganho
                pontos_acumulados += ganho
                print(colorir_txt(f'\nAcertou!! Pontuação: {pontuacao}', 'verde'))
            else:
                print(colorir_txt('\nErrou!!', 'vermelho'))
        elif resp == '8':
            ajudas_disponiveis[resp] = False
            num_quest -= 1
            print(colorir_txt('\nQuestão Pulada.', 'amarelo'))

        explicar.append(questoes.pop(indic))
        limpar(1)

        # Se a resposta for esc, a partida é encerrada.
        if resp == 'esc':
            print(colorir_txt('\nEncerrando a partida...', 'amarelo'))
            limpar(0.5)
            return pontuacao, explicar
            
    return pontuacao, explicar
    
# Modo 2: Limite de tempo. O jogador tem que responder corretamente todas as 15 questões apresentadas no limite de 300 segundo (5 minutos).
# A função restante ao acertar todas as questoes, alem da lista com as questões apresentadas.
def modo_2(questoes, teclas, alternativas):
    # A função perf_counter retorna um valor de tempo absoluto correspondente a algum ponto arbitrario do sitema.
    tempo_tot = 300
    tempo_ini = time.perf_counter()
    tempo_fim = 0

    selecionadas = []
    explicar = []
    tot_quest = 15
    num_quest = 0
    acertos = 0

    pontuacao = 0
    pontos_acumulados = 0
    ajudas_disponiveis = {'7': True, '8': True, '9': True}

    # As questões vão continuar se repetindo ate que o jogador acerte todas as 15 ou que o tempo se esgote.
    # Para cronometrar o tempo foi usado a formula de variação de tempo, tempo final - tempo inicial.
    while (acertos < tot_quest) and (tempo_fim - tempo_ini <= tempo_tot):
        
        indic = 0
        
        # Questões são sorteadas aleatoriamente até que o contador atinja 15.
        while num_quest < tot_quest:
            iq= random.randint(0, len(questoes)-1)
            q = questoes.pop(iq)
            selecionadas.insert(indic, q)
            explicar.append(q)
            num_quest += 1

        pontos_acumulados, resp = responder(selecionadas, indic, alternativas, teclas, pontos_acumulados, ajudas_disponiveis)
        
        # Caso a resposta esteja dentro dos indices de alternativa ele verifica se acertou ou não. Caso a resposta seja de indice 8, o jogo pula a questão.
        if resp in teclas[:5]:
            if verificar_acerto(selecionadas, resp, indic):
                print(colorir_txt('\nAcertou!!', 'verde'))
                acertos += 1
                ganhos = float(selecionadas[indic]['value'])
                pontuacao += ganhos
                pontos_acumulados += ganhos
                selecionadas.pop(indic)
            else:
                print(colorir_txt('\nErrou!!', 'vermelho'))
                selecionadas.append(selecionadas.pop(indic))
        elif resp == '8':
            ajudas_disponiveis[resp] = False
            num_quest -= 1
            selecionadas.pop(indic)
            print(colorir_txt('\nQuestão Pulada.', 'amarelo'))
        
        # O tempo final é atualizado para manter o calculo da variação correto.
        tempo_fim = time.perf_counter()
        tempo_rest = round(-(tempo_fim - tempo_ini - tempo_tot), 5)
        print('\nTempo Restante: ', tempo_rest,  'segundos.')
        print('Acertos: ', acertos)

        limpar(0.5)

        # Se a resposta for esc, a partida é encerrada.
        if resp == 'esc':
            print(colorir_txt('\nEncerrando a partida...', 'amarelo'))
            limpar(0.5)
            return tempo_rest, explicar

    return tempo_rest, explicar
    
# Modo de jogo 3: Tente nao errar. Questões vai continuar sendo apresentadas ao jogador até que ele erre ou acabe todas as questões.
def modo_3(questoes, teclas, alternativas):
    pontuacao = 0
    pontos_acumulados = 0
    errar = False
    num_quest = 0
    explicar = []

    ajudas_disponiveis = {'7': True, '8': True, '9': True}

    while questoes and not errar:
   
        indic = random.randint(0, len(questoes)-1)
        num_quest += 1

        pontos_acumulados, resp = responder(questoes, indic, alternativas, teclas, pontos_acumulados, ajudas_disponiveis)

        # Caso a resposta esteja dentro dos indices de alternativa ele verifica se acertou ou não. Caso a resposta seja de indice 8, o jogo pula a questão.
        if resp in teclas[:5]:
            if verificar_acerto(questoes, resp, indic):
                ganho = int(questoes[indic]['value'])
                pontuacao += ganho
                pontos_acumulados += ganho
                print(colorir_txt(f'\nAcertou!! Pontuação: {pontuacao}', 'verde'))
            else:
                print(colorir_txt('\nErrou!! Fim de jogo!', 'vermelho'))
                errar = True
        elif resp == '8':
            ajudas_disponiveis[resp] = False
            num_quest -= 1
            print(colorir_txt('\nQuestão Pulada.', 'amarelo'))

        explicar.append(questoes.pop(indic))
        limpar(1)

        # Se a resposta for esc, a partida é encerrada.
        if resp == 'esc':
            print(colorir_txt('\nEncerrando a partida...', 'amarelo'))
            limpar(0.5)
            return pontuacao, explicar

    return pontuacao, explicar

# A função recebe uma lista com questões e apesenta cada uma delas destacando a resposta correta.
def explicar_questoes(lista, opcs):

    limpar(0.5)

    print(colorir_txt('\nExplicação das questões apresentadas:\n', 'amarelo'))
    for q in lista:
        for k, v in q.items():
            if k == 'questionText':
                print('\n>', v)
                print()
            if k in opcs:
                if q['answer'] == v:
                    print(colorir_txt(f'[{k[6]}] >> {v} <<', cor_txt='verde',))
                else:
                    print(f'[{k[6]}]    {v}')
            if k == 'explanation':
                print('\nExplicação: ', v)
        print()
        print('=-'*20)

    # O jogador continuara nessa tela até que aperte esc.
    print(colorir_txt('Pressione [ESC] para sair.', 'amarelo'))
    time.sleep(1)
    keyboard.wait('esc', True)
    limpar(0.5)

# Tela com todas as informações sobre o Quiz.
def guia():
    print(colorir_txt(pyfiglet.figlet_format('Guia AskMe'), 'magenta', estilo='negrito'))
    
    print(colorir_txt('[COMO JOGAR]', 'azul'))
    print('\nPara jogar, você deve selecionar uma opção utilizando as teclas numéricas, que representam as opções disponíveis. À medida que você pressiona o número correspondente, a opção é destacada. Quando você tiver escolhido sua resposta, pressione Enter para confirmá-la.')

    print(f'\n{'=-'*40}\n')

    print(colorir_txt('[HALL DA FAMA]', 'azul'))
    print('\nNo Hall da Fama, as 10 maiores pontuações de cada modo de jogo são registradas, permitindo que os jogadores vejam quem alcançou os melhores resultados em cada categoria. Para ser registrado no Hall da Fama, você precisa alcançar uma pontuação alta o suficiente para figurar entre os 10 primeiros colocados no modo de jogo em que participou. Caso consiga essa marca, seu nome e pontuação serão exibidos na Hall, garantindo reconhecimento e orgulho por sua conquista.')

    print(f'\n{'=-'*40}\n')

    print(colorir_txt('[MODOS]', 'azul'))

    print(colorir_txt('\n> Número de questões fixas: ', 'amarelo'), 'Neste modo, você responderá a 15 perguntas. Cada questão possui uma pontuação específica, e toda vez que você acerta, recebe os pontos correspondentes àquela questão. No final, sua pontuação será a soma de todos os acertos. Prepare-se e acerte o máximo que puder!')

    print(colorir_txt('\n> Limite de tempo: ', 'amarelo'),'Neste modo, você terá 5 minutos para responder a 15 questões. Sua pontuação será determinada pelo tempo que sobrar ao concluir todas as questões, ou seja, quanto mais rápido você responder corretamente, maior será a sua pontuação final. Mostre sua agilidade e conhecimento para vencer o relógio!')

    print(colorir_txt('\n> Tente não errar: ', 'amarelo'),'Neste modo, objetivo é responder corretamente o máximo de questões possível, sem cometer erros. Cada questão tem uma pontuação específica e você ganha pontos a cada resposta correta. O jogo continuará até você errar uma pergunta ou até responder todas as questões disponíveis. Sua pontuação final será a soma das pontuações das questões que você acertou, então cada acerto conta para o seu desempenho. Tente acertar o máximo que puder!')

    print(f'\n{'=-'*40}\n')

    print(colorir_txt('[AJUDAS DISPONIVEIS NO JOGO]', 'azul'))

    print(colorir_txt('\n> Dica: ', 'amarelo'),'Oferece uma pista para ajudá-lo a responder a questão. Ao utilizá-la, uma sugestão será revelada para guiá-lo em sua escolha, facilitando a resolução da pergunta.')

    print(colorir_txt('\n> Pular Questão: ', 'amarelo'),'Você pode trocar a questão atual por outra. Caso não saiba a resposta ou queira avançar rapidamente, basta usar essa ajuda para seguir para a próxima questão.')

    print(colorir_txt('\n> Eliminar Opções Erradas: ', 'amarelo'),'Remove duas alternativas incorretas de uma pergunta. Com isso, você fica com apenas três opções restantes, aumentando suas chances de acertar a resposta.')

    print(colorir_txt('\nComo funciona: ', 'amarelo'),'No jogo, pode-se utilizar as três ajudas em uma mesma questão, mas cada vez que uma ajuda é utilizada, ela ficará bloqueada. Para desbloquear uma ajuda bloqueada, o jogador precisa acumular 60 pontos. Após atingir essa pontuação, o jogador terá a oportunidade de escolher qual das ajudas desabilitadas deseja recuperar, podendo utilizá-la novamente nas próximas questões.')
    
    print(colorir_txt('\nPressione [ESC] para sair.', 'amarelo'))
    time.sleep(1)
    keyboard.wait('esc', True)
    limpar(0.5)

# Função responsavel por gerenciar a passagem pelos menus. retorna o indice da opção destacada caso pressione enter e retorna esc caso pressione esc.
def menus(teclas, tipo):
    novas_teclas = teclas+['esc']
    tec_final = ''
    eval(f'{tipo}()')
    tec = captar_tecla(novas_teclas)
    while tec != 'enter' or tec_final not in teclas:
        if tec == 'esc':
            return tec
        if tec in teclas:
            tec_final = tec
        limpar(ti=0.1)
        eval(f'{tipo}(tec_final)')
        tec = captar_tecla(novas_teclas+['enter'], tec_final)

    return tec_final

# Retorna a posição que o novo jogador entraria no ranking com determinada pontuação.
def rankear(ranking, pontos):
    for i, j in enumerate(ranking):
        if pontos > j['pontos']:
            return i
        
    return len(ranking)

# Lê os dados dos arquivos do hall da fama, caso existam. Retornando uma lista com o ranking.
def puxar_ranking(hall):
    rank = []
    if os.path.isfile(hall):
        with open(hall, 'r',encoding='utf-8') as dados:
            for linha in dados:
                nome, pontos = linha.strip().split(':')
                rank.append({'nome': nome.strip(), 'pontos': float(pontos.strip())})
    return rank

# Exibe os Halls da fama.
def halls():
    print(colorir_txt(pyfiglet.figlet_format('Hall Da Fama'), 'azul', estilo='negrito'))
    hall = []
    modos = {'1': 'Número de questões fixas', '2': 'Limite de tempo', '3': 'Tente não errar'}
    for n, modo in modos.items():
        hall = puxar_ranking(f'Hall_Modo{n}.txt')

        print(f'\n{'=-'*40}\n')
        print(colorir_txt(f'Modo {n}: {modo}', 'magenta', estilo='negrito'))
        print(f'{'--'*40}')
        print(colorir_txt(f"{'Pos.':<5}{'Nome':<10}{'Pontos'}\n", 'ciano'))
        for i, j in enumerate(hall, start=1):
            if i % 2 == 1:
                print('{:<5}{:<10}{:<10}'.format(f'{i:0>2}', j['nome'], j['pontos']))
            else:
                print(colorir_txt('{:<5}{:<10}{:<10}', cor_fundo='preto_claro').format(f'{i:0>2}', j['nome'], j['pontos']))
    print(f'\n{'=-'*40}\n')
    print(colorir_txt('\nPressione [ESC] para sair.', 'amarelo'))
    time.sleep(1)
    keyboard.wait('esc', True)
    limpar(0.5)

# Limpa o buffer de teclado, para que não haja interferencia na hora do jogador inserir seu nome.
def limpar_buffer():
  while m.kbhit():
    m.getch()


# Código Principal

caminho_arquivo = 'Banco_de_Questões.txt'

# Executa o programa caso o arquivo das questões seja encontrado.
if os.path.isfile(caminho_arquivo):
    print(colorir_txt('Arquivo encontrado!\nIniciando o programa...', 'amarelo'))
    limpar(ti=2)

    quests = puxar_questoes(caminho_arquivo)

    opc = ''
    modo = ''
    teclas = ['1', '2', '3', '4', '5', '7', '8', '9']
    alternativas = ['option1', 'option2', 'option3', 'option4', 'option5']

    # loop do menu inicial, continua ate que esc seja retornado, alterando o valor da variavel encerrar.
    encerrar = False
    while not encerrar:

        opc = menus(teclas[:3], 'menu')

        limpar()
        
        # De acordo com a tecla retornada pelo menu: encerra o programa (esc), abre os modos de jogo(1), mostra o guia(2) ou exibe os halls da fama(3).
        match opc:
            case 'esc':
                encerrar = True
                print(colorir_txt('\n> PROGRAMA ENCERRADO <', 'amarelo'))
            case '1':
                #loop do menu dos modos de jogo. se encerra quando o menu retorna esc, alterando o valor da variavel jogar.
                jogar = True
                while jogar:
                    
                    modo = menus(teclas[:3], 'modos')

                    limpar()

                    # Dependendo do valor retornado pelo menu dos modos, abre um dos tres modos disponiveis ou volta para o menu inicial.
                    match modo:
                        case 'esc':
                            modo = ''
                            jogar = False
                            print(colorir_txt('VOLTANDO AO MENU...', 'amarelo'))
                            limpar(ti=1)   
                        case '1':
                            pontuacao, explicar = modo_1(quests, teclas, alternativas)
                        case '2':
                            pontuacao, explicar = modo_2(quests, teclas, alternativas)
                        case '3':
                            pontuacao, explicar = modo_3(quests, teclas, alternativas)

                    limpar(1)
                    
                    # Apos alguma partida o programa analiza se o jogador conseguiu pontuação suficiente para entrar no hall da fama daquele modo.
                    if modo in teclas[:3]:
                        hall = f'Hall_Modo{modo}.txt'
                        
                        ranking = puxar_ranking(hall)

                        print(colorir_txt('Calculando a pontuação...', 'amarelo'))

                        limpar(0.5)
                        
                        # caso o hall ainda nao tenha atingido o numero maximo ou o jogador atinja uma pontuação maior que o ultimo no ranking ele pode entrar no hall da fama. Isso somado ao fato de que ele não pode ter zerado a pontuação.
                        if (len(ranking)<10 or pontuacao > ranking[-1]['pontos']) and pontuacao > 0:
                            
                            pos = rankear(ranking, pontuacao)
                            
                            print(colorir_txt(f'Parabéns!! Você atingiu a pontuação necessaria para entrar na {pos+1}ª posição do Hall Da Fama!!\n', 'verde', estilo='negrito'))
                            

                            confirmar = False
                            while not confirmar:
                                limpar_buffer()
                                nome_jogador = str(input(colorir_txt('Digite o nome que deseja usar [Limite de 5 caracteres]: ', 'amarelo'))).strip()[:5].strip()
                                while not nome_jogador:
                                    nome_jogador = str(input(colorir_txt('Digite o nome que deseja usar [Limite de 5 caracteres]: ', 'amarelo'))).strip()[:5].strip()
                                print(colorir_txt(f'\nDeseja se registrar com o nome "{nome_jogador}"?\n[Enter] Sim / [Esc] Não', 'amarelo'))
                                time.sleep(0.5)
                                resp = captar_tecla(['enter', 'esc'])
                                if resp == 'enter':
                                    confirmar = True
                                

                            # o jogador é inserido no ranking e caso o ranking fique com mais de 10 participantes os ultimos vão sendo retirados ate que volte para dentro dos limites.
                            ranking.insert(pos, {'nome': nome_jogador, 'pontos': pontuacao})
                            while len(ranking) > 10:
                                ranking.pop()

                            # O arquivo do hall é reescrito, agora com o ranking atual.
                            with open(hall, 'w', encoding='utf-8') as dados:
                                for j in ranking:
                                    dados.write(f'{j['nome']}: {float(j['pontos'])}\n')

                            print(colorir_txt('\nRegistrando...', 'amarelo'))
                            limpar(2)
                            halls()
                        else:
                            print(colorir_txt('Sua pontuação não foi suficiente! Tente novamente e conquiste seu lugar no Hall da Fama!\n', 'vermelho'))
                        
                        # O player tem a opção de ver as explicações das questões que lhe foram apresentadas antes de voltar ao menu.
                        print(colorir_txt('[ENTER]  Ver a explicação das questões apresentadas\n[ESC]  Voltar para os modos de jogo', 'amarelo'))
                    
                        tec = captar_tecla(['enter', 'esc'])
                        if tec == 'enter':
                            explicar_questoes(explicar, alternativas)
                        else:
                            limpar(0.5)

                    quests = puxar_questoes(caminho_arquivo)

            case '2':
                guia()

            case '3':
                halls()
else:
    print(colorir_txt(f'Arquivo "{caminho_arquivo}" não encontrado!! Certifiqui-se de que ele esteja na mesma pasta que o programa.', 'amarelo'))
