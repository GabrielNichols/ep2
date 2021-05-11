import random

'''
Funções para criação do jogo
'''
def cria_baralho():
    naipes = ['♠','♥','♦','♣']
    valores = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    baralho = []
    for naipe in naipes:
        for valor in valores:
            baralho.append(valor+naipe)
    return baralho

def extrai_naipe(carta):
    return carta[len(carta)-1]

def extrai_valor(carta):
    if carta[1] == '0':
        return '10'
    else:
        return carta[0]

def lista_movimentos_possiveis(baralho, indice_carta):
    resultado = []
    carta = baralho[indice_carta]
    if carta == baralho[0]:
        return resultado
    
    #compara o valor e o naipe com carta anterior
    if extrai_naipe(carta) == extrai_naipe(baralho[indice_carta-1]) or extrai_valor(carta) == extrai_valor(baralho[indice_carta-1]):
        resultado.append(1)
    
    #compara valor e naipe com a terceira carta anteiror
    if indice_carta > 2:
        if extrai_naipe(carta) == extrai_naipe(baralho[indice_carta-3]) or extrai_valor(carta) == extrai_valor(baralho[indice_carta-3]):
            resultado.append(3)
    
    return resultado

def empilha(baralho,origem,destino):
    baralho[destino] = baralho[origem]
    del baralho[origem]
    return baralho

def possui_movimentos_possiveis(baralho):
    for i in range(0,len(baralho)):
        movimentos = lista_movimentos_possiveis(baralho, i)
        if len(movimentos) > 0:
            return True
    return False
'''
Paciência Acordeão - implementação do jogo

Autor: Eric Possato e Gabriel Nichols
'''
baralho = cria_baralho()

random.shuffle(baralho)

while possui_movimentos_possiveis(baralho): #repete até não haver movimentos possíveis
 
    print('O estado atual do baralho é:')
    for count, carta in enumerate(baralho, start= 1): #imprime baralho cada rodada
        print(str(count) + '.',carta)

    #pede uma carta e testa se é um valor possível
    mov_possivel = []

    while mov_possivel == []:
        
        jogada = input(f'Escolha uma carta para empilhar (1-{len(baralho)}):')
        if jogada in movimentos_legais[0:len(baralho)]: #testa validez da jogada
            jogada = int(jogada)
            jogada -= 1
            mov_possivel = lista_movimentos_possiveis(baralho, jogada)            
            if mov_possivel == []:
                print(f'A carta {baralho[jogada]} não pode ser movida')
        else:
            print(f'Posição inválida, digite um número entre 1 e {len(baralho)}')

    #empilha a carta no local adequado
    if mov_possivel == [1] or mov_possivel == [3]:
        destino = jogada - mov_possivel[0]
        baralho = empilha(baralho, jogada, destino)
    elif mov_possivel == [1,3]:
        pri_anterior = baralho[jogada-1]
        ter_anterior = baralho[jogada-3]
        (f'Sobre qual carta você quer empilhar o {jogada}?')
        print('1.',pri_anterior)
        print('2.',ter_anterior)
        
        escolha = 0
        
        while escolha != 1 and escolha != 2:
            escolha = int(input('Faça sua escolha (1-2): '))
            if escolha == 1:
                destino = jogada - 1
                baralho = empilha(baralho, jogada, destino)
            elif escolha == 2:
                destino = jogada - 3
                baralho = empilha(baralho,jogada,destino)
            else:
                print('Escolha inválida')

if len(baralho) == 1:
    print('Todas as cartas foram empilhadas\n----------Você venceu!----------')
else:
    print('Não existem mais movimentos possíveis\n----------GAME OVER----------')