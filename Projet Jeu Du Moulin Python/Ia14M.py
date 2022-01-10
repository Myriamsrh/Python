import random

class Ia14M:
    def __init__(self) -> None:
        self.adv = []
        self.advX = []
        self.advY = []
        self.jeuIa = []
        self.jeuIaX = []
        self.jeuIaY = []
        self.jeuxGlobal = []
        self.choixStrat = []
        self.x = []
        self.y = []
        self.u = []
        self.v = []

        self.i = 0
        #self.val = 0
        #----------------------------------------
        #tableau du jeux
        #----------------------------------------
        self.choix001 = [(1, 1), (1, 4), (1, 7), (2, 2), (2, 4),
                         (2, 6), (3, 3), (3, 4), (3, 5), (4, 1), (4, 2),
                         (4, 3), (4, 5), (4, 6), (4, 7), (5, 3), (5, 4),
                         (5, 5), (6, 2), (6, 4), (6, 6), (7, 1), (7, 4),
                         (7, 7)]
        
        self.choix002 = [(1, 7), (7, 1), (6, 2)]

    # ia.new_game(ia_first: bool) informe l'IA qu'une nouvelle partie démarre
    # ia_first vaut True si l'IA est le premier joueur, et False si le joueur humain commence.

    def new_game(self, ia_first): #=None

        if ia_first == True:
            # if self.i == 0:
            self.val = 0
            print("c'est ia_first")
            
        elif ia_first == False:
            self.val = 1
            print("c'est pas ia_first")

    # ia.player_sets(x, y, u=None, v=None) informe 
    # l'IA que le joueur humain pose un pion en
    # position(X, Y). Les paramètres(U, V) correspondent 
    # à la position du pion appartenant à l'IA et volé par
    # le joueur humain, dans le cas où un pion a été volé pendant 
    # cette phase(sinon ces paramètres valent None).

    def player_sets(self, x, y, u=None, v=None):
        self.adv.append((x, y))
        self.advX.append(x)
        self.advY.append(y)
        print("pion adv", self.adv)
        self.jeuxGlobal.append((x, y))
        print("pion jeuxGlobal", self.jeuxGlobal)
        if (u in self.jeuIaX) and (v in self.jeuIaY):
            print("le joueur adv me prend un pion")
            self.jeuIaX.remove(u)
            self.jeuIaY.remove(v)
            self.jeuIa.remove((u,v))
            self.jeuxGlobal.remove((u,v))
            print("jeuIaX", self.jeuIaX)
            print("jeuIaY", self.jeuIaY)
            print("jeuIa", self.jeuIa)
            print("jeuxGlobal", self.jeuxGlobal)


        #c'est l'adv qui joue
        self.i += 1


    # ia.player_moves(x1, y1, x2, y2, u=None, v=None) 
    # informe l'IA que le joueur humain déplace un
    # pion de la position(X1, Y1) à la position(X2, Y2). 
    # Si la phase de saut est développée, c'est également
    # cet appel qui est utilisé. Les paramètres(U, V) 
    # correspondent à la position du pion appartenant à l'IA
    # et volé par le joueur humain, dans le cas 
    # où un pion a été volé pendant
    # cette phase(sinon ces paramètres valent None).

    def player_moves(self, x1, y1, x2, y2, u=None, v=None):
        pass

    # ia.play() est la fonction demandant à l'ordinateur 
    # quel est son prochain coup. La réponse peut
    # être de deux types:
    # "set", (x, y), (u, v) demande à placer un pion 
    # sur la case(X, Y) et à voler le pion en position
    # (u, v). Si aucun pion n'a été volé, alors(u, v) vaut(None, None).
    # "move", (x1, y1), (x2, y2), (u, v) demande à déplacer 
    # un pion de la case(X1, Y1) à la case
    # (X2, Y2) et à voler le pion en position(u, v). 
    # Si aucun pion n'a été volé, alors(u, v) vaut (None, None).
    # Attention: les retours de ces méthodes sont 
    # des tuples(et non une simple chaîne de
    # caractères.Par exemple "set", (x, y), (u, v) est 
    # de type tuple(str, tuple(int, int), tuple(int, int))


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
    def set(self, x, y, u=None, v=None):
            #x = self.x
            #y = self.y
            #u = self.u
            #v = self.v
            self.x.append(x)
            self.y.append(y)
            self.u.append(u)
            self.v.append(v)
            print("l'ia joue", self.x, self.y, "et mange", self.u, self.v)
            self.advX.remove(u)
            self.advY.remove(v)
            self.adv.remove((u,v))
            self.jeuxGlobal.remove((u,v))
            print("advX", self.advX)
            print("advY", self.advY)
            print("adv", self.adv)
            print("jeuxGlobal", self.jeuxGlobal)
                

    def move(self, x1, y1, x2, y2, u=None, v=None):
        pass

    def play(self):
        print("Ia joue")
       
        # scenario 0   
        #----------------------------------------
        # si il joue en premier
        #----------------------------------------
        #if len(self.jeuxGlobal) == 0:
        if self.i == 0:
            if self.val == 0:
                """ ch001 = random.choice(self.choix001)
                self.jeuxGlobal.append(ch001)
                self.jeuIa.append(ch001)
                if ch001 in self.choix001:
                    print("premier tour scenario 0")
                    X = self.jeuIaX.append((ch001[0]))
                    Y = self.jeuIaY.append((ch001[1]))
                    print("pion ia random", self.jeuIa)
                    print("pion jeuxGlobal", self.jeuxGlobal)
                    #self.i += 1 """
                
                ch001 = random.choice(self.choix002)
                self.jeuxGlobal.append(ch001)
                self.jeuIa.append(ch001)
                if ch001 in self.choix002:
                    print("premier tour scenario 0")
                    X = self.jeuIaX.append((ch001[0]))
                    Y = self.jeuIaY.append((ch001[1]))
                    print("pion ia random", self.jeuIa)
                    print("pion jeuxGlobal", self.jeuxGlobal)
                self.i += 1   
                
        """ else:
            print("break0")
            pass """
                
        
        
        # -------------------------------------------------------------
        # si il joue en deuxieme
        #----------------------------------------
        #if len(self.jeuxGlobal) == 1:
        if self.i == 1:
            if self.val == 1:
                
                """ for element in self.choix001:
                    # scenario 1
                    print("la")
                    if self.adv == [element]:
                        print("ici1")
                        
                        ch001 = random.choice(self.choix001)
                        if ch001 == element:
                            print("le pion est deja pris")
                            ch001 = random.choice(self.choix001)
                            self.jeuxGlobal.append(ch001)
                            self.jeuIa.append(ch001)
                            print("premier tour scenario 1 variante")
                            X = self.jeuIaX.append((ch001[0]))
                            Y = self.jeuIaY.append((ch001[1]))
                            print("pion ia random", self.jeuIa)
                            print("pion jeuxGlobal", self.jeuxGlobal)
                            #self.i += 1
                            print("break2")
                            break
                        self.jeuxGlobal.append(ch001)
                        self.jeuIa.append(ch001)
                        print("premier tour scenario 1")
                        #if ch001 in self.choix001:
                        X = self.jeuIaX.append((ch001[0]))
                        Y = self.jeuIaY.append((ch001[1]))
                        print("pion ia random", self.jeuIa)
                        print("pion jeuxGlobal", self.jeuxGlobal)
                        #self.i += 1 
                        print("break1")
                        break
                    else:
                        print("break3")
                        break
                """

                for element in self.choix002:
                        # scenario 1
                        print("la")
                        if self.adv == [element]:
                            print("ici1")
                            
                            ch001 = random.choice(self.choix002)
                            if ch001 == element:
                                print("le pion est deja pris")
                                ch001 = random.choice(self.choix002)
                                self.jeuxGlobal.append(ch001)
                                self.jeuIa.append(ch001)
                                print("premier tour scenario 1 variante")
                                X = self.jeuIaX.append((ch001[0]))
                                Y = self.jeuIaY.append((ch001[1]))
                                print("pion ia random", self.jeuIa)
                                print("pion jeuxGlobal", self.jeuxGlobal)
                                #self.i += 1
                                print("break2")
                                break
                            self.jeuxGlobal.append(ch001)
                            self.jeuIa.append(ch001)
                            print("premier tour scenario 1")
                            #if ch001 in self.choix001:
                            X = self.jeuIaX.append((ch001[0]))
                            Y = self.jeuIaY.append((ch001[1]))
                            print("pion ia random", self.jeuIa)
                            print("pion jeuxGlobal", self.jeuxGlobal)
                            self.i += 1 
                            print("break1")
                            break
                        else:
                            print("break3")
                            break
                else:
                    print("on passe a la suite")
                    pass
                    
        
        #if len(self.jeuxGlobal) == 2:
        if self.i == 2:
            print("si ia joue en premier pose2")
            #----------------------
            #scenario si ia joue en premier
            #-----------------------
            if self.val == 0:
                self.IaTour1()


        #if len(self.jeuxGlobal) == 3:
        if self.i == 3:
            print("si ia joue en deuxieme pose3")
            #----------------------
            #scenario si ia joue en deuxieme
            #-----------------------
            self.IaTour1()
            

        #if len(self.jeuxGlobal) == 4:
        if self.i == 4:
            print("si ia joue en premier pose4")
            #----------------------
            #scenario si ia joue en premier
            #-----------------------
            if self.val == 0:
                self.IaTour2()
            # ici le premier a poser un moulin c'est l'IA

            

        #if len(self.jeuxGlobal) == 5:
        if self.i == 5:
            print("si ia joue en deuxieme pose5")
            #----------------------
            #scenario si ia joue en deuxieme
            #-----------------------
            self.IaTour2()
            # ici le premier a poser un moulin c'est l'adv
        
        #if len(self.jeuxGlobal) == 6:
        if self.i == 6:
            print("si ia joue en premier pose6")
            #----------------------
            #scenario si ia joue en premier
            #-----------------------
            if self.val == 0:
                self.IaTour3()
            # ici le premier a poser un moulin c'est l'IA

            

        #if len(self.jeuxGlobal) == 7:
        if self.i == 7:
            print("si ia joue en deuxieme pose7")
            #----------------------
            #scenario si ia joue en deuxieme
            #-----------------------
            self.IaTour3()
            # ici le premier a poser un moulin c'est l'adv

        #if len(self.jeuxGlobal) == 8:
        if self.i == 8:
            print("si ia joue en premier pose8")
            #----------------------
            #scenario si ia joue en premier
            #-----------------------
            if self.val == 0:
                self.IaTour4()
            # ici le premier a poser un moulin c'est l'IA

        #if len(self.jeuxGlobal) == 9:
        if self.i == 9:
            print("si ia joue en deuxieme pose9")
            #----------------------
            #scenario si ia joue en deuxieme
            #-----------------------
            self.IaTour4()
            # ici le premier a poser un moulin c'est l'adv


        #if len(self.jeuxGlobal) == 10:
        if self.i == 10:
            print("si ia joue en premier pose10")
            #----------------------
            #scenario si ia joue en premier
            #-----------------------
            if self.val == 0:
                self.IaTour5()
            # ici le premier a poser un moulin c'est l'IA

            

        #if len(self.jeuxGlobal) == 11:
        if self.i == 11:
            print("si ia joue en deuxieme pose11")
            #----------------------
            #scenario si ia joue en deuxieme
            #-----------------------
            self.IaTour5()
            # ici le premier a poser un moulin c'est l'adv

        #if len(self.jeuxGlobal) == 12:
        if self.i == 12:
            print("si ia joue en premier pose12")
            #----------------------
            #scenario si ia joue en premier
            #-----------------------
            if self.val == 0:
                self.IaTour6()
            # ici le premier a poser un moulin c'est l'IA

            

        #if len(self.jeuxGlobal) == 13:
        if self.i == 13:
            print("si ia joue en deuxieme pose13")
            #----------------------
            #scenario si ia joue en deuxieme
            #-----------------------
            self.IaTour6()
            # ici le premier a poser un moulin c'est l'adv

        #if len(self.jeuxGlobal) == 14:
        if self.i == 14:
            print("si ia joue en premier pose14")
            #----------------------
            #scenario si ia joue en premier
            #-----------------------
            if self.val == 0:
                self.IaTour7()
            # ici le premier a poser un moulin c'est l'IA

            

        #if len(self.jeuxGlobal) == 15:
        if self.i == 15:
            print("si ia joue en deuxieme pose15")
            #----------------------
            #scenario si ia joue en deuxieme
            #-----------------------
            self.IaTour7()
            # ici le premier a poser un moulin c'est l'adv

        
        #if len(self.jeuxGlobal) == 16:
        if self.i == 16:
            print("si ia joue en premier pose16")
            #----------------------
            #scenario si ia joue en premier
            #-----------------------
            if self.val == 0:
                self.IaTour8()
            # ici le premier a poser un moulin c'est l'IA

            

        #if len(self.jeuxGlobal) == 17:
        if self.i == 17:
            print("si ia joue en deuxieme pose17")
            #----------------------
            #scenario si ia joue en deuxieme
            #-----------------------
            self.IaTour8()
            # ici le premier a poser un moulin c'est l'adv
            




    #-----------------------------
    #tour1
    #-----------------------------
    def IaTour1(self):
        if self.jeuIa == [(7,1)]: #si dans le jeux il y a
            #if self.adv != [(7,4)]:
            if ((7, 4) not in self.adv):
                #if self.adv != [(7,7)]:
                if ((7, 7) not in self.adv):
                    self.jeuxGlobal.append((7, 4))
                    self.jeuIa.append((7, 4))
                    print("deuxieme tours ia 7,4 ")
                    X = self.jeuIaX.append(7)
                    Y = self.jeuIaY.append(4)
                    print("pion ia", self.jeuIa)
                    print("pion jeuxGlobal", self.jeuxGlobal)
                    self.i += 1  

                #elif self.adv != [(4,1)]:
                elif ((4, 1) not in self.adv):
                    #if self.adv != [(1,1)]:
                    if ((1, 1) not in self.adv):
                        self.jeuxGlobal.append((4, 1))
                        self.jeuIa.append((4, 1))
                        print("deuxieme tours ia 4,1 ")
                        X = self.jeuIaX.append(4)
                        Y = self.jeuIaY.append(1)
                        print("pion ia", self.jeuIa)
                        print("pion jeuxGlobal", self.jeuxGlobal)
                        self.i += 1
                else:
                    pass
            
        elif self.jeuIa == [(6,2)]: #si dans le jeux il y a
            #if self.adv != [(6,4)]:
            if ((6, 4) not in self.adv):
                #if self.adv != [(6,6)]:
                if ((6, 6) not in self.adv):
                    self.jeuxGlobal.append((6, 4))
                    self.jeuIa.append((6, 4))
                    print("deuxieme tours ia 6,4 ")
                    X = self.jeuIaX.append(6)
                    Y = self.jeuIaY.append(4)
                    print("pion ia", self.jeuIa)
                    print("pion jeuxGlobal", self.jeuxGlobal)
                    self.i += 1

                #elif self.adv != [(4,2)]:
                elif ((4, 2) not in self.adv):
                    #if self.adv != [(3,2)]:
                    if ((3, 2) not in self.adv):
                        self.jeuxGlobal.append((4, 2))
                        self.jeuIa.append((4, 2))
                        print("deuxieme tours ia 4,2 ")
                        X = self.jeuIaX.append(4)
                        Y = self.jeuIaY.append(2)
                        print("pion ia", self.jeuIa)
                        print("pion jeuxGlobal", self.jeuxGlobal)
                        self.i += 1
                else:
                    pass

        elif self.jeuIa == [(1,7)]: #si dans le jeux il y a
            if ((1, 4) not in self.adv):
                if ((1, 1) not in self.adv):
                    self.jeuxGlobal.append((1, 4))
                    self.jeuIa.append((1, 4))
                    print("deuxieme tours ia 1,4 ")
                    X = self.jeuIaX.append(1)
                    Y = self.jeuIaY.append(4)
                    print("pion ia", self.jeuIa)
                    print("pion jeuxGlobal", self.jeuxGlobal)
                    self.i += 1

                elif ((4, 7) not in self.adv):
                    if ((7, 7) not in self.adv):
                        self.jeuxGlobal.append((4, 7))
                        self.jeuIa.append((4, 7))
                        print("deuxieme tours ia 4,7 ")
                        X = self.jeuIaX.append(4)
                        Y = self.jeuIaY.append(7)
                        print("pion ia", self.jeuIa)
                        print("pion jeuxGlobal", self.jeuxGlobal)
                        self.i += 1
                else:
                    pass
        
    #-----------------------------
    #tour2
    #-----------------------------
    def IaTour2(self):
        if self.jeuIa == [(7,1), (7,4)]: #si dans le jeux il y a
            if ((7, 7) not in self.adv):
                self.jeuxGlobal.append((7, 7))
                self.jeuIa.append((7, 7))
                print("troisieme tours ia 7,7 ")
                X = self.jeuIaX.append(7)
                Y = self.jeuIaY.append(7)
                print("pion ia", self.jeuIa)
                print("pion jeuxGlobal", self.jeuxGlobal)
                # partie ou l'ia a un moulin et il mange le dernier pion posé par l'adv
                print("j'ai un moulin je mange un pion adv")
                print("jeuIaX", self.jeuIaX[-1], "jeuIaY", self.jeuIaY[-1], "advX", self.advX[-1], "advY", self.advY[-1])
                self.set(self.jeuIaX[-1], self.jeuIaY[-1], self.advX[-1], self.advY[-1])
                print("pion ia", self.jeuIa)
                self.i += 1
                pass

            elif ((7, 7) in self.adv):
                if ((4,1) not in self.adv):
                    if ((1,1) not in self.adv):
                        self.jeuxGlobal.append((4, 1))
                        self.jeuIa.append((4, 1))
                        print("troisieme tours ia 4,1 ")
                        X = self.jeuIaX.append(4)
                        Y = self.jeuIaY.append(1)
                        print("pion ia", self.jeuIa)
                        print("pion jeuxGlobal", self.jeuxGlobal)
                        self.i += 1
                else:
                    pass

        elif self.jeuIa == [(6, 2), (6, 4)]: #si dans le jeux il y a
            if ((6, 6) not in self.adv):
                self.jeuxGlobal.append((6, 6))
                self.jeuIa.append((6, 6))
                print("troisieme tours ia 6,6 ")
                X = self.jeuIaX.append(6)
                Y = self.jeuIaY.append(6)
                print("pion ia", self.jeuIa)
                print("pion jeuxGlobal", self.jeuxGlobal)
                 # partie ou l'ia a un moulin et il mange le dernier pion posé par l'adv
                print("j'ai un moulin je mange un pion adv")
                print("jeuIaX", self.jeuIaX[-1], "jeuIaY", self.jeuIaY[-1], "advX", self.advX[-1], "advY", self.advY[-1])
                self.set(self.jeuIaX[-1], self.jeuIaY[-1], self.advX[-1], self.advY[-1])
                self.i += 1
            
            elif ((6, 6) in self.adv):
                if ((4, 2) not in self.adv):
                    if ((2, 2) not in self.adv):
                        self.jeuxGlobal.append((4, 2))
                        self.jeuIa.append((4, 2))
                        print("troisieme tours ia 4,2 ")
                        X = self.jeuIaX.append(4)
                        Y = self.jeuIaY.append(2)
                        print("pion ia", self.jeuIa)
                        print("pion jeuxGlobal", self.jeuxGlobal)
                        self.i += 1
                else:
                    pass
        
        elif self.jeuIa == [(1, 7), (1, 4)]: #si dans le jeux il y a
            if ((1, 1) not in self.adv):
                self.jeuxGlobal.append((1, 1))
                self.jeuIa.append((1, 1))
                print("troisieme tours ia 1,1 ")
                X = self.jeuIaX.append(1)
                Y = self.jeuIaY.append(1)
                print("pion ia", self.jeuIa)
                print("pion jeuxGlobal", self.jeuxGlobal)
                 # partie ou l'ia a un moulin et il mange le dernier pion posé par l'adv
                print("j'ai un moulin je mange un pion adv")
                print("jeuIaX", self.jeuIaX[-1], "jeuIaY", self.jeuIaY[-1], "advX", self.advX[-1], "advY", self.advY[-1])
                self.set(self.jeuIaX[-1], self.jeuIaY[-1], self.advX[-1], self.advY[-1])
                self.i += 1
            
            elif ((1, 1) in self.adv):
                if ((4, 7) not in self.adv):
                    if ((7, 7) not in self.adv):
                        self.jeuxGlobal.append((4, 7))
                        self.jeuIa.append((4, 7))
                        print("troisieme tours ia 4,7 ")
                        X = self.jeuIaX.append(4)
                        Y = self.jeuIaY.append(7)
                        print("pion ia", self.jeuIa)
                        print("pion jeuxGlobal", self.jeuxGlobal)
                        self.i += 1
                else:
                    pass

            
    #-----------------------------
    #tour3
    #-----------------------------
    def IaTour3(self):
        
        if self.jeuIa == [(7,1), (7,4), (7,7)]: #si dans le jeux il y a
            if ((6, 2) not in self.adv):
                if ((6, 4) not in self.adv):
                    if ((6, 6) not in self.adv):
                        self.jeuxGlobal.append((6, 2))
                        self.jeuIa.append((6, 2))
                        print("quatrieme tours ia 6,2 ")
                        X = self.jeuIaX.append(6)
                        Y = self.jeuIaY.append(2)
                        print("pion ia", self.jeuIa)
                        print("pion jeuxGlobal", self.jeuxGlobal)
                        self.i += 1
                
            elif ((6, 2) in self.adv):
                if ((5,3) not in self.adv):
                    if ((5,4) not in self.adv):
                        if ((5,5) not in self.adv):
                            self.jeuxGlobal.append((5, 3))
                            self.jeuIa.append((5, 3))
                            print("quatrieme tours ia 5,3 ")
                            X = self.jeuIaX.append(5)
                            Y = self.jeuIaY.append(3)
                            print("pion ia", self.jeuIa)
                            print("pion jeuxGlobal", self.jeuxGlobal)
                            self.i += 1
                else:
                    pass

        elif self.jeuIa == [(6, 2), (6, 4), (6, 6)]: #si dans le jeux il y a
            if ((5, 3) not in self.adv):
                if ((5, 4) not in self.adv):
                    if ((5, 5) not in self.adv):
                        self.jeuxGlobal.append((5, 3))
                        self.jeuIa.append((5, 3))
                        print("quatrieme tours ia 5,3 ")
                        X = self.jeuIaX.append(5)
                        Y = self.jeuIaY.append(3)
                        print("pion ia", self.jeuIa)
                        print("pion jeuxGlobal", self.jeuxGlobal)
                        self.i += 1
                
            elif ((5, 3) in self.adv):
                if ((3,3) not in self.adv):
                    if ((3,4) not in self.adv):
                        if ((3,5) not in self.adv):
                            self.jeuxGlobal.append((3, 3))
                            self.jeuIa.append((3, 3))
                            print("quatrieme tours ia 3,3 ")
                            X = self.jeuIaX.append(3)
                            Y = self.jeuIaY.append(3)
                            print("pion ia", self.jeuIa)
                            print("pion jeuxGlobal", self.jeuxGlobal)
                            self.i += 1
                else:
                    pass

        elif self.jeuIa == [(1, 7), (1, 4), (1, 1)]: #si dans le jeux il y a
            if ((5, 3) not in self.adv):
                if ((5, 4) not in self.adv):
                    if ((5, 5) not in self.adv):
                        self.jeuxGlobal.append((5, 3))
                        self.jeuIa.append((5, 3))
                        print("quatrieme tours ia 5,3 ")
                        X = self.jeuIaX.append(5)
                        Y = self.jeuIaY.append(3)
                        print("pion ia", self.jeuIa)
                        print("pion jeuxGlobal", self.jeuxGlobal)
                        self.i += 1
                
            elif ((5, 3) in self.adv):
                if ((3,3) not in self.adv):
                    if ((3,4) not in self.adv):
                        if ((3,5) not in self.adv):
                            self.jeuxGlobal.append((3, 3))
                            self.jeuIa.append((3, 3))
                            print("quatrieme tours ia 3,3 ")
                            X = self.jeuIaX.append(3)
                            Y = self.jeuIaY.append(3)
                            print("pion ia", self.jeuIa)
                            print("pion jeuxGlobal", self.jeuxGlobal)
                            self.i += 1
                else:
                    pass

        elif self.jeuIa == [(7,1), (7,4), (4,1)]: #si dans le jeux il y a
            if ((1, 1) not in self.adv):
                self.jeuxGlobal.append((1, 1))
                self.jeuIa.append((1, 1))
                print("quatrieme tours ia 1,1 ")
                X = self.jeuIaX.append(1)
                Y = self.jeuIaY.append(1)
                print("pion ia", self.jeuIa)
                print("pion jeuxGlobal", self.jeuxGlobal)
                # partie ou l'ia a un moulin et il mange le dernier pion posé par l'adv
                print("j'ai un moulin je mange un pion adv")
                print("jeuIaX", self.jeuIaX[-1], "jeuIaY", self.jeuIaY[-1], "advX", self.advX[-1], "advY", self.advY[-1])
                self.set(self.jeuIaX[-1], self.jeuIaY[-1], self.advX[-1], self.advY[-1])
                self.i += 1
                
            elif ((1, 1) in self.adv):
                if ((3,3) not in self.adv):
                    if ((3,4) not in self.adv):
                        if ((3,5) not in self.adv):
                            self.jeuxGlobal.append((3, 3))
                            self.jeuIa.append((3, 3))
                            print("quatrieme tours ia 3,3 ")
                            X = self.jeuIaX.append(3)
                            Y = self.jeuIaY.append(3)
                            print("pion ia", self.jeuIa)
                            print("pion jeuxGlobal", self.jeuxGlobal)
                            self.i += 1
                else:
                    pass

        elif self.jeuIa == [(6,2), (6,4), (4,2)]: #si dans le jeux il y a
            if ((2, 2) not in self.adv):
                self.jeuxGlobal.append((2, 2))
                self.jeuIa.append((2, 2))
                print("quatrieme tours ia 2,2 ")
                X = self.jeuIaX.append(2)
                Y = self.jeuIaY.append(2)
                print("pion ia", self.jeuIa)
                print("pion jeuxGlobal", self.jeuxGlobal)
                # partie ou l'ia a un moulin et il mange le dernier pion posé par l'adv
                print("j'ai un moulin je mange un pion adv")
                print("jeuIaX", self.jeuIaX[-1], "jeuIaY", self.jeuIaY[-1], "advX", self.advX[-1], "advY", self.advY[-1])
                self.set(self.jeuIaX[-1], self.jeuIaY[-1], self.advX[-1], self.advY[-1])
                self.i += 1
                
            elif ((2, 2) in self.adv):
                if ((3,3) not in self.adv):
                    if ((3,4) not in self.adv):
                        if ((3,5) not in self.adv):
                            self.jeuxGlobal.append((3, 3))
                            self.jeuIa.append((3, 3))
                            print("quatrieme tours ia 3,3 ")
                            X = self.jeuIaX.append(3)
                            Y = self.jeuIaY.append(3)
                            print("pion ia", self.jeuIa)
                            print("pion jeuxGlobal", self.jeuxGlobal)
                            self.i += 1
                else:
                    pass

    #-----------------------------
    #tour4
    #-----------------------------
    def IaTour4(self):

        if self.jeuIa == [(6,2), (6,4), (4,2), (2,2)]: #si dans le jeux il y a
            if ((5, 3) not in self.adv):
                if ((5, 4) not in self.adv):
                    if ((5, 5) not in self.adv):
                        self.jeuxGlobal.append((5, 3))
                        self.jeuIa.append((5, 3))
                        print("Cinquieme tours ia 5,3 ")
                        X = self.jeuIaX.append(5)
                        Y = self.jeuIaY.append(3)
                        print("pion ia", self.jeuIa)
                        print("pion jeuxGlobal", self.jeuxGlobal)
                        self.i += 1
                
            elif ((5, 3) in self.adv):
                if ((3,3) not in self.adv):
                    if ((3,4) not in self.adv):
                        if ((3,5) not in self.adv):
                            self.jeuxGlobal.append((3, 3))
                            self.jeuIa.append((3, 3))
                            print("Cinquieme tours ia 3,3 ")
                            X = self.jeuIaX.append(3)
                            Y = self.jeuIaY.append(3)
                            print("pion ia", self.jeuIa)
                            print("pion jeuxGlobal", self.jeuxGlobal)
                            self.i += 1
                else:
                    pass
        
    #-----------------------------
    #tour5
    #-----------------------------
    def IaTour5(self):
        #todo
        pass
        
    #-----------------------------
    #tour6
    #-----------------------------
    def IaTour6(self):
        #todo
        pass

    #-----------------------------
    #tour7
    #-----------------------------
    def IaTour7(self):
        #todo
        pass

    #-----------------------------
    #tour8
    #-----------------------------
    def IaTour8(self):
        #todo
        pass

    #-----------------------------
    #move1
    #-----------------------------
    def IaMove1(self):
        #todo
        pass