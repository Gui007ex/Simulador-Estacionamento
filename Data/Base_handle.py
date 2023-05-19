#Controlador da base de 26 letras (alfabeto)
alf = [l for l in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']

def LetterValue(letter):
    return alf.index(letter)

def Value(comb):
    value = 0
    pos = len(comb) - 1
    for i in range(len(comb)):
        value += LetterValue(comb[i]) * (26 ** pos)
        pos -= 1
    return value
