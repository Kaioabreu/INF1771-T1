def get_matriz(file):
    mapa = open(file,"r")
    Matriz=[]
    for linha in mapa:
        row=[]
        linha=linha.strip()
        for carac in linha:
            row.append(carac)
        Matriz.append(row)
    return Matriz
    
class GameMap:
    def __init__(self, file, rows,columns):
        self.map = get_matriz(file)
        self.difficulty = {"1":"10", "2":"20", "3":"30", "4":"40", "5":"50", "6":"60", "7":"70", "8":"80", "9":"90", "10":"100", "11":"110", "12":"120", "13":"130","14":"140", "15":"150", "16":"160", "17":"170", "18":"180", "19":"190", "20":"200", "21":"210", "22":"220", "23":"230", "24":"240", "25":"250", "26":"260", "27":"270", "28":"280", "29":"290", "30":"300", "31":"310"}
        self.agility = {"Aang":1.8, "Zukko":1.6, "Toph":1.6, "Katara":1.6, "Sokka":1.4, "Appa":0.9, "Momo":0.7}
        self.ImageSize = {"Aang":(50,62),"Zukko":(50,62),"Toph":(50,62),"Katara":(50,62),"Sokka":(50,62),"Appa":(50,62),"Momo":(50,62)}
        self.tile_difficulty = {'.':1,'R':5,'V':10,'A':15,'M':200,'F':0 ,'Etapa':0}
        self.etapas = ["0","1","2","3","4","5","6","7","8","9","B","C","D","E","G","H","I","J","K","L","N","O","P","Q","S","T","U","V","W","X","Y","Z"]
        self.difficultySum = {}
        self.rows = rows
        self.columns = columns
    def setDifficultySum(self, etapa, custo):
        self.difficultySum[etapa]=custo+int(self.difficulty[str(etapa)])
    def get_difficulty(self,etapa):
        return self.difficulty[etapa]
    
    def get_agility(self):
        return self.agility
    def sortDictDifficulty(self):
        self.difficultySum=dict(sorted(self.difficultySum.items(), key=lambda item:item[1]))
    
    def get_tile_difficulty(self, x):
        if x in ".RVAMF":
            return self.tile_difficulty[x]
        return 0
    
    def get_matrix(self):
        return self.matriz
    
    def findGoal(self, goal):
        for y,row in enumerate(self.map):
            for x,item in enumerate(row):
                if(goal==item):
                    return [x,y]
        return -1
    
    def getTileType(self, x,y):
        return self.map[y][x]

    
def get_tempo(dificuldade, somatorio_agilidades):
    return dificuldade/somatorio_agilidades

