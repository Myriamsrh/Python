import unittest
from Ia14M import Ia14M

#nota toujour penser a mettre la partie execution qui se trouve dans l'objet 
# style instentiation de l'objet utilisation des methode sinon il vas les lancer
# et on ne verra pas les test

class MyTest(unittest.TestCase):

    def setUp(self):
        self.s = Ia14M()
    

    @unittest.skip("showing class skipping")
    def testNew_game1(self):
        self.assertEqual(self.s.new_game(True), (self.s.val == 0))
        self.assertEqual(self.s.new_game(False), (self.s.val == 1))


    #@unittest.skip("showing class skipping")
    def testPlayer_sets(self):
        #remplissage de donnee
        self.s.jeuIa.append((2, 2))
        self.s.jeuxGlobal.append((2, 2))
        self.s.jeuIaX.append(2)
        self.s.jeuIaY.append(2)
        #action de la fonction
        self.s.player_sets(1, 1, 2, 2)
        #resultats attendu
        self.assertEqual(self.s.adv, [(1,1)])
        self.assertEqual(self.s.advX, [1])
        self.assertEqual(self.s.advY, [1])

        self.assertEqual(self.s.jeuIa, [])
        self.assertEqual(self.s.jeuIaX, [])
        self.assertEqual(self.s.jeuIaY, [])
        self.assertEqual(self.s.jeuxGlobal, [(1,1)])


    @unittest.skip("showing class skipping")
    def testPlayer_moves(self):
        pass

    
    @unittest.skip("showing class skipping")
    def testSet(self):
        pass

    
    @unittest.skip("showing class skipping")
    def testMove(self):
        pass

    
    @unittest.skip("showing class skipping")
    def testPlay(self):
        pass

    
    #@unittest.skip("showing class skipping")
    def testIaTour1(self):

        if self.s.adv.append((7,1)):
            self.assertEqual(self.s.IaTour1, self.s.jeuIa == [(6,2)])
        if self.s.adv.append((7,7)):
            self.assertEqual(self.s.IaTour1, self.s.jeuIa == [(4,1)])
        if self.s.adv.append((6,2)):
            self.assertEqual(self.s.IaTour1, self.s.jeuIa == [(1,7)])
        if self.s.adv.append((6,6)):
            self.assertEqual(self.s.IaTour1, self.s.jeuIa == [(4,2)])
        
        if self.s.jeuIa.append((7,1)):
            self.assertEqual(self.s.IaTour1, self.s.jeuIa == [(7,4)])
        if self.s.jeuIa.append((6,2)):
            self.assertEqual(self.s.IaTour1, self.s.jeuIa == [(6,4)])
        if self.s.jeuIa.append((1,7)):
            self.assertEqual(self.s.IaTour1, self.s.jeuIa == [(1,4)])
        
        if self.s.jeuIa.append((7,1)):
            if self.s.adv.append((7,7)):
                self.assertEqual(self.s.IaTour1, self.s.jeuIa == [(4,1)])
        if self.s.jeuIa.append((6,2)):
            if self.s.adv.append((6,6)):
                self.assertEqual(self.s.IaTour1, self.s.jeuIa == [(4,2)])
        if self.s.jeuIa.append((1,7)):
            if self.s.adv.append((1,1)):
                self.assertEqual(self.s.IaTour1, self.s.jeuIa == [(4,7)])
    
    
    @unittest.skip("showing class skipping")
    def testIaTour2(self):
        pass

    @unittest.skip("showing class skipping")
    def testIaTour3(self):
        pass

    @unittest.skip("showing class skipping")
    def testIaTour4(self):
        pass

    @unittest.skip("showing class skipping")
    def testIaTour5(self):
        pass

    @unittest.skip("showing class skipping")
    def testIaTour6(self):
        pass

    @unittest.skip("showing class skipping")
    def testIaTour7(self):
        pass

    @unittest.skip("showing class skipping")
    def testIaTour8(self):
        pass

    @unittest.skip("showing class skipping")
    def testIaTour9(self):
        pass
    
    
    @unittest.skip("showing class skipping")
    def testIaMove1(self):
        pass



if __name__ == '__main__':
    unittest.main()