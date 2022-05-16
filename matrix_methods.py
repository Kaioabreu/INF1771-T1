def get_matriz():
    mapa = open("mapa.txt","r")
    Matriz=[]
    for linha in mapa:
        row=[]
        linha=linha.strip()
        for carac in linha:
            row.append(carac)
        Matriz.append(row)
    return Matriz


def get_difficulty():
    return {"1":"10", "2":"20", "3":"30", "4":"40", "5":"50", "6":"60", "7":"70", "8":"80", "9":"90", "10":"100", "11":"110", "12":"120", "13":"130", "15":"150", "16":"160", "17":"170", "18":"180", "19":"190", "20":"200", "21":"210", "22":"220", "23":"230", "24":"240", "25":"250", "26":"260", "27":"270", "28":"280", "29":"290", "30":"300", "31":"310"}
    

def get_specific_difficulty(etapa):
    return get_difficulty()[etapa]

def get_agility():
    return {"Aang":1.8, "Zukko":1.6, "Toph":1.6, "Katara":1.6, "Sokka":1.4, "Appa":0.9, "Momo":0.7}

def get_specific_agility(personagem):
    return get_specific_agility()[personagem]

def get_tempo(dificuldade, somatorio_agilidades):
    return dificuldade/somatorio_agilidades

def get_tile_difficulty():
    return {'.':1,'R':5,'V':10,'A':15,'M':200, 'Etapa':0}