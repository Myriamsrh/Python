import random

class Ia6:
    def __init__(self) -> None:
        self.adv = []
        self.jeuIa = []
        self.jeuIaX = []
        self.jeuIaY = []
        self.jeuxGlobal = []
        self.choixStrat = []

        self.i = 0
        #----------------------------------------
        #tableau du jeux
        #----------------------------------------
        self.choix001 = [(1, 1), (1, 4), (1, 7), (2, 2), (2, 4),
                         (2, 6), (3, 3), (3, 4), (3, 5), (4, 1), (4, 2),
                         (4, 3), (4, 5), (4, 6), (4, 7), (5, 3), (5, 4),
                         (5, 5), (6, 2), (6, 4), (6, 6), (7, 1), (7, 4),
                         (7, 7)]


    # ia.new_game(ia_first: bool) informe l'IA qu'une nouvelle partie démarre
    # ia_first vaut True si l'IA est le premier joueur, et False si le joueur humain commence.

    def new_game(self, ia_first=None):

        if ia_first == True:
            # if self.i == 0:
            self.val = 0
            print("c'est ia_first")
            
        else :
            self.val = 1
            print("c'est pas ia_first")

    # ia.player_sets(x, y, u=None, v=None) informe l'IA que le joueur humain pose un pion en
    # position(X, Y). Les paramètres(U, V) correspondent à la position du pion appartenant à l'IA et volé par
    # le joueur humain, dans le cas où un pion a été volé pendant cette phase(sinon ces paramètres valent None).

    def player_sets(self, x, y, u=None, v=None):
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        # print(x, y, u, v)

        self.adv.append((x, y))
        print("pion adv", self.adv)

    # ia.player_moves(x1, y1, x2, y2, u=None, v=None) informe l'IA que le joueur humain déplace un
    # pion de la position(X1, Y1) à la position(X2, Y2). Si la phase de saut est développée, c'est également
    # cet appel qui est utilisé. Les paramètres(U, V) correspondent à la position du pion appartenant à l'IA
    # et volé par le joueur humain, dans le cas où un pion a été volé pendant
    # cette phase(sinon ces paramètres valent None).

    def player_moves(x1, y1, x2, y2, u=None, v=None):
        pass

    # ia.play() est la fonction demandant à l'ordinateur quel est son prochain coup. La réponse peut
    # être de deux types:
    # "set", (x, y), (u, v) demande à placer un pion sur la case(X, Y) et à voler le pion en position
    # (u, v). Si aucun pion n'a été volé, alors(u, v) vaut(None, None).
    # "move", (x1, y1), (x2, y2), (u, v) demande à déplacer un pion de la case(X1, Y1) à la case
    # (X2, Y2) et à voler le pion en position(u, v). Si aucun pion n'a été volé, alors(u, v) vaut (None, None).
    # Attention: les retours de ces méthodes sont des tuples(et non une simple chaîne de
    # caractères.Par exemple "set", (x, y), (u, v) est de type tuple(str, tuple(int, int), tuple(int, int))


    # Exemples d'appels eﬀectués par le joueur humain :
    """ ia.player_sets(2, 4)  # place un pion en position (2,4)
    ia.player_sets(2, 4, 2, 2)  # place un pion en position (2,4). Ce pion forme un
    moulin et permet de voler un pion de l'IA en position (2,2). L'IA pourra
    vérifier la validité de cet appel.
    ia.player_moves(2, 4, 2, 2)  # déplace le pion (2,4) en position (2,2).
    ia.player_moves(2, 4, 2, 2, 3, 4)  # déplace le pion (2,4) en position (2,2) et
    vole un pion de l'IA en position(3, 4).
    """

    # Exemples de retours de l'IA :
    """ ia.play() -> "set", (2, 4), (None, None)  # L'IA place un pion en position (2, 4).
    ia.play() -> "set", (2, 4), (2, 2)  # L'IA place un pion en position (2,4) et
    vole un pion du joueur humain en position(2, 2).
    ia.play() -> "move", (2, 4), (2, 2)  # L'IA déplace un pion de la position (2,4)
    vers la position(2, 2).
    # L'IA déplace un pion de la position
    ia.play() -> "move", (2, 4), (2, 2), (3, 4)
    (2, 4) vers la position(2, 2) et vole un pion du joueur humain en position (3, 4). """

    def play(self):
        print("Ia joue")
        
        # scenario 0
       
        if self.i == 0:
            #----------------------------------------
            # si il joue en premier
            #----------------------------------------
            if self.val == 0:
                ch001 = random.choice(self.choix001)
                self.jeuxGlobal.append(ch001)
                self.jeuIa.append(ch001)
                print("premier tour scenario 0")
                if ch001 in self.choix001:
                    X = self.jeuIaX.append((ch001[0]))
                    Y = self.jeuIaY.append((ch001[1]))
                    print("tourIA ", self.i)
                    print("pion IA", self.jeuIa)
                    self.i += 1
            
            # -------------------------------------------------------------
            # si il joue en deuxieme
            #----------------------------------------
            if self.val == 1:
                for element in self.choix001:
                    # scenario 1
                    if self.adv == [element]:
                        if self.jeuxGlobal[:] != [element]:
                            self.jeuxGlobal.append(element)
                            ch001 = random.choice(self.choix001)
                            if ch001 == element:
                                print("le pion est deja pris")
                                ch001 = random.choice(self.choix001)
                                self.jeuxGlobal.append(ch001)
                                self.jeuIa.append(ch001)
                                print("premier tour scenario 1 variante")
                                X = self.jeuIaX.append((ch001[0]))
                                Y = self.jeuIaY.append((ch001[1]))
                                self.i += 1
                            self.jeuxGlobal.append(ch001)
                            self.jeuIa.append(ch001)
                            print("premier tour scenario 1")
                            #if ch001 in self.choix001:
                            X = self.jeuIaX.append((ch001[0]))
                            Y = self.jeuIaY.append((ch001[1]))
                            self.i += 1
                            
            #self.i += 1
        if self.i >= 1:
            #----------------------------------------
            # choix entre strategie"Moulin" et "contre" 
            # a partir du 2eme tour
            #----------------------------------------
            """ choixStrat = ["objContre", "objMoulin"]
            strat = random.choice(choixStrat)
            print("choix strat", strat) """
            
            #----------------------------------------
            # scenario 1 "Moulin" a partir du 2eme tour
            #----------------------------------------
            #if strat == "objMoulin":
                #pass
            # scenario 1.1
            """if [(7, 1), (7, 4),  (7, 7)] not in self.jeuxGlobal:
                self.jeuxGlobal.append((7, 1))
                self.jeuIa.append((7, 1))
                print("deuxieme tours ia firt ou pas scenario 1.1a ")
                X = self.jeuIaX.append(7)
                Y = self.jeuIaY.append(1)
            else:
                if [(6, 2), (6, 4),  (6, 6)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((6, 2))
                    self.jeuIa.append((6, 2))
                    print("deuxieme tours ia firt ou pas scenario 1.1b ")
                    X = self.jeuIaX.append(6)
                    Y = self.jeuIaY.append(2)
            self.i += 1

            # scenario 1.2
            if [(7, 1)] in self.jeuxGlobal:
                if [(7, 4),  (7, 7)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((7, 4))
                    self.jeuIa.append((7, 4))
                    print("deuxieme tours ia firt ou pas scenario 1.1a ")
                    X = self.jeuIaX.append(7)
                    Y = self.jeuIaY.append(4)

            # scenario 1.3
            if [(7, 1), (7, 4)] in self.jeuxGlobal:
                if [(7, 7)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((7, 7))
                    self.jeuIa.append((7, 7))
                    print("deuxieme tours ia firt ou pas scenario 1.1a ")
                    X = self.jeuIaX.append(7)
                    Y = self.jeuIaY.append(7)"""

            

            #----------------------------------------
            # scenario 1 "contre" 2eme tour
            #----------------------------------------
            #if strat == "objContre":
            # scenario 1.1
            if self.adv == [(1, 1)]:
                if [(1, 1)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((1, 1))
                print("deuxieme tours ia firt ou pas scenario 1.1 ")
                if [(4, 1)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((4, 1))
                    self.jeuIa.append((4, 1))
                    X = self.jeuIaX.append(4)
                    Y = self.jeuIaY.append(1)
                else:
                    if [(1, 4)] not in self.jeuxGlobal:
                        self.jeuxGlobal.append((1, 4))
                        self.jeuIa.append((1, 4))
                        X = self.jeuIaX.append(1)
                        Y = self.jeuIaY.append(4)
                self.i += 1
            
            # scenario 1.2
            if self.adv == [(1, 4)]:
                if [(1, 4)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((1, 4))
                print("deuxieme tours ia firt ou pas scenario 1.2 ")
                if [(1, 1)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((1, 1))
                    self.jeuIa.append((1, 1))
                    X = self.jeuIaX.append(1)
                    Y = self.jeuIaY.append(1)
                else:
                    if [(1, 7)] not in self.jeuxGlobal:
                        self.jeuxGlobal.append((1, 7))
                        self.jeuIa.append((1, 7))
                        X = self.jeuIaX.append(1)
                        Y = self.jeuIaY.append(7)
                self.i += 1

            # scenario 1.3
            if self.adv == [(1, 7)]:
                if [(1, 7)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((1, 7))
                print("deuxieme tours ia firt ou pas scenario 1.3 ")
                if [(1, 4)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((1, 4))
                    self.jeuIa.append((1, 4))
                    X = self.jeuIaX.append(1)
                    Y = self.jeuIaY.append(4)
                else:
                    if [(4, 7)] not in self.jeuxGlobal:
                        self.jeuxGlobal.append((4, 7))
                        self.jeuIa.append((4, 7))
                        X = self.jeuIaX.append(4)
                        Y = self.jeuIaY.append(7)
                self.i += 1

            # scenario 1.4
            if self.adv == [(4, 7)]:
                if [(4, 7)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((4, 7))
                print("deuxieme tours ia firt ou pas scenario 1.4 ")
                if [(1, 7)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((1, 7))
                    self.jeuIa.append((1, 7))
                    X = self.jeuIaX.append(1)
                    Y = self.jeuIaY.append(7)
                else:
                    if [(7, 7)] not in self.jeuxGlobal:
                        self.jeuxGlobal.append((7, 7))
                        self.jeuIa.append((7, 7))
                        X = self.jeuIaX.append(7)
                        Y = self.jeuIaY.append(7)
                self.i += 1

            # scenario 1.5
            if self.adv == [(7, 7)]:
                if [(7, 7)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((7, 7))
                print("deuxieme tours ia firt ou pas scenario 1.5 ")
                if [(4, 7)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((4, 7))
                    self.jeuIa.append((4, 7))
                    X = self.jeuIaX.append(4)
                    Y = self.jeuIaY.append(7)
                else:
                    if [(7, 4)] not in self.jeuxGlobal:
                        self.jeuxGlobal.append((7, 4))
                        self.jeuIa.append((7, 4))
                        X = self.jeuIaX.append(7)
                        Y = self.jeuIaY.append(4)
                self.i += 1

            # scenario 1.6
            if self.adv == [(7, 4)]:
                if [(7, 4)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((7, 4))
                print("deuxieme tours ia firt ou pas scenario 1.6 ")
                if [(7, 7)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((7, 7))
                    self.jeuIa.append((7, 7))
                    X = self.jeuIaX.append(7)
                    Y = self.jeuIaY.append(7)
                else:
                    if [(7, 1)] not in self.jeuxGlobal:
                        self.jeuxGlobal.append((7, 1))
                        self.jeuIa.append((7, 1))
                        X = self.jeuIaX.append(7)
                        Y = self.jeuIaY.append(1)
                self.i += 1

            # scenario 1.7
            if self.adv == [(7, 1)]:
                if [(7, 1)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((7, 1))
                print("deuxieme tours ia firt ou pas scenario 1.7 ")
                if [(7, 4)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((7, 4))
                    self.jeuIa.append((7, 4))
                    X = self.jeuIaX.append(7)
                    Y = self.jeuIaY.append(4)
                else:
                    if [(4, 1)] not in self.jeuxGlobal:
                        self.jeuxGlobal.append((4, 1))
                        self.jeuIa.append((4, 1))
                        X = self.jeuIaX.append(4)
                        Y = self.jeuIaY.append(1)
                self.i += 1

            # scenario 1.8
            if self.adv == [(4, 1)]:
                if [(4, 1)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((4, 1))
                print("deuxieme tours ia firt ou pas scenario 1.8 ")
                if [(7, 1)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((7, 1))
                    self.jeuIa.append((7, 1))
                    X = self.jeuIaX.append(7)
                    Y = self.jeuIaY.append(1)
                else:
                    if [(1, 1)] not in self.jeuxGlobal:
                        self.jeuxGlobal.append((1, 1))
                        self.jeuIa.append((1, 1))
                        X = self.jeuIaX.append(1)
                        Y = self.jeuIaY.append(1)
                self.i += 1

            # scenario 1.9
            if self.adv == [(2, 2)]:
                if [(2, 2)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((2, 2))
                print("deuxieme tours ia firt ou pas scenario 1.9 ")
                if [(2, 4)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((2, 4))
                    self.jeuIa.append((2, 4))
                    X = self.jeuIaX.append(2)
                    Y = self.jeuIaY.append(4)
                else:
                    if [(4, 2)] not in self.jeuxGlobal:
                        self.jeuxGlobal.append((4, 2))
                        self.jeuIa.append((4, 2))
                        X = self.jeuIaX.append(4)
                        Y = self.jeuIaY.append(2)
                self.i += 1

            # scenario 1.10
            if self.adv == [(2, 4)]:
                if [(2, 4)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((2, 4))
                print("deuxieme tours ia firt ou pas scenario 1.10 ")
                if [(2, 2)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((2, 2))
                    self.jeuIa.append((2, 2))
                    X = self.jeuIaX.append(2)
                    Y = self.jeuIaY.append(2)
                else:
                    if [(2, 6)] not in self.jeuxGlobal:
                        self.jeuxGlobal.append((2, 6))
                        self.jeuIa.append((2, 6))
                        X = self.jeuIaX.append(2)
                        Y = self.jeuIaY.append(6)
                self.i += 1

            # scenario 1.11
            if self.adv == [(2, 6)]:
                if [(2, 6)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((2, 6))
                print("deuxieme tours ia firt ou pas scenario 1.11 ")
                if [(2, 4)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((2, 4))
                    self.jeuIa.append((2, 4))
                    X = self.jeuIaX.append(2)
                    Y = self.jeuIaY.append(4)
                else:
                    if [(4, 6)] not in self.jeuxGlobal:
                        self.jeuxGlobal.append((4, 6))
                        self.jeuIa.append((4, 6))
                        X = self.jeuIaX.append(4)
                        Y = self.jeuIaY.append(6)
                self.i += 1

            # scenario 1.12
            if self.adv == [(4, 6)]:
                if [(4, 6)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((4, 6))
                print("deuxieme tours ia firt ou pas scenario 1.12 ")
                if [(2, 6)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((2, 6))
                    self.jeuIa.append((2, 6))
                    X = self.jeuIaX.append(2)
                    Y = self.jeuIaY.append(6)
                else:
                    if [(6, 6)] not in self.jeuxGlobal:
                        self.jeuxGlobal.append((6, 6))
                        self.jeuIa.append((6, 6))
                        X = self.jeuIaX.append(6)
                        Y = self.jeuIaY.append(6)
                self.i += 1

            # scenario 1.13
            if self.adv == [(6, 6)]:
                if [(6, 6)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((6, 6))
                print("deuxieme tours ia firt ou pas scenario 1.13 ")
                if [(4, 6)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((4, 6))
                    self.jeuIa.append((4, 6))
                    X = self.jeuIaX.append(4)
                    Y = self.jeuIaY.append(6)
                else:
                    if [(6, 4)] not in self.jeuxGlobal:
                        self.jeuxGlobal.append((6, 4))
                        self.jeuIa.append((6, 4))
                        X = self.jeuIaX.append(6)
                        Y = self.jeuIaY.append(4)
                self.i += 1

            # scenario 1.14
            if self.adv == [(6, 4)]:
                if [(6, 4)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((6, 4))
                print("deuxieme tours ia firt ou pas scenario 1.14 ")
                if [(6, 6)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((6, 6))
                    self.jeuIa.append((6, 6))
                    X = self.jeuIaX.append(6)
                    Y = self.jeuIaY.append(6)
                else:
                    if [(6, 2)] not in self.jeuxGlobal:
                        self.jeuxGlobal.append((6, 2))
                        self.jeuIa.append((6, 2))
                        X = self.jeuIaX.append(6)
                        Y = self.jeuIaY.append(2)
                self.i += 1

            # scenario 1.15
            if self.adv == [(6, 2)]:
                if [(6, 2)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((6, 2))
                print("deuxieme tours ia firt ou pas scenario 1.15 ")
                if [(6, 4)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((6, 4))
                    self.jeuIa.append((6, 4))
                    X = self.jeuIaX.append(6)
                    Y = self.jeuIaY.append(4)
                else:
                    if [(4, 2)] not in self.jeuxGlobal:
                        self.jeuxGlobal.append((4, 2))
                        self.jeuIa.append((4, 2))
                        X = self.jeuIaX.append(4)
                        Y = self.jeuIaY.append(2)
                self.i += 1

            # scenario 1.16
            if self.adv == [(4, 2)]:
                if [(4, 2)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((4, 2))
                print("deuxieme tours ia firt ou pas scenario 1.16 ")
                if [(6, 2)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((6, 2))
                    self.jeuIa.append((6, 2))
                    X = self.jeuIaX.append(6)
                    Y = self.jeuIaY.append(2)
                else:
                    if [(2, 2)] not in self.jeuxGlobal:
                        self.jeuxGlobal.append((2, 2))
                        self.jeuIa.append((2, 2))
                        X = self.jeuIaX.append(2)
                        Y = self.jeuIaY.append(2)
                self.i += 1

            # scenario 1.17
            if self.adv == [(3, 3)]:
                if [(3, 3)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((3, 3))
                print("deuxieme tours ia firt ou pas scenario 1.17 ")
                if [(4, 3)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((4, 3))
                    self.jeuIa.append((4, 3))
                    X = self.jeuIaX.append(4)
                    Y = self.jeuIaY.append(3)
                else:
                    if [(3, 4)] not in self.jeuxGlobal:
                        self.jeuxGlobal.append((3, 4))
                        self.jeuIa.append((3, 4))
                        X = self.jeuIaX.append(3)
                        Y = self.jeuIaY.append(4)
                self.i += 1

            # scenario 1.18
            if self.adv == [(3, 4)]:
                if [(3, 4)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((3, 4))
                print("deuxieme tours ia firt ou pas scenario 1.18 ")
                if [(3, 3)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((3, 3))
                    self.jeuIa.append((3, 3))
                    X = self.jeuIaX.append(3)
                    Y = self.jeuIaY.append(3)
                else:
                    if [(3, 5)] not in self.jeuxGlobal:
                        self.jeuxGlobal.append((3, 5))
                        self.jeuIa.append((3, 5))
                        X = self.jeuIaX.append(3)
                        Y = self.jeuIaY.append(5)
                self.i += 1

            # scenario 1.19
            if self.adv == [(3, 5)]:
                if [(3, 5)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((3, 5))
                print("deuxieme tours ia firt ou pas scenario 1.19 ")
                if [(3, 4)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((3, 4))
                    self.jeuIa.append((3, 4))
                    X = self.jeuIaX.append(3)
                    Y = self.jeuIaY.append(4)
                else:
                    if [(4, 5)] not in self.jeuxGlobal:
                        self.jeuxGlobal.append((4, 5))
                        self.jeuIa.append((4, 5))
                        X = self.jeuIaX.append(4)
                        Y = self.jeuIaY.append(5)
                self.i += 1

            # scenario 1.20
            if self.adv == [(4, 5)]:
                if [(4, 5)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((4, 5))
                print("deuxieme tours ia firt ou pas scenario 1.20 ")
                if [(3, 5)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((3, 5))
                    self.jeuIa.append((3, 5))
                    X = self.jeuIaX.append(3)
                    Y = self.jeuIaY.append(5)
                else:
                    if [(5, 5)] not in self.jeuxGlobal:
                        self.jeuxGlobal.append((5, 5))
                        self.jeuIa.append((5, 5))
                        X = self.jeuIaX.append(5)
                        Y = self.jeuIaY.append(5)
                self.i += 1

            # scenario 1.21
            if self.adv == [(5, 5)]:
                if [(5, 5)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((5, 5))
                print("deuxieme tours ia firt ou pas scenario 1.21 ")
                if [(4, 5)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((4, 5))
                    self.jeuIa.append((4, 5))
                    X = self.jeuIaX.append(4)
                    Y = self.jeuIaY.append(5)
                else:
                    if [(5, 4)] not in self.jeuxGlobal:
                        self.jeuxGlobal.append((5, 4))
                        self.jeuIa.append((5, 4))
                        X = self.jeuIaX.append(5)
                        Y = self.jeuIaY.append(4)
                self.i += 1

            # scenario 1.22
            if self.adv == [(5, 4)]:
                if [(5, 4)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((5, 4))
                print("deuxieme tours ia firt ou pas scenario 1.22 ")
                if [(5, 5)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((5, 5))
                    self.jeuIa.append((5, 5))
                    X = self.jeuIaX.append(5)
                    Y = self.jeuIaY.append(5)
                else:
                    if [(5, 3)] not in self.jeuxGlobal:
                        self.jeuxGlobal.append((5, 3))
                        self.jeuIa.append((5, 3))
                        X = self.jeuIaX.append(5)
                        Y = self.jeuIaY.append(3)
                self.i += 1

            # scenario 1.23
            if self.adv == [(5, 3)]:
                if [(5, 3)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((5, 3))
                print("deuxieme tours ia firt ou pas scenario 1.23 ")
                if [(5, 4)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((5, 4))
                    self.jeuIa.append((5, 4))
                    X = self.jeuIaX.append(5)
                    Y = self.jeuIaY.append(4)
                else:
                    if [(4, 3)] not in self.jeuxGlobal:
                        self.jeuxGlobal.append((4, 3))
                        self.jeuIa.append((4, 3))
                        X = self.jeuIaX.append(4)
                        Y = self.jeuIaY.append(3)
                self.i += 1

            # scenario 1.24
            if self.adv == [(4, 3)]:
                if [(4, 3)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((4, 3))
                print("deuxieme tours ia firt ou pas scenario 1.24 ")
                if [(5, 3)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((5, 3))
                    self.jeuIa.append((5, 3))
                    X = self.jeuIaX.append(5)
                    Y = self.jeuIaY.append(3)
                else:
                    if [(3, 3)] not in self.jeuxGlobal:
                        self.jeuxGlobal.append((3, 3))
                        self.jeuIa.append((3, 3))
                        X = self.jeuIaX.append(3)
                        Y = self.jeuIaY.append(3)
                self.i += 1

            #----------------------------------------
            # tour exterieur contre 2eme tour
            # scenario 2
            #----------------------------------------

            # scenario 2.1
            if self.adv == [(1, 1), (1, 4)]:
                if [(1, 4)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((1, 4)) #je le rentre dans ma vision du jeu global
                print("deuxieme tours ia firt ou pas scenario 2.1 ")
                self.jeuxGlobal.append((1, 7))
                self.jeuIa.append((1, 7))
                X = self.jeuIaX.append(1)
                Y = self.jeuIaY.append(7)
                self.i += 1
                
            # scenario 2.2
            if self.adv == [(1, 1), (4, 1)]:
                if [(4, 1)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((4, 1))
                print("deuxieme tours ia firt ou pas scenario 2.2 ")
                self.jeuxGlobal.append((7, 1))
                self.jeuIa.append((7, 1))
                X = self.jeuIaX.append(7)
                Y = self.jeuIaY.append(1)
                self.i += 1

            # scenario 2.3
            if self.adv == [(1, 4), (1, 1)]:
                if [(1, 1)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((1, 1))
                print("deuxieme tours ia firt ou pas scenario 2.3 ")
                self.jeuxGlobal.append((1, 7))
                self.jeuIa.append((1, 7))
                X = self.jeuIaX.append(1)
                Y = self.jeuIaY.append(7)
                self.i += 1
            
            # scenario 2.4
            if self.adv == [(1, 4), (2, 4)]:
                if [(2, 4)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((2, 4))
                print("deuxieme tours ia firt ou pas scenario 2.4 ")
                self.jeuxGlobal.append((3, 4))
                self.jeuIa.append((3, 4))
                X = self.jeuIaX.append(3)
                Y = self.jeuIaY.append(4)
                self.i += 1

            # scenario 2.5
            if self.adv == [(1, 4), (1, 7)]:
                if [(1, 7)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((1, 7))
                print("deuxieme tours ia firt ou pas scenario 2.5 ")
                self.jeuxGlobal.append((1, 1))
                self.jeuIa.append((1, 1))
                X = self.jeuIaX.append(1)
                Y = self.jeuIaY.append(1)
                self.i += 1
            
            # scenario 2.6
            if self.adv == [(1, 7), (1, 4)]:
                if [(1, 4)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((1, 4))
                print("deuxieme tours ia firt ou pas scenario 2.6 ")
                self.jeuxGlobal.append((1, 1))
                self.jeuIa.append((1, 1))
                X = self.jeuIaX.append(1)
                Y = self.jeuIaY.append(1)
                self.i += 1

            # scenario 2.7
            if self.adv == [(1, 7), (4, 7)]:
                if [(4, 7)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((4, 7))
                print("deuxieme tours ia firt ou pas scenario 2.7 ")
                self.jeuxGlobal.append((7, 7))
                self.jeuIa.append((7, 7))
                X = self.jeuIaX.append(7)
                Y = self.jeuIaY.append(7)
                self.i += 1

            # scenario 2.8
            if self.adv == [(4, 7), (1, 7)]:
                if [(1, 7)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((1, 7))
                print("deuxieme tours ia firt ou pas scenario 2.8 ")
                self.jeuxGlobal.append((7, 7))
                self.jeuIa.append((7, 7))
                X = self.jeuIaX.append(7)
                Y = self.jeuIaY.append(7)
                self.i += 1

            # scenario 2.9
            if self.adv == [(4, 7), (4, 6)]:
                if [(4, 6)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((4, 6))
                print("deuxieme tours ia firt ou pas scenario 2.9 ")
                self.jeuxGlobal.append((4, 5))
                self.jeuIa.append((4, 5))
                X = self.jeuIaX.append(4)
                Y = self.jeuIaY.append(5)
                self.i += 1

            # scenario 2.10
            if self.adv == [(4, 7), (7, 7)]:
                if [(7, 7)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((7, 7))
                print("deuxieme tours ia firt ou pas scenario 2.10 ")
                self.jeuxGlobal.append((1, 7))
                self.jeuIa.append((1, 7))
                X = self.jeuIaX.append(1)
                Y = self.jeuIaY.append(7)
                self.i += 1

            # scenario 2.11
            if self.adv == [(7, 7), (4, 7)]:
                if [(4, 7)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((4, 7))
                print("deuxieme tours ia firt ou pas scenario 2.11 ")
                self.jeuxGlobal.append((1, 7))
                self.jeuIa.append((1, 7))
                X = self.jeuIaX.append(1)
                Y = self.jeuIaY.append(7)
                self.i += 1

            # scenario 2.12
            if self.adv == [(7, 7), (7, 4)]:
                if [(7, 4)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((7, 4))
                print("deuxieme tours ia firt ou pas scenario 2.12 ")
                self.jeuxGlobal.append((7, 1))
                self.jeuIa.append((7, 1))
                X = self.jeuIaX.append(7)
                Y = self.jeuIaY.append(1)
                self.i += 1

            # scenario 2.13
            if self.adv == [(7, 4), (7, 7)]:
                if [(7, 7)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((7, 7))
                print("deuxieme tours ia firt ou pas scenario 2.13 ")
                self.jeuxGlobal.append((7, 1))
                self.jeuIa.append((7, 1))
                X = self.jeuIaX.append(7)
                Y = self.jeuIaY.append(1)
                self.i += 1

            # scenario 2.14
            if self.adv == [(7, 4), (6, 4)]:
                if [(6, 4)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((6, 4))
                print("deuxieme tours ia firt ou pas scenario 2.14 ")
                self.jeuxGlobal.append((5, 4))
                self.jeuIa.append((5, 4))
                X = self.jeuIaX.append(5)
                Y = self.jeuIaY.append(4)
                self.i += 1

            # scenario 2.15
            if self.adv == [(7, 4), (7, 1)]:
                if [(7, 1)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((7, 1))
                print("deuxieme tours ia firt ou pas scenario 2.15 ")
                self.jeuxGlobal.append((7, 7))
                self.jeuIa.append((7, 7))
                X = self.jeuIaX.append(7)
                Y = self.jeuIaY.append(7)
                self.i += 1

            # scenario 2.16
            if self.adv == [(7, 1), (7, 4)]:
                if [(7, 1)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((7, 1))
                print("deuxieme tours ia firt ou pas scenario 2.16 ")
                self.jeuxGlobal.append((7, 7))
                self.jeuIa.append((7, 7))
                X = self.jeuIaX.append(7)
                Y = self.jeuIaY.append(7)
                self.i += 1

            # scenario 2.17
            if self.adv == [(7, 1), (4, 1)]:
                if [(4, 1)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((4, 1))
                print("deuxieme tours ia firt ou pas scenario 2.17 ")
                self.jeuxGlobal.append((1, 1))
                self.jeuIa.append((1, 1))
                X = self.jeuIaX.append(1)
                Y = self.jeuIaY.append(1)
                self.i += 1

            # scenario 2.18
            if self.adv == [(4, 1), (7, 1)]:
                if [(7, 1)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((7, 1))
                print("deuxieme tours ia firt ou pas scenario 2.18 ")
                self.jeuxGlobal.append((1, 1))
                self.jeuIa.append((1, 1))
                X = self.jeuIaX.append(1)
                Y = self.jeuIaY.append(1)
                self.i += 1

            # scenario 2.19
            if self.adv == [(4, 1), (4, 2)]:
                if [(4, 2)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((4, 2))
                print("deuxieme tours ia firt ou pas scenario 2.19 ")
                self.jeuxGlobal.append((4, 3))
                self.jeuIa.append((4, 3))
                X = self.jeuIaX.append(4)
                Y = self.jeuIaY.append(3)
                self.i += 1

            # scenario 2.20
            if self.adv == [(4, 1), (1, 1)]:
                if [(1, 1)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((1, 1))
                print("deuxieme tours ia firt ou pas scenario 2.19 ")
                self.jeuxGlobal.append((7, 1))
                self.jeuIa.append((7, 1))
                X = self.jeuIaX.append(7)
                Y = self.jeuIaY.append(1)
                self.i += 1
            
            #----------------------------------------
            # tour central contre 2eme tour
            # scenario 3
            #----------------------------------------
            
            # scenario 3.1
            if self.adv == [(2, 2), (2, 4)]:
                if [(2, 4)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((2, 4))
                print("deuxieme tours ia firt ou pas scenario 3.1 ")
                self.jeuxGlobal.append((2, 6))
                self.jeuIa.append((2, 6))
                X = self.jeuIaX.append(2)
                Y = self.jeuIaY.append(6)
                self.i += 1

            # scenario 3.2
            if self.adv == [(2, 2), (4, 2)]:
                if [(4, 2)] not in self.jeuxGlobal:
                    self.jeuxGlobal.append((4, 2))
                print("deuxieme tours ia firt ou pas scenario 3.2 ")
                self.jeuxGlobal.append((6, 2))
                self.jeuIa.append((6, 2))
                X = self.jeuIaX.append(6)
                Y = self.jeuIaY.append(2)
                self.i += 1

            # scenario 3.3
            if self.adv == [(2, 4), (2, 2)]:
                pass  # TO DO
            if self.adv == [(2, 4), (3, 4)]:
                pass  # TO DO
            if self.adv == [(2, 4), (1, 4)]:
                pass  # TO DO
            if self.adv == [(2, 4), (2, 6)]:
                pass  # TO DO
            if self.adv == [(2, 6), (2, 4)]:
                pass  # TO DO
            if self.adv == [(2, 6), (4, 6)]:
                pass  # TO DO
            if self.adv == [(4, 6), (2, 6)]:
                pass  # TO DO
            if self.adv == [(4, 6), (4, 5)]:
                pass  # TO DO
            if self.adv == [(4, 6), (4, 7)]:
                pass  # TO DO
            if self.adv == [(4, 6), (6, 6)]:
                pass  # TO DO
            if self.adv == [(6, 6), (4, 6)]:
                pass  # TO DO
            if self.adv == [(6, 6), (6, 4)]:
                pass  # TO DO
            if self.adv == [(6, 4), (6, 6)]:
                pass  # TO DO
            if self.adv == [(6, 4), (5, 4)]:
                pass  # TO DO
            if self.adv == [(6, 4), (7, 4)]:
                pass  # TO DO
            if self.adv == [(6, 4), (6, 2)]:
                pass  # TO DO
            if self.adv == [(6, 2), (6, 4)]:
                pass  # TO DO
            if self.adv == [(6, 2), (4, 2)]:
                pass  # TO DO
            if self.adv == [(4, 2), (6, 2)]:
                pass  # TO DO
            if self.adv == [(4, 2), (4, 1)]:
                pass  # TO DO
            if self.adv == [(4, 2), (4, 3)]:
                pass  # TO DO
            if self.adv == [(4, 2), (2, 2)]:
                pass  # TO DO
            
            #----------------------------------------
            # tour central contre 2eme tour
            # scenario 4
            #----------------------------------------

            # tour interieur
            if self.adv == [(3, 3), (3, 4)]:
                pass  # TO DO
            if self.adv == [(3, 3), (4, 3)]:
                pass  # TO DO
            if self.adv == [(3, 4), (3, 3)]:
                pass  # TO DO
            if self.adv == [(3, 4), (2, 4)]:
                pass  # TO DO
            if self.adv == [(3, 4), (3, 5)]:
                pass  # TO DO
            if self.adv == [(3, 5), (3, 4)]:
                pass  # TO DO
            if self.adv == [(3, 5), (4, 5)]:
                pass  # TO DO
            if self.adv == [(4, 5), (3, 5)]:
                pass  # TO DO
            if self.adv == [(4, 5), (4, 6)]:
                pass  # TO DO
            if self.adv == [(4, 5), (5, 5)]:
                pass  # TO DO
            if self.adv == [(5, 5), (4, 5)]:
                pass  # TO DO
            if self.adv == [(5, 5), (5, 4)]:
                pass  # TO DO
            if self.adv == [(5, 4), (5, 5)]:
                pass  # TO DO
            if self.adv == [(5, 4), (6, 4)]:
                pass  # TO DO
            if self.adv == [(5, 4), (5, 3)]:
                pass  # TO DO
            if self.adv == [(5, 3), (5, 4)]:
                pass  # TO DO
            if self.adv == [(5, 3), (4, 3)]:
                pass  # TO DO
            if self.adv == [(4, 3), (5, 3)]:
                pass  # TO DO
            if self.adv == [(4, 3), (4, 2)]:
                pass  # TO DO
            if self.adv == [(4, 3), (3, 3)]:
                pass  # TO DO

            #----------------------------------------
            # tour contre 2eme tour
            # scenario transverse si adv fait autre chose
            #----------------------------------------
            
            # si 1,1
            if self.adv == [(1, 1), (1, 7)]:
                pass  # TO DO

            if self.adv == [(1, 1), (4, 7)]:
                pass  # TO DO

            if self.adv == [(1, 1), (7, 7)]:
                pass  # TO DO

            if self.adv == [(1, 1), (7, 4)]:
                pass  # TO DO

            if self.adv == [(1, 1), (7, 1)]:
                pass  # TO DO

            if self.adv == [(1, 1), (2, 2)]:
                pass  # TO DO

            if self.adv == [(1, 1), (2, 4)]:
                pass  # TO DO

            if self.adv == [(1, 1), (2, 6)]:
                pass  # TO DO

            if self.adv == [(1, 1), (4, 6)]:
                pass  # TO DO

            if self.adv == [(1, 1), (6, 6)]:
                pass  # TO DO

            if self.adv == [(1, 1), (6, 4)]:
                pass  # TO DO

            if self.adv == [(1, 1), (6, 2)]:
                pass  # TO DO

            if self.adv == [(1, 1), (4, 2)]:
                pass  # TO DO

            if self.adv == [(1, 1), (3, 3)]:
                pass  # TO DO

            if self.adv == [(1, 1), (3, 4)]:
                pass  # TO DO

            if self.adv == [(1, 1), (3, 5)]:
                pass  # TO DO

            if self.adv == [(1, 1), (4, 5)]:
                pass  # TO DO

            if self.adv == [(1, 1), (5, 5)]:
                pass  # TO DO

            if self.adv == [(1, 1), (5, 4)]:
                pass  # TO DO

            if self.adv == [(1, 1), (5, 3)]:
                pass  # TO DO

            if self.adv == [(1, 1), (4, 3)]:
                pass  # TO DO


            # si 1,4
            if self.adv == [(1, 4), (4, 7)]:
                pass  # TO DO

            if self.adv == [(1, 4), (7, 7)]:
                pass  # TO DO

            if self.adv == [(1, 4), (7, 4)]:
                pass  # TO DO

            if self.adv == [(1, 4), (7, 1)]:
                pass  # TO DO

            if self.adv == [(1, 4), (4, 1)]:
                pass  # TO DO

            if self.adv == [(1, 4), (2, 2)]:
                pass  # TO DO

            if self.adv == [(1, 4), (2, 6)]:
                pass  # TO DO

            if self.adv == [(1, 4), (4, 6)]:
                pass  # TO DO

            if self.adv == [(1, 4), (6, 6)]:
                pass  # TO DO

            if self.adv == [(1, 4), (6, 4)]:
                pass  # TO DO

            if self.adv == [(1, 4), (6, 2)]:
                pass  # TO DO

            if self.adv == [(1, 4), (4, 2)]:
                pass  # TO DO

            if self.adv == [(1, 4), (3, 3)]:
                pass  # TO DO

            if self.adv == [(1, 4), (3, 4)]:
                pass  # TO DO

            if self.adv == [(1, 4), (3, 5)]:
                pass  # TO DO

            if self.adv == [(1, 4), (4, 5)]:
                pass  # TO DO

            if self.adv == [(1, 4), (5, 5)]:
                pass  # TO DO

            if self.adv == [(1, 4), (5, 4)]:
                pass  # TO DO

            if self.adv == [(1, 4), (5, 3)]:
                pass  # TO DO

            if self.adv == [(1, 4), (4, 3)]:
                pass  # TO DO


            # si 1,7
            if self.adv == [(1, 7), (1, 1)]:
                pass  # TO DO

            if self.adv == [(1, 7), (7, 7)]:
                pass  # TO DO

            if self.adv == [(1, 7), (7, 4)]:
                pass  # TO DO

            if self.adv == [(1, 7), (7, 1)]:
                pass  # TO DO

            if self.adv == [(1, 7), (4, 1)]:
                pass  # TO DO

            if self.adv == [(1, 7), (2, 2)]:
                pass  # TO DO

            if self.adv == [(1, 7), (2, 4)]:
                pass  # TO DO

            if self.adv == [(1, 7), (2, 6)]:
                pass  # TO DO

            if self.adv == [(1, 7), (4, 6)]:
                pass  # TO DO

            if self.adv == [(1, 7), (6, 6)]:
                pass  # TO DO

            if self.adv == [(1, 7), (6, 4)]:
                pass  # TO DO

            if self.adv == [(1, 7), (6, 2)]:
                pass  # TO DO

            if self.adv == [(1, 7), (4, 2)]:
                pass  # TO DO

            if self.adv == [(1, 7), (3, 3)]:
                pass  # TO DO

            if self.adv == [(1, 7), (3, 4)]:
                pass  # TO DO

            if self.adv == [(1, 7), (3, 5)]:
                pass  # TO DO

            if self.adv == [(1, 7), (4, 5)]:
                pass  # TO DO

            if self.adv == [(1, 7), (5, 5)]:
                pass  # TO DO

            if self.adv == [(1, 7), (5, 4)]:
                pass  # TO DO

            if self.adv == [(1, 7), (5, 3)]:
                pass  # TO DO

            if self.adv == [(1, 7), (4, 3)]:
                pass  # TO DO


            # si 4,7
            if self.adv == [(4, 7), (1, 1)]:
                pass  # TO DO

            if self.adv == [(4, 7), (1, 4)]:
                pass  # TO DO

            if self.adv == [(4, 7), (7, 4)]:
                pass  # TO DO

            if self.adv == [(4, 7), (7, 1)]:
                pass  # TO DO

            if self.adv == [(4, 7), (4, 1)]:
                pass  # TO DO

            if self.adv == [(4, 7), (2, 2)]:
                pass  # TO DO

            if self.adv == [(4, 7), (2, 4)]:
                pass  # TO DO

            if self.adv == [(4, 7), (2, 6)]:
                pass  # TO DO

            if self.adv == [(4, 7), (6, 6)]:
                pass  # TO DO

            if self.adv == [(4, 7), (6, 4)]:
                pass  # TO DO

            if self.adv == [(4, 7), (6, 2)]:
                pass  # TO DO

            if self.adv == [(4, 7), (4, 2)]:
                pass  # TO DO

            if self.adv == [(4, 7), (3, 3)]:
                pass  # TO DO

            if self.adv == [(4, 7), (3, 4)]:
                pass  # TO DO

            if self.adv == [(4, 7), (3, 5)]:
                pass  # TO DO

            if self.adv == [(4, 7), (4, 5)]:
                pass  # TO DO

            if self.adv == [(4, 7), (5, 5)]:
                pass  # TO DO

            if self.adv == [(4, 7), (5, 4)]:
                pass  # TO DO

            if self.adv == [(4, 7), (5, 3)]:
                pass  # TO DO

            if self.adv == [(4, 7), (4, 3)]:
                pass  # TO DO


            # si 7,7
            if self.adv == [(7, 7), (1, 1)]:
                pass  # TO DO

            if self.adv == [(7, 7), (1, 4)]:
                pass  # TO DO

            if self.adv == [(7, 7), (1, 7)]:
                pass  # TO DO

            if self.adv == [(7, 7), (7, 1)]:
                pass  # TO DO

            if self.adv == [(7, 7), (4, 1)]:
                pass  # TO DO

            if self.adv == [(7, 7), (2, 2)]:
                pass  # TO DO

            if self.adv == [(7, 7), (2, 4)]:
                pass  # TO DO

            if self.adv == [(7, 7), (2, 6)]:
                pass  # TO DO

            if self.adv == [(7, 7), (4, 6)]:
                pass  # TO DO

            if self.adv == [(7, 7), (6, 6)]:
                pass  # TO DO

            if self.adv == [(7, 7), (6, 4)]:
                pass  # TO DO

            if self.adv == [(7, 7), (6, 2)]:
                pass  # TO DO

            if self.adv == [(7, 7), (4, 2)]:
                pass  # TO DO

            if self.adv == [(7, 7), (3, 3)]:
                pass  # TO DO

            if self.adv == [(7, 7), (3, 4)]:
                pass  # TO DO

            if self.adv == [(7, 7), (3, 5)]:
                pass  # TO DO

            if self.adv == [(7, 7), (4, 5)]:
                pass  # TO DO

            if self.adv == [(7, 7), (5, 5)]:
                pass  # TO DO

            if self.adv == [(7, 7), (5, 4)]:
                pass  # TO DO

            if self.adv == [(7, 7), (5, 3)]:
                pass  # TO DO

            if self.adv == [(7, 7), (4, 3)]:
                pass  # TO DO


            # si 7,4
            if self.adv == [(7, 4), (1, 1)]:
                pass  # TO DO

            if self.adv == [(7, 4), (1, 4)]:
                pass  # TO DO

            if self.adv == [(7, 4), (1, 7)]:
                pass  # TO DO

            if self.adv == [(7, 4), (4, 7)]:
                pass  # TO DO

            if self.adv == [(7, 4), (4, 1)]:
                pass  # TO DO

            if self.adv == [(7, 4), (2, 2)]:
                pass  # TO DO

            if self.adv == [(7, 4), (2, 4)]:
                pass  # TO DO

            if self.adv == [(7, 4), (2, 6)]:
                pass  # TO DO

            if self.adv == [(7, 4), (4, 6)]:
                pass  # TO DO

            if self.adv == [(7, 4), (6, 6)]:
                pass  # TO DO

            if self.adv == [(7, 4), (6, 2)]:
                pass  # TO DO

            if self.adv == [(7, 4), (4, 2)]:
                pass  # TO DO

            if self.adv == [(7, 4), (3, 3)]:
                pass  # TO DO

            if self.adv == [(7, 4), (3, 4)]:
                pass  # TO DO

            if self.adv == [(7, 4), (3, 5)]:
                pass  # TO DO

            if self.adv == [(7, 4), (4, 5)]:
                pass  # TO DO

            if self.adv == [(7, 4), (5, 5)]:
                pass  # TO DO

            if self.adv == [(7, 4), (5, 4)]:
                pass  # TO DO

            if self.adv == [(7, 4), (5, 3)]:
                pass  # TO DO

            if self.adv == [(7, 4), (4, 3)]:
                pass  # TO DO

            
            # si 7,1
            if self.adv == [(7, 1), (1, 1)]:
                pass  # TO DO

            if self.adv == [(7, 1), (1, 4)]:
                pass  # TO DO

            if self.adv == [(7, 1), (1, 7)]:
                pass  # TO DO

            if self.adv == [(7, 1), (4, 7)]:
                pass  # TO DO

            if self.adv == [(7, 1), (7, 7)]:
                pass  # TO DO

            if self.adv == [(7, 1), (2, 2)]:
                pass  # TO DO

            if self.adv == [(7, 1), (2, 4)]:
                pass  # TO DO

            if self.adv == [(7, 1), (2, 6)]:
                pass  # TO DO

            if self.adv == [(7, 1), (4, 6)]:
                pass  # TO DO

            if self.adv == [(7, 1), (6, 6)]:
                pass  # TO DO

            if self.adv == [(7, 1), (6, 4)]:
                pass  # TO DO

            if self.adv == [(7, 1), (6, 2)]:
                pass  # TO DO

            if self.adv == [(7, 1), (4, 2)]:
                pass  # TO DO

            if self.adv == [(7, 1), (3, 3)]:
                pass  # TO DO

            if self.adv == [(7, 1), (3, 4)]:
                pass  # TO DO

            if self.adv == [(7, 1), (3, 5)]:
                pass  # TO DO

            if self.adv == [(7, 1), (4, 5)]:
                pass  # TO DO

            if self.adv == [(7, 1), (5, 5)]:
                pass  # TO DO

            if self.adv == [(7, 1), (5, 4)]:
                pass  # TO DO

            if self.adv == [(7, 1), (5, 3)]:
                pass  # TO DO

            if self.adv == [(7, 1), (4, 3)]:
                pass  # TO DO


            # si 4,1
            if self.adv == [(4, 1), (1, 4)]:
                pass  # TO DO

            if self.adv == [(4, 1), (1, 7)]:
                pass  # TO DO

            if self.adv == [(4, 1), (4, 7)]:
                pass  # TO DO

            if self.adv == [(4, 1), (7, 7)]:
                pass  # TO DO

            if self.adv == [(4, 1), (7, 4)]:
                pass  # TO DO

            if self.adv == [(4, 1), (2, 2)]:
                pass  # TO DO

            if self.adv == [(4, 1), (2, 4)]:
                pass  # TO DO

            if self.adv == [(4, 1), (2, 6)]:
                pass  # TO DO

            if self.adv == [(4, 1), (4, 6)]:
                pass  # TO DO

            if self.adv == [(4, 1), (6, 6)]:
                pass  # TO DO

            if self.adv == [(4, 1), (6, 4)]:
                pass  # TO DO

            if self.adv == [(4, 1), (6, 2)]:
                pass  # TO DO

            if self.adv == [(4, 1), (3, 3)]:
                pass  # TO DO

            if self.adv == [(4, 1), (3, 4)]:
                pass  # TO DO

            if self.adv == [(4, 1), (3, 5)]:
                pass  # TO DO

            if self.adv == [(4, 1), (4, 5)]:
                pass  # TO DO

            if self.adv == [(4, 1), (5, 5)]:
                pass  # TO DO

            if self.adv == [(4, 1), (5, 4)]:
                pass  # TO DO

            if self.adv == [(4, 1), (5, 3)]:
                pass  # TO DO

            if self.adv == [(4, 1), (4, 3)]:
                pass  # TO DO

            
            # si 2,2
            if self.adv == [(2, 2), (1, 1)]:
                pass  # TO DO

            if self.adv == [(2, 2), (1, 4)]:
                pass  # TO DO

            if self.adv == [(2, 2), (1, 7)]:
                pass  # TO DO

            if self.adv == [(2, 2), (4, 7)]:
                pass  # TO DO

            if self.adv == [(2, 2), (7, 7)]:
                pass  # TO DO

            if self.adv == [(2, 2), (7, 4)]:
                pass  # TO DO

            if self.adv == [(2, 2), (7, 1)]:
                pass  # TO DO

            if self.adv == [(2, 2), (4, 1)]:
                pass  # TO DO

            if self.adv == [(2, 2), (2, 6)]:
                pass  # TO DO

            if self.adv == [(2, 2), (4, 6)]:
                pass  # TO DO

            if self.adv == [(2, 2), (6, 6)]:
                pass  # TO DO

            if self.adv == [(2, 2), (6, 4)]:
                pass  # TO DO

            if self.adv == [(2, 2), (6, 2)]:
                pass  # TO DO

            if self.adv == [(2, 2), (3, 3)]:
                pass  # TO DO

            if self.adv == [(2, 2), (3, 4)]:
                pass  # TO DO

            if self.adv == [(2, 2), (3, 5)]:
                pass  # TO DO

            if self.adv == [(2, 2), (4, 5)]:
                pass  # TO DO

            if self.adv == [(2, 2), (5, 5)]:
                pass  # TO DO

            if self.adv == [(2, 2), (5, 4)]:
                pass  # TO DO

            if self.adv == [(2, 2), (5, 3)]:
                pass  # TO DO

            if self.adv == [(2, 2), (4, 3)]:
                pass  # TO DO

            # si 2,4
            if self.adv == [(2, 4), (1, 1)]:
                pass  # TO DO

            if self.adv == [(2, 4), (1, 7)]:
                pass  # TO DO

            if self.adv == [(2, 4), (4, 7)]:
                pass  # TO DO

            if self.adv == [(2, 4), (7, 7)]:
                pass  # TO DO

            if self.adv == [(2, 4), (7, 4)]:
                pass  # TO DO

            if self.adv == [(2, 4), (7, 1)]:
                pass  # TO DO

            if self.adv == [(2, 4), (4, 1)]:
                pass  # TO DO

            if self.adv == [(2, 4), (4, 6)]:
                pass  # TO DO

            if self.adv == [(2, 4), (6, 6)]:
                pass  # TO DO

            if self.adv == [(2, 4), (6, 4)]:
                pass  # TO DO

            if self.adv == [(2, 4), (6, 2)]:
                pass  # TO DO

            if self.adv == [(2, 4), (4, 2)]:
                pass  # TO DO

            if self.adv == [(2, 4), (3, 3)]:
                pass  # TO DO

            if self.adv == [(2, 4), (3, 5)]:
                pass  # TO DO

            if self.adv == [(2, 4), (4, 5)]:
                pass  # TO DO

            if self.adv == [(2, 4), (5, 5)]:
                pass  # TO DO

            if self.adv == [(2, 4), (5, 4)]:
                pass  # TO DO

            if self.adv == [(2, 4), (5, 3)]:
                pass  # TO DO

            if self.adv == [(2, 4), (4, 3)]:
                pass  # TO DO

            
            # si 2,6
            if self.adv == [(2, 6), (1, 1)]:
                pass  # TO DO

            if self.adv == [(2, 6), (1, 4)]:
                pass  # TO DO

            if self.adv == [(2, 6), (1, 7)]:
                pass  # TO DO

            if self.adv == [(2, 6), (4, 7)]:
                pass  # TO DO

            if self.adv == [(2, 6), (7, 7)]:
                pass  # TO DO

            if self.adv == [(2, 6), (7, 4)]:
                pass  # TO DO

            if self.adv == [(2, 6), (7, 1)]:
                pass  # TO DO

            if self.adv == [(2, 6), (4, 1)]:
                pass  # TO DO

            if self.adv == [(2, 6), (2, 2)]:
                pass  # TO DO

            if self.adv == [(2, 6), (6, 6)]:
                pass  # TO DO

            if self.adv == [(2, 6), (6, 4)]:
                pass  # TO DO

            if self.adv == [(2, 6), (6, 2)]:
                pass  # TO DO

            if self.adv == [(2, 6), (4, 2)]:
                pass  # TO DO

            if self.adv == [(2, 6), (3, 3)]:
                pass  # TO DO

            if self.adv == [(2, 6), (3, 4)]:
                pass  # TO DO

            if self.adv == [(2, 6), (3, 5)]:
                pass  # TO DO

            if self.adv == [(2, 6), (4, 5)]:
                pass  # TO DO

            if self.adv == [(2, 6), (5, 5)]:
                pass  # TO DO

            if self.adv == [(2, 6), (5, 4)]:
                pass  # TO DO

            if self.adv == [(2, 6), (5, 3)]:
                pass  # TO DO

            if self.adv == [(2, 6), (4, 3)]:
                pass  # TO DO

            
            # si 4,6
            if self.adv == [(4, 6), (1, 1)]:
                pass  # TO DO
            # si 6,6
            # si 6,4
            # si 6,2
            # si 4,2
            # si 3,3
            # si 3,4
            # si 3,5
            # si 4,5
            # si 5,5
            # si 5,4
            # si 5,3
            # si 4,3


            

            


            
            print("fin deuxieme tour") 
            #----------------------------------------
            # tour contre 3eme tour
            # scenario 1
            #----------------------------------------
            # TO DO
            


            #----------------------------------------
            # tour contre 4eme tour
            # scenario 1
            #----------------------------------------
            # TO DO
            

            #----------------------------------------
            # tour contre 5eme tour
            # scenario 1
            #----------------------------------------
            # TO DO


            #----------------------------------------
            # tour contre 6eme tour
            # scenario 1
            #----------------------------------------
            # TO DO


            #----------------------------------------
            # tour contre 7eme tour
            # scenario 1
            #----------------------------------------
            # TO DO


            #----------------------------------------
            # tour contre 8eme tour
            # scenario 1
            #----------------------------------------
            # TO DO


            #----------------------------------------
            # tour contre 9eme tour
            # scenario 1
            #----------------------------------------
            # TO DO
        