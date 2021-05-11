import random
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

baralho = cria_baralho()

random.shuffle(baralho)