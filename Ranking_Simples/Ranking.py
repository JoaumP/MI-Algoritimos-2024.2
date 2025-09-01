'''
/*******************************************************************************
Autor: João Pedro da Silva Ferreira
Componente Curricular: MI - Algoritmos
Concluido em:15/09/2024
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************/
'''

# Variaveis para definir a pontuação recebida ao resolver alguma questão.
# qf = Questões faceis; qm = Questões medias; qd = Questões dificeis.
peso_faceis = float(input('Defina os pontos de uma questão fácil: '))
peso_medias = float(input('Defina os pontos de uma questão média: '))
peso_dificeis = float(input('Defina os pontos de uma questão difícil: '))

print()
print('-='*25)
print()

# Variavies para armazenar os dados das equipes
# Nome, pontuação, tempo e quantidade de questões categorizadas por tipo
nome_eq1 = nome_eq2 = nome_eq3 = nome_eq4 = nome_eq5 = ''
pontos1 = pontos2 = pontos3 = pontos4 = pontos5 = 0
tempo1 = tempo2 = tempo3 = tempo4 = tempo5 = 0
quant_q_faceis1 = quant_q_faceis2 = quant_q_faceis3 = quant_q_faceis4 = quant_q_faceis5 = 0
quant_q_medias1 = quant_q_medias2 = quant_q_medias3 = quant_q_medias4 = quant_q_medias5 =0
quant_q_dificeis1 = quant_q_dificeis2 = quant_q_dificeis3 = quant_q_dificeis4 = quant_q_dificeis5 = 0


# variavel para armazenar o maior numero de questões dificeis resolvidas
maior_dificeis = 0
# variavel para armazenar o nome da equipe que resolveu mais questões dificeis
eq_maior_dificeis = ''


# laço de repetição para auxiliar na captura dos dados das equipes e determinar sua posição no ranking
for n in range(1, 6):
    # entrada dos dados
    nome_eq = str(input(f'Nome da {n}ª equipe: ')).strip()
    quant_q_faceis = int(input('Quantidade de questões fáceis: '))
    quant_q_medias = int(input('Quantidade de questões médias: '))
    quant_q_dificeis = int(input('Quantidade de questões difíceis: '))
    tempo = float(input('Tempo levado para resolver: [Em segundos] '))
    pontos = (quant_q_faceis * peso_faceis) + (quant_q_medias * peso_medias) + (quant_q_dificeis * peso_dificeis)

    # variaveis de comparação para saber em qual posiçao a nova equipe vai se encaixar
    # a = equipe1; b = equipe2; c = equipe3; d = equipe4; e = equipe5
    a = pontos > pontos1 or pontos == pontos1 and (quant_q_dificeis > quant_q_dificeis1 or (quant_q_dificeis == quant_q_dificeis1 and tempo < tempo1))
    b = pontos > pontos2 or pontos == pontos2 and (quant_q_dificeis > quant_q_dificeis2 or (quant_q_dificeis == quant_q_dificeis2 and tempo < tempo2))
    c = pontos > pontos3 or pontos == pontos3 and (quant_q_dificeis > quant_q_dificeis3 or (quant_q_dificeis == quant_q_dificeis3 and tempo < tempo3))
    d = pontos > pontos4 or pontos == pontos4 and (quant_q_dificeis > quant_q_dificeis4 or (quant_q_dificeis == quant_q_dificeis4 and tempo < tempo4))

    # Verificando qual das sentanças são verdadeiras e ajustando o ranking
    if a:
        nome_eq5 = nome_eq4
        quant_q_faceis5 = quant_q_faceis4
        quant_q_medias5 = quant_q_medias4
        quant_q_dificeis5 = quant_q_dificeis4
        tempo5 = tempo4
        pontos5 = pontos4

        nome_eq4 = nome_eq3
        quant_q_faceis4 = quant_q_faceis3
        quant_q_medias4 = quant_q_medias3
        quant_q_dificeis4 = quant_q_dificeis3
        tempo4 = tempo3
        pontos4 = pontos3

        nome_eq3 = nome_eq2
        quant_q_faceis3 = quant_q_faceis2
        quant_q_medias3 = quant_q_medias2
        quant_q_dificeis3 = quant_q_dificeis2
        tempo3 = tempo2
        pontos3 = pontos2

        nome_eq2= nome_eq1
        quant_q_faceis2 = quant_q_faceis1
        quant_q_medias2 = quant_q_medias1
        quant_q_dificeis2 = quant_q_dificeis1
        tempo2 = tempo1
        pontos2 = pontos1

        nome_eq1 = nome_eq
        quant_q_faceis1 = quant_q_faceis
        quant_q_medias1 = quant_q_medias
        quant_q_dificeis1 = quant_q_dificeis
        tempo1 = tempo
        pontos1 = pontos
    
    elif b:
        nome_eq5 = nome_eq4
        quant_q_faceis5 = quant_q_faceis4
        quant_q_medias5 = quant_q_medias4
        quant_q_dificeis5 = quant_q_dificeis4
        tempo5 = tempo4
        pontos5 = pontos4

        nome_eq4 = nome_eq3
        quant_q_faceis4 = quant_q_faceis3
        quant_q_medias4 = quant_q_medias3
        quant_q_dificeis4 = quant_q_dificeis3
        tempo4 = tempo3
        pontos4 = pontos3

        nome_eq3 = nome_eq2
        quant_q_faceis3 = quant_q_faceis2
        quant_q_medias3 = quant_q_medias2
        quant_q_dificeis3 = quant_q_dificeis2
        tempo3 = tempo2
        pontos3 = pontos2

        nome_eq2 = nome_eq
        quant_q_faceis2 = quant_q_faceis
        quant_q_medias2 = quant_q_medias
        quant_q_dificeis2 = quant_q_dificeis
        tempo2 = tempo
        pontos2 = pontos
    
    elif c:
        nome_eq5 = nome_eq4
        quant_q_faceis5 = quant_q_faceis4
        quant_q_medias5 = quant_q_medias4
        quant_q_dificeis5 = quant_q_dificeis4
        tempo5 = tempo4
        pontos5 = pontos4

        nome_eq4 = nome_eq3
        quant_q_faceis4 = quant_q_faceis3
        quant_q_medias4 = quant_q_medias3
        quant_q_dificeis4 = quant_q_dificeis3
        tempo4 = tempo3
        pontos4 = pontos3

        nome_eq3 = nome_eq
        quant_q_faceis3 = quant_q_faceis
        quant_q_medias3 = quant_q_medias
        quant_q_dificeis3 = quant_q_dificeis
        tempo3 = tempo
        pontos3 = pontos
    
    elif d:
        nome_eq5 = nome_eq4
        quant_q_faceis5 = quant_q_faceis4
        quant_q_medias5 = quant_q_medias4
        quant_q_dificeis5 = quant_q_dificeis4
        tempo5 = tempo4
        pontos5 = pontos4

        nome_eq4 = nome_eq
        quant_q_faceis4 = quant_q_faceis
        quant_q_medias4 = quant_q_medias
        quant_q_dificeis4 = quant_q_dificeis
        tempo4 = tempo
        pontos4 = pontos

    else:
        nome_eq5 = nome_eq
        quant_q_faceis5 = quant_q_faceis
        quant_q_medias5 = quant_q_medias
        quant_q_dificeis5 = quant_q_dificeis
        tempo5 = tempo
        pontos5 = pontos

    print('-='*25)

    # comparando o numero de questoes dificeis para saber qual o maior
    if quant_q_dificeis > maior_dificeis:
        maior_dificeis = quant_q_dificeis
        eq_maior_dificeis = nome_eq


