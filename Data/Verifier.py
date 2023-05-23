alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '1234567890'
plaque = {
    0: alf,
    1: alf,
    2: alf,
    3: num,
    4: alf,
    5: num,
    6: num
}
hour = {
    0: num,
    1: num,
    2: ':',
    3: num,
    4: num
}

def isPlaque(string):
    # Verificar se o formato da placa está certo
    # Exemplo: POV3L51 (AAA1A11)
    if len(string) == len(plaque):
        for index in plaque:
            if string[index] not in plaque[index]:
                return False
        return True
    return False

def isHour(string):
    # Verificar se o formato da placa está certo
    # Exemplo: 12:30
    if len(string) == len(hour):
        for index in hour:
            if string[index] not in hour[index]:
                return False
        return True
    return False