#import random
import json

mon_dictionnaire_pion = {'11': [(1, 1), False, 0],
                         '14': [(1, 4), False, 0],
                         '17': [(1, 7), False, 0],
                         '22': [(2, 2), False, 0],
                         '24': [(2, 4), False, 0],
                         '26': [(2, 6), False, 0],
                         '33': [(3, 3), False, 0],
                         '34': [(3, 4), False, 0],
                         '36': [(3, 5), False, 0],
                         '41': [(4, 1), False, 0],
                         '42': [(4, 2), False, 0],
                         '43': [(4, 3), False, 0],
                         '45': [(4, 5), False, 0],
                         '46': [(4, 6), False, 0],
                         '47': [(4, 7), False, 0],
                         '53': [(5, 3), False, 0],
                         '54': [(5, 4), False, 0],
                         '55': [(5, 5), False, 0],
                         '62': [(6, 2), False, 0],
                         '64': [(6, 4), False, 0],
                         '66': [(6, 6), False, 0],
                         '71': [(7, 1), False, 0],
                         '74': [(7, 4), False, 0],
                         '77': [(7, 7), False, 0],
                        }

class Moulin:

    """ Initialisation des attributs de ma class """
    def __init__(self):
        self.t6 = ' ———— '
        self.t8 = '   |  '
        self.esp = '      '
        self.damier = [[self.esp, self.esp, self.esp, self.esp, self.esp, self.esp, self.esp, self.esp],
                       [self.esp, (1, 1), self.t6, self.t6, (1, 4), self.t6, self.t6, (1, 7)],
                       [self.esp, self.t8, (2, 2), self.t6, (2, 4), self.t6, (2, 6), self.t8],
                       [self.esp, self.t8, self.t8, (3, 3), (3, 4), (3, 5), self.t8, self.t8],
                       [self.esp, (4, 1), (4, 2), (4, 3), self.esp, (4, 5), (4, 6), (4, 7)],
                       [self.esp, self.t8, self.t8, (5, 3), (5, 4), (5, 5), self.t8, self.t8],
                       [self.esp, self.t8, (6, 2), self.t6, (6, 4), self.t6, (6, 6), self.t8],
                       [self.esp, (7, 1), self.t6, self.t6, (7, 4), self.t6, self.t6, (7, 7)]]

        self.lp = list(range(9 * 2))
        self.R1 = False
        self.R2 = False
        self.boolRetirer = False
        # self.lp = list(range(7))
        self.p = 2
        self.player = 'R'
        self.pion_red = []
        self.pion_blue = []
        self.pionposé_damier = []
        self.couleur = ['R', 'B']
        self.moulin_déjàfait = [[]]
        self.listeM = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

        self.mon_dictionnaire_variable = {'liste de pion posé': self.pionposé_damier,
                                          'liste de pion rouge': self.pion_red,
                                          'liste de pion bleue': self.pion_blue,
                                          'listeM': self.listeM,
                                          'liste moulin utilisé': self.moulin_déjàfait,
                                          'liste de nombre de pion': self.lp,
                                          'player': self.player}

        with open('Test.json', 'w', encoding='utf-8') as f:
            json.dump(mon_dictionnaire, f, indent=4)
            json.dump(self.mon_dictionnaire_variable, f, indent=4)

    """ Representer le damier """

    def newdamier(self):
        for i in range(len(self.damier[0])):
            print(end='\n')
            for j in range(len(self.damier[0])):
                print(self.damier[i][j], end=' ')
        print()

    """ Relation entre pion-mouvement """

    def déplacement(self, X, Y):
        if (X, Y) in self.pionposé_damier:
            match X, Y:
                case 1, 1:
                    return [(1, 4), (4, 1)]
                case 1, 4:
                    return [(1, 1), (2, 4), (1, 7)]
                case 1, 7:
                    return [(1, 4), (4, 7)]
                case 2, 2:
                    return [(2, 4), (4, 2)]
                case 2, 4:
                    return [(1, 4), (2, 2), (2, 6), (3, 4)]
                case 2, 6:
                    return [(2, 4), (4, 6)]
                case 3, 3:
                    return [(3, 4), (4, 3)]
                case 3, 4:
                    return [(3, 3), (2, 4), (3, 5)]
                case 3, 5:
                    return [(3, 4), (4, 5)]
                case 4, 1:
                    return [(1, 1), (4, 2), (7, 1)]
                case 4, 2:
                    return [(4, 1), (2, 2), (4, 3), (6, 2)]
                case 4, 3:
                    return [(3, 3), (4, 2), (5, 3)]
                case 4, 5:
                    return [(3, 5), (5, 5), (4, 6)]
                case 4, 6:
                    return [(4, 5), (2, 6), (4, 7), (6, 6)]
                case 4, 7:
                    return [(1, 7), (4, 6), (7, 7)]
                case 5, 3:
                    return [(5, 4), (4, 3)]
                case 5, 4:
                    return [(5, 3), (6, 4), (5, 5)]
                case 5, 5:
                    return [(5, 4), (4, 5)]
                case 6, 2:
                    return [(6, 4), (4, 2)]
                case 6, 4:
                    return [(5, 4), (6, 6), (6, 2), (7, 4)]
                case 6, 6:
                    return [(6, 4), (4, 6)]
                case 7, 1:
                    return [(7, 4), (4, 1)]
                case 7, 4:
                    return [(7, 1), (6, 4), (7, 7)]
                case 7, 7:
                    return [(7, 4), (4, 7)]
                case _:
                    return 'relation pion damier impossible'
        else:
            print('Ce pion n existe pas sur le damier')

    """ Reconnaitre l'alignement de 3 pions par un joueur et renvoyer un bool"""
    def reconnaitre_moulin(self):
        if (self.damier[1][1] == self.damier[1][4]) and (self.damier[1][1] == self.damier[1][7]):
            return True
        if (self.damier[2][2] == self.damier[2][4]) and (self.damier[2][2] == self.damier[2][6]):
            return True
        if (self.damier[3][3] == self.damier[3][4]) and (self.damier[3][3] == self.damier[3][5]):
            return True
        if (self.damier[4][1] == self.damier[4][2]) and (self.damier[4][1] == self.damier[4][3]):
            return True
        if (self.damier[4][5] == self.damier[4][6]) and (self.damier[4][5] == self.damier[4][7]):
            return True
        if (self.damier[5][3] == self.damier[5][4]) and (self.damier[5][3] == self.damier[5][5]):
            return True
        if (self.damier[6][2] == self.damier[6][4]) and (self.damier[6][2] == self.damier[6][6]):
            return True
        if (self.damier[7][1] == self.damier[7][4]) and (self.damier[7][1] == self.damier[7][7]):
            return True
        if (self.damier[1][1] == self.damier[4][1]) and (self.damier[1][1] == self.damier[7][1]):
            return True
        if (self.damier[2][2] == self.damier[4][2]) and (self.damier[2][2] == self.damier[6][2]):
            return True
        if (self.damier[3][3] == self.damier[4][3]) and (self.damier[3][3] == self.damier[5][3]):
            return True
        if (self.damier[1][4] == self.damier[2][4]) and (self.damier[1][4] == self.damier[3][4]):
            return True
        if (self.damier[5][4] == self.damier[6][4]) and (self.damier[5][4] == self.damier[7][4]):
            return True
        if (self.damier[3][5] == self.damier[4][5]) and (self.damier[3][5] == self.damier[5][5]):
            return True
        if (self.damier[2][6] == self.damier[4][6]) and (self.damier[2][6] == self.damier[6][6]):
            return True
        if (self.damier[1][7] == self.damier[7][7]) and (self.damier[4][7] == self.damier[7][7]):
            return True
        else:
            ' Pas de nouveau moulin réalisé '
            return False

    """ Reconnaitre l'alignement de 3 pions par un joueur et renvoyer une liste """
    def moulin_renvoi_liste(self):
        if ((self.damier[1][1] == self.damier[1][4]) and (self.damier[1][1] == self.damier[1][7])):
            self.listeM[0] = [(1, 1), (1, 4), (1, 7)]
        else:
            self.listeM[0] = []
        if (self.damier[2][2] == self.damier[2][4]) and (self.damier[2][2] == self.damier[2][6]):
            self.listeM[1] = [(2, 2), (2, 4), (2, 6)]
        else:
            self.listeM[1] = []
        if (self.damier[3][3] == self.damier[3][4]) and (self.damier[3][3] == self.damier[3][5]):
            self.listeM[2] = [(3, 3), (3, 4), (3, 5)]
        else:
            self.listeM[2] = []
        if (self.damier[4][1] == self.damier[4][2]) and (self.damier[4][1] == self.damier[4][3]):
            self.listeM[3] = [(4, 1), (4, 2), (4, 3)]
        else:
            self.listeM[3] = []
        if (self.damier[4][5] == self.damier[4][6]) and (self.damier[4][5] == self.damier[4][7]):
            self.listeM[4] = [(4, 5), (4, 6), (4, 7)]
        else:
            self.listeM[4] = []
        if (self.damier[5][3] == self.damier[5][4]) and (self.damier[5][3] == self.damier[5][5]):
            self.listeM[5] = [(5, 3), (5, 4), (5, 5)]
        else:
            self.listeM[5] = []
        if (self.damier[6][2] == self.damier[6][4]) and (self.damier[6][2] == self.damier[6][6]):
            self.listeM[6] = [(6, 2), (6, 4), (6, 6)]
        else:
            self.listeM[6] = []
        if (self.damier[7][1] == self.damier[7][4]) and (self.damier[7][1] == self.damier[7][7]):
            self.listeM[7] = [(7, 1), (7, 4), (7, 7)]
        else:
            self.listeM[7] = []
        if (self.damier[1][1] == self.damier[4][1]) and (self.damier[1][1] == self.damier[7][1]):
            self.listeM[8] = [(1, 1), (4, 1), (7, 1)]
        else:
            self.listeM[8] = []
        if (self.damier[2][2] == self.damier[4][2]) and (self.damier[2][2] == self.damier[6][2]):
            self.listeM[9] = [(2, 2), (4, 2), (6, 2)]
        else:
            self.listeM[9] = []
        if (self.damier[3][3] == self.damier[4][3]) and (self.damier[3][3] == self.damier[5][3]):
            self.listeM[10] = [(3, 3), (4, 3), (5, 3)]
        else:
            self.listeM[10] = []
        if (self.damier[1][4] == self.damier[2][4]) and (self.damier[1][4] == self.damier[3][4]):
            self.listeM[11] = [(1, 4), (2, 4), (3, 4)]
        else:
            self.listeM[11] = []
        if (self.damier[5][4] == self.damier[6][4]) and (self.damier[5][4] == self.damier[7][4]):
            self.listeM[12] = [(5, 4), (6, 4), (7, 4)]
        else:
            self.listeM[12] = []
        if (self.damier[3][5] == self.damier[4][5]) and (self.damier[3][5] == self.damier[5][5]):
            self.listeM[13] = [(3, 5), (4, 5), (5, 5)]
        else:
            self.listeM[13] = []
        if (self.damier[2][6] == self.damier[4][6]) and (self.damier[2][6] == self.damier[6][6]):
            self.listeM[14] = [(2, 6), (4, 6), (6, 6)]
        else:
            self.listeM[14] = []
        if (self.damier[1][7] == self.damier[7][7]) and (self.damier[4][7] == self.damier[7][7]):
            self.listeM[15] = [(1, 7), (4, 7), (7, 7)]
        else:
            self.listeM[15] = []

    def tour_player(self):
        if self.player == 'R':
            self.player = 'B'
            return self.player
        else:
            self.player = 'R'
            return self.player

    def set_dict(self, X, Y):
        if self.p == 1:
            self.p = 2
        else:
            self.p = 1
        print(self.p)
        for key, value in mon_dictionnaire.items():
            if key == str(str(X) + str(Y)):
                mon_dictionnaire[key] = [(X, Y), True, self.p]
                return mon_dictionnaire

    def dict_reset(self, X, Y):
        for key, value in mon_dictionnaire.items():
            if key == str(str(X) + str(Y)):
                mon_dictionnaire[key] = [(X, Y), False, 0]
                return mon_dictionnaire

    """ Phase 1 : pose de pion """

    def pose(self, X, Y):
        if any((X, Y) in sub for sub in self.damier):
            # if self.pion(X, Y) in self.damier:
            self.pionposé_damier.append((X, Y))
            if self.player == self.couleur[0]:
                self.pion_red.append((X, Y))
                self.damier[X][Y] = self.couleur[0]
                print(self.damier)
            else:
                self.pion_blue.append((X, Y))
                self.damier[X][Y] = self.couleur[1]
                print(self.damier)
            self.set_dict(X, Y)
            print(mon_dictionnaire)
            print('Position du pion validé')
            print(self.tour_player())
            self.lp.pop()
            print(self.lp)
        else:
            print('Re saisir les valeurs de X et Y :')
        print(self.reconnaitre_moulin())
        print(self.newdamier())

    def mouvement(self, Xd, Yd, Xa, Ya):
        if ((Xd, Yd) in self.pionposé_damier) and (self.damier[Xd][Yd] == self.player):
            self.R2 = True
            print(self.déplacement(Xd, Yd))
            if ((Xa, Ya) in self.déplacement(Xd, Yd) or (len(self.pion_red) == 3 and self.player == 'B') or (len(self.pion_blue) == 3 and self.player == 'N')) and (Xa, Ya) not in self.pionposé_damier and self.R2 == True:
                newcouleur = self.damier[Xd][Yd]
                self.damier[Xd][Yd] = (Xd, Yd)
                self.damier[Xa][Ya] = newcouleur
                self.pionposé_damier.append((Xa, Ya))
                self.pionposé_damier.remove((Xd, Yd))
                for i in range(len(self.moulin_déjàfait)):
                    print("self.moulin_déjà_fait : ", self.moulin_déjàfait)
                    print("self.moulin_déjà_fait[i] : ", self.moulin_déjàfait[i])
                    if (Xd, Yd) in self.moulin_déjàfait[i]:
                        defait = self.moulin_déjàfait[i]
                        self.moulin_déjàfait.remove(defait)
                    else:
                        print('Ce pion ne former pas un moulin déjà utilisé')
                if newcouleur != 'R':
                    self.pion_blue.append((Xa, Ya))
                    self.pion_blue.remove((Xd, Yd))
                else:
                    self.pion_red.append((Xa, Ya))
                    self.pion_red.remove((Xd, Yd))
                self.set_dict(Xa, Ya)
                self.dict_reset(Xd, Yd)
                print(mon_dictionnaire)
                print(self.tour_player())
                print(self.newdamier())
            else:
                print('Re saisir les valeurs de X et Y à larrivée:')
        else:
            self.R2 = False
            print('Pas de pion poser ici - Re saisir les valeurs de X et Y au départ:')

    def verif_moulinfait(self):
        print(self.newdamier())
        print('Moulin déjà fait : ', self.moulin_déjàfait)
        self.moulin_renvoi_liste()
        print('listeM: ', self.listeM)
        for j in range(0, 15):
            for l in range(len(self.moulin_déjàfait)):
                print("cond", self.listeM[j] not in self.moulin_déjàfait)
                print("self.listeM", self.listeM[j] != [])
                if self.listeM[j] not in self.moulin_déjàfait and self.listeM[j] != []:
                    # print(self.listeM)
                    self.R1 = True
                    print("self.R1", self.R1)
                    print(self.pionposé_damier)
                    # for i in range(0,len(self.listeM[j])):
                    print(self.listeM)
                    self.lm = self.listeM[j]
                    self.boolRetirer = True
                else:
                    print('Aucun nouveau moulin fait')
        print("valeur de R a la fin", self.R1)

    def retirer_pion(self, Xr, Yr):
        if ((Xr, Yr) not in self.lm) and ((Xr, Yr) in self.pionposé_damier) and self.damier[Xr][Yr]==self.player:
            self.pionposé_damier.remove((Xr, Yr))
            self.damier[Xr][Yr] = (Xr, Yr)
            self.fait = self.lm
            self.moulin_déjàfait.append(self.fait)
            self.autrefait=[]
            for i in range(len(self.listeM)):
                for j in range(len(self.fait)):
                    if self.fait[j] in self.listeM[i] and self.listeM[i]!=self.fait:
                        self.autrefait=self.listeM[i]
            if self.autrefait!=[] and self.autrefait!=self.fait :
                self.moulin_déjàfait.append(self.autrefait)
            print(self.moulin_déjàfait)

            if (Xr, Yr) in self.pion_red:
                self.pion_red.remove((Xr, Yr))
            else:
                self.pion_blue.remove((Xr, Yr))
                print(self.newdamier())
            self.dict_reset(Xr, Yr)
            print(mon_dictionnaire)
            self.R1 = False
            self.boolRetirer = False
            print("NOMBRE DE PION ROUGE : ", len(self.pion_red))
            print("NOMBRE DE PION BLEUE : ", len(self.pion_blue))
        else:
            print('Moulin déja utilisé')
        print(self.newdamier())
        random.randint(2, 9)

    """def run(self):
        while True:
            if self.lp != []:
                (X, Y)=random.choice([(1, 1), (1, 4), (1, 7), (2, 2), (2, 4), (2, 6), (3, 3), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3),
                                     (4, 5), (4, 6), (4, 7), (5, 3), (5, 4), (5, 5), (6, 2),(6, 4), (6, 6), (7, 1), (7, 4), (7, 7)])
                print("------------------------------ ", (X, Y), " ------------------------------ ")
                self.pose(X, Y)
                print("valeur de R au debut", self.R1)
                self.verif_moulinfait()
                print("res : ", self.R1)
                while self.R1:
                    (Xr, Yr)=random.choice([(1, 1), (1, 4), (1, 7), (2, 2), (2, 4), (2, 6), (3, 3), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3),
                                         (4, 5), (4, 6), (4, 7), (5, 3), (5, 4), (5, 5), (6, 2),(6, 4), (6, 6), (7, 1), (7, 4), (7, 7)])
                    print("------------------------------ ", (Xr, Yr), " ------------------------------ ")
                    print("self.player: ", self.player)
                    print("self.damier[Xr][Yr]: ", self.damier[Xr][Yr])
                    if (Xr, Yr) in self.pionposé_damier and self.damier[Xr][Yr] == self.player:
                        self.retirer_pion(Xr, Yr)
                    else:
                        print("Resaisir un pion")
                print(self.newdamier())
            else:
                (Xd, Yd) = random.choice(
                    [(1, 1), (1, 4), (1, 7), (2, 2), (2, 4), (2, 6), (3, 3), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3),
                     (4, 5), (4, 6), (4, 7), (5, 3), (5, 4), (5, 5), (6, 2), (6, 4), (6, 6), (7, 1), (7, 4), (7, 7)])
                (Xa, Ya) = random.choice(
                    [(1, 1), (1, 4), (1, 7), (2, 2), (2, 4), (2, 6), (3, 3), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3),
                     (4, 5), (4, 6), (4, 7), (5, 3), (5, 4), (5, 5), (6, 2), (6, 4), (6, 6), (7, 1), (7, 4), (7, 7)])
                print("------------------------------ ", (Xd, Yd), (Xa, Ya), " ------------------------------ ")
                self.mouvement(Xd, Yd, Xa, Ya)
                print("valeur de R eu debut :", self.R1)
                self.verif_moulinfait()
                while self.R1:
                    (Xr, Yr) = random.choice(
                        [(1, 1), (1, 4), (1, 7), (2, 2), (2, 4), (2, 6), (3, 3), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3),
                         (4, 5), (4, 6), (4, 7), (5, 3), (5, 4), (5, 5), (6, 2), (6, 4), (6, 6), (7, 1), (7, 4),
                         (7, 7)])
                    print("------------------------------ ", (Xr, Yr), " ------------------------------ ")
                    if (Xr, Yr) in self.pionposé_damier and self.damier[Xr][Yr] == self.player:
                        self.retirer_pion(Xr, Yr)
                    else:
                        print("Resaisir un pion")
                    if len(self.pion_blue) == 2 or len(self.pion_red) == 2:
                        return 'Game over'
                print(self.newdamier())"""

    def run(self):
        while True:
            if self.lp != []:
                X = int(input('Entrez la valeur de X entre 1 et 7:'))
                Y = int(input('Entrez la valeur de Y entre 1 et 7:'))
                self.pose(X, Y)
                print("valeur de R au debut", self.R1)
                self.verif_moulinfait()
                print("res : ", self.R1)
                while self.R1:
                    Xr = int(input('Entrez la valeur de X du pion à retirer : '))
                    Yr = int(input('Entrez la valeur de Y du pion à retirer : '))
                    print("self.player: ", self.player)
                    print("self.damier[Xr][Yr]: ", self.damier[Xr][Yr])
                    if (Xr,Yr) in self.pionposé_damier and self.damier[Xr][Yr]==self.player :
                        self.retirer_pion(Xr, Yr)
                    else:
                        print("Resaisir un pion")
                print(self.moulin_déjàfait)

                print(self.newdamier())
            else:
                Xd = int(input('Entrez la valeur de X de départ : '))
                Yd = int(input('Entrez la valeur de Y de départ : '))
                Xa = int(input('Entrez la valeur de X à l arrivée: '))
                Ya = int(input('Entrez la valeur de Y à l arrivée: '))
                self.mouvement(Xd, Yd, Xa, Ya)
                print("valeur de R eu debut :", self.R1)
                self.verif_moulinfait()
                while self.R1:
                    Xr = int(input('Entrez la valeur de X du pion à retirer : '))
                    Yr = int(input('Entrez la valeur de Y du pion à retirer : '))
                    if (Xr, Yr) in self.pionposé_damier and self.damier[Xr][Yr]==self.player:
                        self.retirer_pion(Xr, Yr)
                    else:
                        print("Resaisir un pion")
                if len(self.pion_blue) == 2 or len(self.pion_red) == 2:
                    return 'Game over'
                print(self.newdamier())


    def save(self):
        with open('Test.json', 'w', encoding='utf-8') as f:
            json.dump(mon_dictionnaire, f)



if __name__ == "__main__":
    s = Moulin()
    s.run()