print()

# Ranking de todas as equipes, mostrando a pontuação, o numero de questoes categorizados por tipo e o tempo
# equipe1 = primeiro lugar; equipe2 = segundo lugar; equipe3 = terceiro ; equipe4 = quarto ; equipe5 = quinto
print(f'Nº {'Equipe':<20} {'Pontuação':<10} {'Q. Fáceis':<10} {'Q. Médias':<10} {'Q. Difíceis':<12} {'Tempo'}')
print('-'*75)
print(f'1º-{nome_eq1:<20} {pontos1:<10} {quant_q_faceis1:<10} {quant_q_medias1:<10} {quant_q_dificeis1:<12} {tempo1}')
print(f'2º-{nome_eq2:<20} {pontos2:<10} {quant_q_faceis2:<10} {quant_q_medias2:<10} {quant_q_dificeis2:<12} {tempo2}')
print(f'3º-{nome_eq3:<20} {pontos3:<10} {quant_q_faceis3:<10} {quant_q_medias3:<10} {quant_q_dificeis3:<12} {tempo3}')
print(f'4º-{nome_eq4:<20} {pontos4:<10} {quant_q_faceis4:<10} {quant_q_medias4:<10} {quant_q_dificeis4:<12} {tempo4}') 
print(f'5º-{nome_eq5:<20} {pontos5:<10} {quant_q_faceis5:<10} {quant_q_medias5:<10} {quant_q_dificeis5:<12} {tempo5}')

print()
print('-='*25)
print()

# mostrando a equipe vencedroa e sua pontuação
print(f'Parabéns equipe {nome_eq1}, conquistou o primeiro lugar realizando um total de {pontos1} pontos!!')

print()
print('-='*25)
print()

# equipe que resolveu a maior quantidade de questões dificeis
print(f'A equipe {eq_maior_dificeis} resolveu o maior número de questões difíceis, um total de {maior_dificeis}!!')

print()
print('-='*25)
print()

# calculo e print da media de pontos da maratona
media = (pontos1 + pontos2 + pontos3 + pontos4 + pontos5)/5
print(f'A média de pontos por equipe foi de {media}!!')

print()
print('-='*25)
print()

# o total de tempo gasto pela equipe vencedora
print(f'A equipe vencedora ({nome_eq1}) gastou um total de {tempo1} segundos!!')

print()
print('-='*25)
print()

print('FIM DO SISTEMA')
