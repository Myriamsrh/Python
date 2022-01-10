import unittest
import Moteur_new as game


class MyTestCase(unittest.TestCase):

    """ Test des listes """
    def test_pose_pion(self):
        # Arrange
        moteur = game.Moulin()
        # Act
        """ Pion 1 """
        moteur.pion_red.append((4, 1))
        moteur.damier[4][1] = moteur.couleur[0]
        moteur.pionposé_damier.append((4, 1))
        """ Pion 2 """
        moteur.pion_blue.append((2, 2))
        moteur.damier[2][2] = moteur.couleur[1]
        moteur.pionposé_damier.append((2, 2))
        """ Pion 3 """
        moteur.pion_red.append((1, 4))
        moteur.damier[1][4] = moteur.couleur[0]
        moteur.pionposé_damier.append((1, 4))
        """ Pion 4 """
        moteur.pion_blue.append((2, 4))
        moteur.damier[2][4] = moteur.couleur[1]
        moteur.pionposé_damier.append((2, 4))
        """ Pion 5 """
        moteur.pion_red.append((1, 7))
        moteur.damier[1][7] = moteur.couleur[0]
        moteur.pionposé_damier.append((1, 7))
        """ Pion 6 """
        moteur.pion_blue.append((6, 4))
        moteur.damier[6][4] = moteur.couleur[1]
        moteur.pionposé_damier.append((6, 4))
        """ Pion 7 """
        moteur.pion_red.append((3, 4))
        moteur.damier[3][4] = moteur.couleur[0]
        moteur.pionposé_damier.append((3, 4))
        """ Pion 8 """
        moteur.pion_blue.append((4, 3))
        moteur.damier[4][3] = moteur.couleur[1]
        moteur.pionposé_damier.append((4, 3))
        """ Pion 9 """
        moteur.pion_red.append((7, 4))
        moteur.damier[7][4] = moteur.couleur[0]
        moteur.pionposé_damier.append((7, 4))
        """ Pion 10 """
        moteur.pion_blue.append((2, 6))
        moteur.damier[2][6] = moteur.couleur[1]
        moteur.pionposé_damier.append((2, 6))
        """ Pion 11 """
        moteur.pion_red.append((5, 5))
        moteur.damier[5][5] = moteur.couleur[0]
        moteur.pionposé_damier.append((5, 5))
        """ Pion 12 """
        moteur.pion_blue.append((6, 2))
        moteur.damier[6][2] = moteur.couleur[1]
        moteur.pionposé_damier.append((6, 2))
        """ Pion 13 """
        moteur.pion_red.append((5, 3))
        moteur.damier[5][3] = moteur.couleur[0]
        moteur.pionposé_damier.append((5, 3))
        """ Pion 14 """
        moteur.pion_blue.append((4, 2))
        moteur.damier[4][2] = moteur.couleur[1]
        moteur.pionposé_damier.append((4, 2))
        """ Pion 15 """
        moteur.pion_red.append((5, 4))
        moteur.damier[5][4] = moteur.couleur[0]
        moteur.pionposé_damier.append((5, 4))
        """ Moulin """
        resultat = moteur.moulin_renvoi_liste()
        resultatR = moteur.pion_red
        resultatB = moteur.pion_blue
        resultatP = moteur.pionposé_damier
        # Assert
        print("Pion : ", resultatP)
        print("Rouge : ", resultatR)
        print("Bleue : ", resultatB)
        print("List moulin : ", moteur.listeM)
        print(moteur.newdamier())
        print(moteur.damier)
        self.assertEqual(resultatP,
                         [(4, 1), (2, 2), (1, 4), (2, 4), (1, 7), (6, 4), (3, 4), (4, 3), (7, 4), (2, 6), (5, 5),
                          (6, 2), (5, 3), (4, 2), (5, 4)])
        self.assertNotEqual(resultatP, [(1, 4), (2, 4), (1, 7), (6, 4), (7, 1), (4, 3), (7, 4), (5, 3), (4, 2), (5, 4)])
        self.assertNotEqual(resultatP, [])
        self.assertEqual(resultatR, [(4, 1), (1, 4), (1, 7), (3, 4), (7, 4), (5, 5), (5, 3), (5, 4)])
        self.assertNotEqual(resultatR, [(4, 1), (1, 4), (1, 7), (7, 1), (7, 4)])
        self.assertEqual(resultatB, [(2, 2), (2, 4), (6, 4), (4, 3), (2, 6), (6, 2), (4, 2)])
        self.assertNotEqual(resultatB, [(2, 2), (2, 4)])
        self.assertEqual(moteur.listeM, [[], [(2, 2), (2, 4), (2, 6)], [], [], [], [(5, 3), (5, 4), (5, 5)], [], [], [],
                                    [(2, 2), (4, 2), (6, 2)], [], [], [], [], [], []])
        self.assertNotEqual(resultat,
                            [[(1, 1), (1, 4), (1, 7)], [(2, 2), (2, 4), (2, 6)], [], [], [], [], [], [], [], [], [], [],
                             [], [(2, 2), (4, 2), (6, 2)], [], []])
        self.assertNotEqual(resultat, [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []])
        self.assertEqual(moteur.damier[4][3], "B")
        self.assertNotEqual(moteur.damier[7][4], "B")

    """ Test de déplacement """
    def test_déplacement(self):
        # Arrange
        m = game.Moulin()
        # Act
        m.pionposé_damier.append((1, 1))
        m.pionposé_damier.append((3, 5))
        m.pionposé_damier.append((4, 2))
        resultat_1 = m.déplacement(1, 1)
        resultat_2 = m.déplacement(2, 2)
        resultat_3 = m.déplacement(3, 5)
        resultat_4 = m.déplacement(4, 2)
        resultat_5 = m.déplacement(2, 3)
        # Assert
        print(m.pionposé_damier)
        print(resultat_1)
        print(resultat_2)
        self.assertEqual(resultat_1, [(1, 4), (4, 1)])
        self.assertNotEqual(resultat_1, [(7, 4), (4, 7)])
        self.assertEqual(resultat_2, None)
        self.assertNotEqual(resultat_2, [(2, 4), (4, 2)])
        self.assertEqual(resultat_3, [(3, 4), (4, 5)])
        self.assertNotEqual(resultat_3, [(3, 3), (3, 5)])
        self.assertEqual(resultat_4, [(4, 1), (2, 2), (4, 3), (6, 2)])
        self.assertNotEqual(resultat_4, [(4, 3), (6, 2)])
        self.assertEqual(resultat_5, None)

    """ Test de reconnaitre_moulin """
    def test_reconnaitremoulin(self):
        # Arrange
        l = game.Moulin()
        m = game.Moulin()
        m.damier[3][5] = m.couleur[0]
        m.damier[4][1] = m.couleur[1]
        m.damier[4][5] = m.couleur[0]
        m.damier[4][2] = m.couleur[1]
        m.damier[5][5] = m.couleur[0]
        m.damier[4][3] = m.couleur[1]
        m.damier[6][2] = m.couleur[0]
        m.damier[2][2] = m.couleur[1]
        m.damier[6][6] = m.couleur[1]
        n = game.Moulin()
        n.damier[6][2] = n.couleur[0]
        n.damier[6][4] = n.couleur[0]
        n.damier[6][6] = n.couleur[0]
        # Act
        resultat1 = l.reconnaitre_moulin()
        resultat2 = m.reconnaitre_moulin()
        resultat3 = n.reconnaitre_moulin()
        # Assert
        self.assertEqual(resultat1, False)
        self.assertNotEqual(resultat1, True)
        self.assertEqual(resultat2, True)
        self.assertNotEqual(resultat2, False)
        self.assertEqual(resultat3, True)
        self.assertNotEqual(resultat3, False)

    """ Test de moulin_renvoi_liste """
    def test_moulin_renvoi_liste(self):
        # Arrange
        l = game.Moulin()
        m = game.Moulin()
        n = game.Moulin()
        o = game.Moulin()
        # Act
        m.damier[1][4] = m.couleur[0]
        m.damier[5][3] = m.couleur[1]
        m.damier[2][4] = m.couleur[0]
        m.damier[5][4] = m.couleur[1]
        m.damier[3][4] = m.couleur[0]
        m.damier[5][5] = m.couleur[1]
        m.damier[1][7] = m.couleur[0]
        m.damier[2][2] = m.couleur[1]

        n.damier[6][2] = n.couleur[0]
        n.damier[6][4] = n.couleur[0]
        n.damier[6][6] = n.couleur[0]

        o.damier[4][1] = o.couleur[1]
        o.damier[4][2] = o.couleur[1]
        o.damier[4][3] = o.couleur[1]
        o.damier[3][3] = o.couleur[1]
        o.damier[4][3] = o.couleur[1]
        o.damier[5][3] = o.couleur[1]
        # Act
        resultat1 = l.moulin_renvoi_liste()
        resultat2 = m.moulin_renvoi_liste()
        resultat3 = n.moulin_renvoi_liste()
        resultat4 = o.moulin_renvoi_liste()
        # Assert
        self.assertEqual(resultat1, None)
        self.assertNotEqual(resultat1, [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []])
        self.assertEqual(l.listeM, [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []])
        self.assertNotEqual(l.listeM, None)
        self.assertEqual(resultat2, None)
        self.assertEqual(m.listeM, [[], [], [], [], [], [(5, 3), (5, 4), (5, 5)], [], [], [], [], [], [(1, 4), (2, 4), (3, 4)], [], [], [], []])
        self.assertNotEqual(m.listeM, [[], [(2, 2), (2, 4), (2, 6)], [], [], [], [], [], [(1, 4), (2, 4), (3, 4)], [], [], [], [], [], [], [], []])
        self.assertEqual(m.damier[1][4], "R")
        self.assertEqual(m.damier[2][2], "B")
        self.assertEqual(resultat3, None)
        self.assertNotEqual(resultat3, [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []])
        self.assertEqual(n.listeM, [[], [], [], [], [], [], [(6, 2), (6, 4), (6, 6)], [], [], [], [], [], [], [], [], []])
        self.assertNotEqual(n.damier[6][4], "B")
        self.assertEqual(resultat4, None)
        self.assertEqual(o.listeM, [[], [], [], [(4, 1), (4, 2), (4, 3)], [], [], [], [], [], [], [(3, 3), (4, 3), (5, 3)], [], [], [], [], []])
        self.assertNotEqual(o.listeM, [[], [], [], [(3, 3), (4, 3), (5, 3)], [], [], [], [], [], [], [(4, 1), (4, 2), (4, 3)], [], [], [], [], []])

    """ Test de Pose """
    def test_pose(self):
        #Arrange
        m = game.Moulin()
        # Act
        m.pose(1, 4)
        m.pose(3, 3)
        m.pose(5, 4)
        m.pose(7, 1)
        # Assert
        print(m.lp)
        self.assertEqual(m.lp, list(range(7 * 2)))
        self.assertNotEqual(m.lp, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        self.assertEqual(m.pionposé_damier, [(1, 4), (3, 3), (5, 4), (7, 1)])
        self.assertEqual(m.pion_red, [(1, 4), (5, 4)])
        self.assertEqual(m.pion_blue, [(3, 3), (7, 1)])
        self.assertEqual(m.damier[1][4], "R")
        self.assertEqual(m.damier[3][3], "B")
        self.assertEqual(m.damier[5][4], "R")
        self.assertEqual(m.damier[7][1], "B")
        self.assertEqual(game.mon_dictionnaire['14'], [(1, 4), True, 1])
        self.assertEqual(game.mon_dictionnaire['33'], [(3, 3), True, 2])
        self.assertEqual(game.mon_dictionnaire['34'], [(3, 4), False, 0])
        self.assertEqual(game.mon_dictionnaire['54'][1], True)
        self.assertEqual(game.mon_dictionnaire['71'][2], 2)
        self.assertEqual(game.mon_dictionnaire['66'][2], 0)


    """" Test de Mouvement """
    def test_mouvement(self):
        # Arrange
        m = game.Moulin()
        # Act
        game.mon_dictionnaire= {'11': [(1, 1), False, 0], '14': [(1, 4), True, 1], '17': [(1, 7), False, 0],
                                '22': [(2, 2), True, 2], '24': [(2, 4), False, 0], '26': [(2, 6), False, 0],
                                '33': [(3, 3), True, 1], '34': [(3, 4), False, 0], '36': [(3, 5), False, 0],
                                '41': [(4, 1), True, 2], '42': [(4, 2), True, 1], '43': [(4, 3), False, 0],
                                '45': [(4, 5), False, 0], '46': [(4, 6), False, 0], '47': [(4, 7), True, 2],
                                '53': [(5, 3), False, 0], '54': [(5, 4), True, 1], '55': [(5, 5), False, 0],
                                '62': [(6, 2), False, 0], '64': [(6, 4), False, 0], '66': [(6, 6), True, 2],
                                '71': [(7, 1), True, 1], '74': [(7, 4), False, 0], '77': [(7, 7), True, 2]}
        m.damier[1][4] = "R"
        m.damier[2][2] = "B"
        m.damier[3][3] = "R"
        m.damier[4][1] = "B"
        m.damier[4][2] = "R"
        m.damier[4][7] = "B"
        m.damier[5][4] = "R"
        m.damier[6][6] = "B"
        m.damier[7][1] = "R"
        m.damier[7][7] = "B"
        m.pionposé_damier = [(1, 4), (2, 2), (3, 3), (4, 1), (4, 2), (4, 7), (5, 4), (6, 6), (7, 1), (7, 7)]
        m.pion_red = [(1, 4), (3, 3), (4, 2), (5, 4), (7, 1)]
        m.pion_blue = [(2, 2), (4, 1),  (4, 7),  (6, 6),  (7, 7)]
        m.mouvement(1, 4, 1 ,1)
        m.mouvement(6, 6, 6, 4)
        m.mouvement(4, 2, 6 ,2)
        m.mouvement(2, 2, 2, 4)
        m.mouvement(7, 1, 7 ,4)
        # Assert
        print("Pion posé : ", m.pion_blue)
        self.assertEqual(m.pionposé_damier, [(3, 3), (4, 1), (4, 7), (5, 4), (7, 7), (1, 1), (6, 4), (6, 2), (2, 4), (7, 4)])
        self.assertNotEqual(m.pionposé_damier, [(1, 1), (2, 4), (3, 3), (4, 1), (4, 2), (4, 7), (5, 4), (6, 4), (7, 4), (7, 7)])
        self.assertEqual(m.pion_red, [(3, 3), (5, 4), (1, 1), (6, 2), (7, 4)])
        self.assertNotEqual(m.pion_red, [(1, 1), (3, 3), (6, 2), (5, 4), (7, 4)])
        self.assertNotEqual(m.pion_red, [(1, 4), (3, 3), (4, 2), (5, 4), (7, 1)])
        self.assertEqual(m.pion_blue,   [(4, 1), (4, 7), (7, 7), (6, 4), (2, 4)])
        self.assertNotEqual(m.pion_blue, [])
        self.assertEqual(m.damier[1][1], "R")
        self.assertNotEqual(m.damier[6][2], "B")
        self.assertEqual(m.damier[6][4], "B")
        self.assertEqual(m.damier[7][4], "R")
        self.assertEqual(game.mon_dictionnaire['11'][2], 1)
        self.assertEqual(game.mon_dictionnaire['14'][2], 0)
        self.assertEqual(game.mon_dictionnaire['64'][1], True)
        self.assertEqual(game.mon_dictionnaire['71'][1], False)
        self.assertEqual(game.mon_dictionnaire['24'][2], 2)
        self.assertEqual(game.mon_dictionnaire['62'], [(6, 2), True, 1])

    """ Test de retirer_pion """
    def test_retirerpion(self):
        # Arrange
        m = game.Moulin()
        # Act
        game.mon_dictionnaire = {'11': [(1, 1), False, 0], '14': [(1, 4), True, 1], '17': [(1, 7), False, 0],
                                 '22': [(2, 2), False, 0], '24': [(2, 4), False, 0], '26': [(2, 6), True, 2],
                                 '33': [(3, 3), True, 1], '34': [(3, 4), False, 0], '36': [(3, 5), False, 0],
                                 '41': [(4, 1), False, 0], '42': [(4, 2), True, 2], '43': [(4, 3), True, 1],
                                 '45': [(4, 5), False, 0], '46': [(4, 6), False, 0], '47': [(4, 7), False, 0],
                                 '53': [(5, 3), False, 0], '54': [(5, 4), True, 1], '55': [(5, 5), False, 0],
                                 '62': [(6, 2), True, 2], '64': [(6, 4), True, 2], '66': [(6, 6), True, 2],
                                 '71': [(7, 1), False, 0], '74': [(7, 4), False, 0], '77': [(7, 7), True, 2]}
        m.damier[1][4] = "R"
        m.damier[2][6] = "B"
        m.damier[3][3] = "R"
        m.damier[4][2] = "B"
        m.damier[4][3] = "R"
        m.damier[6][2] = "B"
        m.damier[5][4] = "R"
        m.damier[6][4] = "B"
        m.damier[7][7] = "R"
        m.damier[6][6] = "B"
        m.pionposé_damier = [(1, 4), (2, 6), (3, 3), (4, 2), (4 ,3), (6, 2), (5, 4), (6, 4), (7, 7), (6, 6)]
        m.pion_red = [(1, 4), (3, 3), (4 ,3), (5, 4), (7, 7)]
        m.pion_blue = [(2, 6), (4, 2), (6, 2), (6, 4), (6, 6)]
        m.verif_moulinfait()
        self.assertEqual(m.moulin_déjàfait, [[]])
        self.assertEqual(m.boolRetirer, True)
        m.moulin_renvoi_liste()
        self.assertEqual(m.listeM, [[], [], [], [], [], [], [(6, 2), (6, 4), (6, 6)], [], [], [], [], [], [], [], [], []])
        self.assertEqual(m.damier[6][2], "B")
        m.retirer_pion(1, 4)
        self.assertEqual(m.pionposé_damier,[(2, 6), (3, 3), (4, 2), (4 ,3), (6, 2), (5, 4), (6, 4), (7, 7), (6, 6)])
        self.assertNotEqual(m.pionposé_damier, [(1, 4), (2, 6), (3, 3), (4, 2), (4 ,3), (6, 2), (5, 4), (6, 4), (7, 7), (6, 6)])
        self.assertEqual(m.pion_red,[(3, 3), (4 ,3), (5, 4), (7, 7)])
        self.assertEqual(m.pion_blue, [(2, 6), (4, 2), (6, 2), (6, 4), (6, 6)])
        self.assertEqual(m.boolRetirer, False)
        self.assertEqual(game.mon_dictionnaire['14'], [(1, 4), False, 0])
        self.assertEqual(m.moulin_déjàfait, [[],[(6, 2), (6, 4), (6, 6)]])
        m.mouvement(5, 4, 5, 3)
        self.assertEqual(m.pionposé_damier, [(2, 6), (3, 3), (4, 2), (4 ,3), (6, 2), (6, 4), (7, 7), (6, 6), (5, 3)])
        self.assertEqual(m.pion_red, [(3, 3), (4 ,3), (7, 7), (5, 3)])
        self.assertEqual(m.pion_blue, [(2, 6), (4, 2), (6, 2), (6, 4), (6, 6)])
        self.assertEqual(m.damier[5][4], (5, 4))
        self.assertEqual(m.damier[5][3], "R")
        self.assertEqual(game.mon_dictionnaire['54'], [(5, 4), False, 0])
        self.assertEqual(game.mon_dictionnaire['53'], [(5, 3), True, 1])
        m.verif_moulinfait()
        self.assertEqual(m.boolRetirer, True)
        m.moulin_renvoi_liste()
        self.assertEqual(m.listeM, [[], [], [], [], [], [], [(6, 2), (6, 4), (6, 6)], [], [], [], [(3, 3), (4, 3), (5, 3)], [], [], [], [], []])
        m.retirer_pion(4, 2)
        self.assertEqual(m.pionposé_damier, [(2, 6), (3, 3), (4 ,3), (6, 2), (6, 4), (7, 7), (6, 6), (5, 3)])
        self.assertEqual(m.pion_red, [(3, 3), (4 ,3), (7, 7), (5, 3)])
        self.assertEqual(m.pion_blue, [(2, 6), (6, 2), (6, 4), (6, 6)])
        self.assertEqual(m.boolRetirer, False)
        self.assertEqual(game.mon_dictionnaire['42'], [(4, 2), False, 0])
        self.assertEqual(m.moulin_déjàfait, [[], [(6, 2), (6, 4), (6, 6)], [(3, 3), (4, 3), (5, 3)]])

    def test_setdict(self):
            #Arrange
            m = game.Moulin()
            #Act
            print(game.mon_dictionnaire)
            self.assertEqual(game.mon_dictionnaire, {'11': [(1, 1), False, 0], '14': [(1, 4), False, 0], '17': [(1, 7), False, 0],
                                                     '22': [(2, 2), False, 0], '24': [(2, 4), False, 0], '26': [(2, 6), True, 2],
                                                     '33': [(3, 3), True, 1], '34': [(3, 4), False, 0], '36': [(3, 5), False, 0],
                                                     '41': [(4, 1), False, 0], '42': [(4, 2), False, 0], '43': [(4, 3), True, 1],
                                                     '45': [(4, 5), False, 0], '46': [(4, 6), False, 0], '47': [(4, 7), False, 0],
                                                     '53': [(5, 3), True, 1], '54': [(5, 4), False, 0], '55': [(5, 5), False, 0],
                                                     '62': [(6, 2), True, 2], '64': [(6, 4), True, 2],'66': [(6, 6), True, 2],
                                                     '71': [(7, 1), False, 0], '74': [(7, 4), False, 0], '77': [(7, 7), True, 2]})

            m.set_dict(1, 1)
            m.set_dict(2, 2)
            m.set_dict(6, 2)
            m.set_dict(5, 5)
            m.set_dict(3, 4)
            m.set_dict(7, 4)
            #Assert
            print(game.mon_dictionnaire)
            print("Vrai : ", game.mon_dictionnaire['62'][1])
            print("Vrai : ", game.mon_dictionnaire['34'][2])
            print("Vrai : ", game.mon_dictionnaire['47'][0])
            self.assertEqual(game.mon_dictionnaire, {'11': [(1, 1), True, 1], '14': [(1, 4), False, 0], '17': [(1, 7), False, 0],
                                                     '22': [(2, 2), True, 2], '24': [(2, 4), False, 0], '26': [(2, 6), True, 2],
                                                     '33': [(3, 3), True, 1], '34': [(3, 4), True, 1], '36': [(3, 5), False, 0],
                                                     '41': [(4, 1), False, 0], '42': [(4, 2), False, 0], '43': [(4, 3), True, 1],
                                                     '45': [(4, 5), False, 0], '46': [(4, 6), False, 0], '47': [(4, 7), False, 0],
                                                     '53': [(5, 3), True, 1], '54': [(5, 4), False, 0], '55': [(5, 5), True, 2],
                                                     '62': [(6, 2), True, 1], '64': [(6, 4), True, 2], '66': [(6, 6), True, 2],
                                                     '71': [(7, 1), False, 0], '74': [(7, 4), True, 2], '77': [(7, 7), True, 2]})
            self.assertEqual(game.mon_dictionnaire['53'], [(5, 3), True, 1])
            self.assertEqual(game.mon_dictionnaire['55'], [(5, 5), True, 2])
            self.assertEqual(game.mon_dictionnaire['62'], [(6, 2), True, 1])
            self.assertEqual(game.mon_dictionnaire['34'][1], True)
            self.assertNotEqual(game.mon_dictionnaire['11'][1], False)
            self.assertEqual(game.mon_dictionnaire['22'][2], 2)
            self.assertEqual(game.mon_dictionnaire['47'][0], (4, 7))
            self.assertNotEqual(game.mon_dictionnaire['74'], [(7, 4), False, 0])
            self.assertNotEqual(game.mon_dictionnaire, False)

    def test_dictreset(self):
        m = game.Moulin()
        game.mon_dictionnaire = {'11': [(1, 1), False, 0], '14': [(1, 4), False, 0], '17': [(1, 7), False, 0],
                                 '22': [(2, 2), False, 0], '24': [(2, 4), False, 0], '26': [(2, 6), False, 0],
                                 '33': [(3, 3), False, 0], '34': [(3, 4), False, 0], '36': [(3, 5), False, 0],
                                 '41': [(4, 1), False, 0], '42': [(4, 2), False, 0], '43': [(4, 3), False, 0],
                                 '45': [(4, 5), False, 0], '46': [(4, 6), False, 0], '47': [(4, 7), False, 0],
                                 '53': [(5, 3), False, 0], '54': [(5, 4), False, 0], '55': [(5, 5), False, 0],
                                 '62': [(6, 2), False, 0], '64': [(6, 4), False, 0], '66': [(6, 6), False, 0],
                                 '71': [(7, 1), False, 0], '74': [(7, 4), False, 0], '77': [(7, 7), False, 0]}
        m.set_dict(1, 1)
        m.set_dict(2, 2)
        m.set_dict(6, 2)
        m.set_dict(5, 5)
        m.set_dict(3, 4)
        m.set_dict(7, 4)
        m.set_dict(4, 1)
        m.set_dict(4, 5)
        m.set_dict(4, 2)
        m.set_dict(4, 6)
        self.assertEqual(game.mon_dictionnaire, {'11': [(1, 1), True, 1], '14': [(1, 4), False, 0], '17': [(1, 7), False, 0],
                                                 '22': [(2, 2), True, 2], '24': [(2, 4), False, 0], '26': [(2, 6), False, 0],
                                                 '33': [(3, 3), False, 0], '34': [(3, 4), True, 1], '36': [(3, 5), False, 0],
                                                 '41': [(4, 1), True, 1], '42': [(4, 2), True, 1], '43': [(4, 3), False, 0],
                                                 '45': [(4, 5), True, 2], '46': [(4, 6), True, 2], '47': [(4, 7), False, 0],
                                                 '53': [(5, 3), False, 0], '54': [(5, 4), False, 0], '55': [(5, 5), True, 2],
                                                 '62': [(6, 2), True, 1], '64': [(6, 4), False, 0], '66': [(6, 6), False, 0],
                                                 '71': [(7, 1), False, 0], '74': [(7, 4), True, 2], '77': [(7, 7), False, 0]})
        self.assertEqual(game.mon_dictionnaire['11'], [(1, 1), True, 1])
        self.assertEqual(game.mon_dictionnaire['74'], [(7, 4), True, 2])
        self.assertEqual(game.mon_dictionnaire['34'][1], True)
        self.assertEqual(game.mon_dictionnaire['42'][1], True)
        self.assertEqual(game.mon_dictionnaire['22'][2], 2)
        self.assertEqual(game.mon_dictionnaire['47'][2], 0)
        self.assertEqual(game.mon_dictionnaire['62'], [(6, 2), True, 1])
        self.assertNotEqual(game.mon_dictionnaire, False)
        m.dict_reset(1, 1)
        m.dict_reset(7, 4)
        m.dict_reset(4, 2)
        m.dict_reset(6, 2)
        m.dict_reset(4, 6)
        m.dict_reset(3, 4)
        #Assert
        print(game.mon_dictionnaire)
        self.assertEqual(game.mon_dictionnaire, {'11': [(1, 1), False, 0], '14': [(1, 4), False, 0], '17': [(1, 7), False, 0],
                                                 '22': [(2, 2), True, 2], '24': [(2, 4), False, 0], '26': [(2, 6), False, 0],
                                                 '33': [(3, 3), False, 0], '34': [(3, 4), False, 0], '36': [(3, 5), False, 0],
                                                 '41': [(4, 1), True, 1], '42': [(4, 2), False, 0], '43': [(4, 3), False, 0],
                                                 '45': [(4, 5), True, 2], '46': [(4, 6), False, 0], '47': [(4, 7), False, 0],
                                                 '53': [(5, 3), False, 0], '54': [(5, 4), False, 0], '55': [(5, 5), True, 2],
                                                 '62': [(6, 2), False, 0], '64': [(6, 4), False, 0], '66': [(6, 6), False, 0],
                                                 '71': [(7, 1), False, 0], '74': [(7, 4), False, 0], '77': [(7, 7), False, 0]})
        self.assertEqual(game.mon_dictionnaire['11'], [(1, 1), False, 0])
        self.assertEqual(game.mon_dictionnaire['74'], [(7, 4), False, 0])
        self.assertEqual(game.mon_dictionnaire['34'][1], False)
        self.assertNotEqual(game.mon_dictionnaire['42'][1], True)
        self.assertEqual(game.mon_dictionnaire['22'], [(2, 2), True, 2])
        self.assertEqual(game.mon_dictionnaire['47'][2], 0)
        self.assertNotEqual(game.mon_dictionnaire['62'], [(6, 2), True, 1])
        self.assertNotEqual(game.mon_dictionnaire, False)


if __name__ == "__main__":
    t = MyTestCase()




