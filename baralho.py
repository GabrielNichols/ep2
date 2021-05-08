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