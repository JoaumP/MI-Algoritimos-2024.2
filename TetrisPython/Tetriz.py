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

-Código feito e testado no sistema operacional Windows 11

Bibliotecas utilizadas:
random - Parte da biblioteca padrão, não precisa ser instalada.
time - Parte da biblioteca padrão, não precisa ser instalada.
os - Parte da biblioteca padrão, não precisa ser instalada.
keyboard - Precisa ser instalada (você pode usar pip install keyboard).
numpy - Precisa ser instalada (use pip install numpy).
pyfiglet - Precisa ser instalada (use pip install pyfiglet).
'''


from random import randint, choice
from time import sleep, perf_counter
from os import system
from keyboard import is_pressed, read_key
from numpy import copy, rot90
from pyfiglet import figlet_format

# Função para limpar o terminal.
def limpar_terminal():
    system('cls')

# Função para 'printar' o titulo do programa, a pontuação atual e a matriz passada como parametro.
def mostrar_tetris(tabuleiro):
    # A função figlet_format() cria uma arte da string inserida usando caracteres ASCII.
    print(figlet_format('Tetris  Python'))
    print('Pontuação: ', pontuacao, '\n')
    for linha in tabuleiro:
        print(''.join(linha))
    
# Função para inserir a peça atual numa copia do tabuleiro princioal.
def inserir_peca(tabuleiro, peca, x, y):
    # É feita uma copia da matriz utilizando a função copy().
    tab_temporario = copy(tabuleiro)
    # A matriz da peça é analisada indice por indice e caso a informação armazenada lá for um pedaço da peça ela é inserida no tabuleiro.
    for l, linha in enumerate(peca):
        for c, coluna in enumerate(linha):
            if coluna in '⬜🟨🟥🟩🟧🟦🟪💣':
                tab_temporario[y + l][x + c] = coluna
    # Então o tabuleiro com a peça inserida é retornado pela função.
    return tab_temporario

# Função para dar o efeito de detonação da peça bomba.
def explodir(tabuleiro, x, y):
    # Primeiro é uma area de 3x3 tendo como centro a bomba (cordenadas passadas com paramentro) é substituida por um emoji de explosão.
    # Essa substituição só ocorre caso a cordenada esteja dentro dos limites do tebuleiro.
    for l in range(-1, 2):
        for c in range(-1, 2):
            if 0 <= y + l < len(tabuleiro) and 0 <= x + c < len(tabuleiro[0]):
                tabuleiro[y + l][x + c] = '💥'

    # Há uma pequena pausa de 0.3 segundos.
    atualizar(0.3, tabuleiro)

    # Então é feito mesmo procedimento anterior, só que desta vez é usado o emoji que compõe o fundo do nosso tabuleiro.
    for l in range(-1, 2):
        for c in range(-1, 2):
            if 0 <= y + l < len(tabuleiro) and 0 <= x + c < len(tabuleiro[0]):
                tabuleiro[y + l][x + c] = '⬛'
    
# Função que verifica se há uma colisão entre a peça atual e as já fixadas no tabuleiro.
def colisao(tabuleiro, peca, x, y):
    # Caso a futura posição da peça atual na matriz já esteja ocupada por outra peça
    # ou caso essa posiçao não faça parte dos limites do tabuleiro é retornado True, indicando colisão
    # se não, é retornado False.
    for l, linha in enumerate(peca):
        for c, coluna in enumerate(linha):
            if coluna in '⬜🟨🟥🟩🟧🟦🟪💣' and (
            y + l >= len(tabuleiro) or 
            x + c < 0 or 
            x + c >= len(tabuleiro[0]) or 
            tabuleiro[y + l][x + c] in '⬜🟨🟥🟩🟧🟦🟪'):
                return True
    return False

# Função que fixa a peça no tabuleiro principal.
def fixar_peca(tabuleiro, peca, x, y):
    # Semelhante a função inserir_peca, essa fixa a peça atual no tabuleiro principal, além disso ela chama a função explodir
    # caso a peça seja uma bomba.
    for l, linha in enumerate(peca):
        for c, coluna in enumerate(linha):
            if coluna in '⬜🟨🟥🟩🟧🟦🟪':
                tabuleiro[y + l][x + c] = coluna
            elif coluna == '💣':
                explodir(tabuleiro, x, y)

# Função para rotacionar as peças.
def girar_pecas(peca, tabuleiro, x, y):
    # É Criado uma copia da peça rotacionada em 90 graus e se não houver colisão ao tentar inserir essa peça no tabuleiro ela é 
    # retornada como peça atual.
    # É utilizada a função rot90, que rotaciona uma matriz qualquer em 90 graus no sentido anti-horario.
    peca_rotacionada = rot90(peca)
    if not colisao(tabuleiro, peca_rotacionada, x, y):
        return peca_rotacionada
    # Se não houver colisão com a peça rotacionada, a peça atual continua igual a
    else:
        return peca
    
# Função para remover as linhas completas
def remover_linhas_completas(tabuleiro):
    # É feito um varredura linha por linha da matriz do tabuleiro contabilizando se cada celula daquela linha é 
    # composta por parte de alguma peça. Caso o contador chegue a 10, sinalizando que a linha esta completa, a linha é apagada 
    # e uma linha limpa (composta apenas pela peça que representa o fundo da matriz) é inserida no topo
    # contabilizando +1 no contador de linhas removidas.
    linhas_removidas = 0
    for l, linha in enumerate(tabuleiro):
        contador = 0
        for coluna in linha:
            if coluna in '⬜🟨🟥🟩🟧🟦🟪':
                contador += 1
        if contador == 10:
            tabuleiro[l] = ['🔥' for _ in range(10)]
            atualizar(0.2, tabuleiro)
            tabuleiro.pop(l)
            tabuleiro.insert(0, ['⬛' for _ in range(10)])
            linhas_removidas += 1

    # Alem de remover as linhas a função tambem realiza do calculo da pontuação resultante
    # utilisando uma pontuação base de 100 para cada linha removida e caso a quantidade de linhas removidas seja 2 ou mais
    # é retornado o dobro de pontuação.
    pont = 100 * linhas_removidas
    if linhas_removidas > 1:
        pont *= 2
    return pont

# Função que atualiza a tabuleiro secundario, aquele que aparece para o usuario durante a movimentação das peças.
def atualizar_tab(tabuleiro, peca, x, y, tempo=0):
    # Para dar a sensação de movimento da peça o terminal é limpo e a matriz é mostrada novamente, mas com a peça em uma nova posição
    # podendo ter um momento de espera no final, depedendo dos parametros.
    limpar_terminal()
    tab_com_peca = inserir_peca(tabuleiro, peca, x, y)
    mostrar_tetris(tab_com_peca)
    sleep(tempo)

# Função semelhante a função atualizar_tab, mas nessa não é usado o tabuleiro secundario
# Utilizada quando não é necessario inserir alguma peça no tabuleiro, mas ainda há alguma mudança para ser visualizada.
def atualizar(tempo, tab):
    limpar_terminal()
    mostrar_tetris(tab)
    sleep(tempo)

# Função do Menu.
def menu(msg):
    # Mostra uma arte da mensagem passada como parametro, além de um pequeno tutorial do jogo.
    print(figlet_format(msg))
    print('Para jogar use:')
    print(f'{'⬅️':>8}  - Mover para a esquerda')
    print(f'{'➡️':>8}  - Mover para a direita')
    print(f'{'⬆️':>8}  - Rotacionar')
    print(f'{'⬇️':>8}  - Queda suave')
    print(f'{'(space)':>8} - Queda rapida')
    print(f'{'(esc)':>8} - Para voltar ao menu (Durante o jogo) \n')

    print('Para iniciar pressione a tecla (enter).')
    print('Para encerrar o progrma pressione (esc)')
    
    tecla = ''
    while tecla not in ['enter', 'esc']:
        # A função read_key faz a leitura da tecla pressiodada pelo usuario.
        tecla = read_key()

        # É retornado True ou False dependendo da tecla pressionada.
        if tecla == 'enter':
            return True
        
        elif tecla == 'esc':
            print('FIM DO PROGRAMA')
            return False
    

# PROGRAMA PRINCIPAL         

# Looping responsavel por gerenciar a inicialização do jogo.
# Continuara repetindo enquanto a função menu retornar True.
continuar = menu('Tetris Python')
while continuar:

    #Criação do Tabuleiro principal e das peças do jogo.
    tabuleiro = [['⬛' for _ in range(10)] for _ in range(20)]

    I = [['⬜','⬜','⬜','⬜']]

    O = [['🟨','🟨'],
        ['🟨','🟨']]

    Z = [['🟥','🟥','⬛'],
        ['⬛','🟥','🟥']]

    S = [['⬛','🟩','🟩'],
        ['🟩','🟩','⬛']]

    L = [['⬛','⬛','🟧'],
        ['🟧','🟧','🟧']]

    J = [['🟦','⬛','⬛'],
        ['🟦','🟦','🟦']]

    T = [['🟪','🟪','🟪'],
        ['⬛','🟪','⬛']]

    B = [['💣']]

    # Lista contendo todas as peças.
    pecas = [I, O, Z, S, L, J, T, B]

    # Variavel que vai armazenar a pontuação ao decorrer de cada partida
    pontuacao = 0

    # Variaveis responsaveis pela escolha da peça e a sua posição na matriz.
    # A função choice faz a escolha aleatoria de peças e a função randint sorteia um numero inteiro aleatorio no intervalo definido.
    # O calculo da posição x leva em consideração a largura da peça, para que ela não saia dos limites do tabuleiro.
    peca_atual = choice(pecas)
    matriz_x = randint(0, 10 - len(peca_atual[0]))
    matriz_y = 0

    # Variaveis para cronometrar o tempo da peça cair.
    # A função perf_counter funciona como um relógio, retornando um valor em segundos fracionarios.
    tempo_inicio = perf_counter()
    tempo_fim = 0
    tempo_gravidade = 0.5
    # Variavel booleana responsavel por decidir se a peça irá descer linha por linha ou cair rapidamente.
    cair = False
    # Variavel booleana responsavel por decidir se a partida deve encerrar ou não.
    gameover = False

    # Laço de repetição principal da partida, se encerra quando é detectado colisão ao tentar inserir uma nova peça no tabuleiro
    # ou quando a variavel gameover for True.
    while not colisao(tabuleiro, peca_atual, matriz_x, matriz_y) and not gameover:
        
        # Só mostra a peça atual caindo linha por linha caso a variavel cair seja False
        if not cair:
            atualizar_tab(tabuleiro, peca_atual, matriz_x, matriz_y)

        # Looping da movimentação das peças.
        # É feito a cronometragem utilizando o calculo de variação do tempo: ∆t = tf - t0.
        # Enquanto a variação do tempo for menor que o tempo definido para a gravidade o jogador poderá mover a peça.
        while (tempo_fim - tempo_inicio) <= tempo_gravidade and not cair:
            
            # Caso a tecla de seta direita seja pressionada e não detectar colisão na próxima coluna a peça é movida para a direita.
            # Há uma espera de 0.05 segundos.
            if is_pressed('right') and not colisao(tabuleiro, peca_atual, matriz_x + 1, matriz_y):
                matriz_x += 1
                atualizar_tab(tabuleiro, peca_atual, matriz_x, matriz_y, 0.05)

            # Caso a tecla de seta esquerda seja pressionada e não detectar colisão na coluna anterior a peça é movida para a esquerda.
            # Há uma espera de 0.05 segundos.
            if is_pressed('left') and not colisao(tabuleiro, peca_atual, matriz_x - 1, matriz_y):
                matriz_x -= 1
                atualizar_tab(tabuleiro, peca_atual, matriz_x, matriz_y, 0.05)

            # Caso a tecla de seta para baixo for pressionada, e não detectar colisão na linha abaixo, a peça é desce uma linha.
            # Há uma espera de 0.05 segundos.
            if is_pressed('down') and not colisao(tabuleiro, peca_atual, matriz_x, matriz_y + 1):
                matriz_y += 1
                atualizar_tab(tabuleiro, peca_atual, matriz_x, matriz_y, 0.05)

            # Caso a tecla de seta pra cima for pressionada a função girar_peca é chamada e o tabuleiro é atualizado.
            # Há uma espera de 0.1 segundos.
            if is_pressed('up'):
                peca_atual = girar_pecas(peca_atual, tabuleiro, matriz_x, matriz_y)
                atualizar_tab(tabuleiro, peca_atual, matriz_x, matriz_y, 0.1)

            # Caso a tecla de espaço for pressionada, cair é alterado para True, sinalizando que a peça deve descer diretamente
            # até colidir com outra peça ou a base do tabuleiro.
            if is_pressed('space'):
                cair = True

            # Caso a tecla esc for pressionada gameover é alterado para True, sinalizando que deve encerrar a partida.
            if is_pressed('esc'):
                gameover = True

            # Atualiza a variavel de tempo final, para calcular a variação de tempo novamente.
            tempo_fim = perf_counter()

        
        # Caso haja colisão.
        if colisao(tabuleiro, peca_atual, matriz_x, matriz_y + 1):
            # A peça vai se fixar no tabuleiro ou caso seja uma bomba irá explodir.
            fixar_peca(tabuleiro, peca_atual, matriz_x, matriz_y)
            # Cair é atualizado para False
            cair = False
            # O tabuleiro principal é apresentado para o usuario e há uma espera de 0.3 segundos.
            atualizar(0.3, tabuleiro)
            # As linhas completas são removidas e é acrecentado á ponteação o devido valor.
            pontuacao += remover_linhas_completas(tabuleiro)
            # É sorteado uma nova peça e as cordenadas são restauradas
            peca_atual = choice(pecas)
            matriz_x = randint(0, 10 - len(peca_atual[0]))
            matriz_y = 0
            
        # Caso não haja colisão com a peça atual na linha de baixo, a coordenada Y é atualizada.
        # Ou seja, a peça atual irá descer 1 linha.
        else:
            matriz_y += 1
            
        # O tempo inicial é reiniciado para garantir uma cronometragem correta.
        tempo_inicio = perf_counter()

    # Caso o usuário perca o jogo ou decida encerra-lo, o menu é apresentado com uma mensagem de gamer over.
    # O usuário pode decidir começar outra partida ou fechar o programa.
    continuar = menu('Game Over')

# FIM DO PROGRAMA
