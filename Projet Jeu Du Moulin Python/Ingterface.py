import tkinter
from tkinter import *
import Moteur_new as game

class Appli:
    def __init__(self):

        self.damier = Canvas(width=900, height=500, bg="ivory", borderwidth=5, relief='raised')
        self.damier.pack(side=LEFT, padx=5, pady=5)  # Affiche le Canvas

        self.create()
        self.moteur = game.Moulin()

        """ Variable """
        self.pX = None
        self.pY = None
        self.y = None
        self.x = None
        self.rX = None
        self.rY = None
        self.tourRun = 0
        self.boolPose = True
        self.boolMouv = True
        self.p = [(40, 40, 60, 60),
                  (240, 40, 260, 60),
                  (440, 40, 460, 60),
                  (100, 100, 120, 120),
                  (240, 100, 260, 120),
                  (380, 100, 400, 120),
                  (160, 160, 180, 180),
                  (240, 160, 260, 180),
                  (320, 160, 340, 180),
                  (40, 240, 60, 260),
                  (100, 240, 120, 260),
                  (160, 240, 180, 260),
                  (320, 240, 340, 260),
                  (380, 240, 400, 260),
                  (440, 240, 460, 260),
                  (160, 320, 180, 340),
                  (240, 320, 260, 340),
                  (320, 320, 340, 340),
                  (100, 380, 120, 400),
                  (240, 380, 260, 400),
                  (380, 380, 400, 400),
                  (40, 440, 60, 460),
                  (240, 440, 260, 460),
                  (440, 440, 460, 460), ]

    def lien_entry_position(self):
        print("x : ", self.x)
        print("y : ", self.y)
        if 60 >= self.x >= 40 and 60 >= self.y >= 40:
            self.pX = 1
            self.pY = 1
        elif 260 >= self.x >= 240 and 60 >= self.y >= 40:
            self.pX = 1
            self.pY = 4
        elif 440 <= self.x <= 460 and 40 <= self.y <= 60:
            self.pX = 1
            self.pY = 7
        elif 100 <= self.x <= 120 and 100 <= self.y <= 120:
            self.pX = 2
            self.pY = 2
        elif 240 <= self.x <= 260 and 100 <= self.y <= 120:
            self.pX = 2
            self.pY = 4
        elif 380 <= self.x <= 400 and 100 <= self.y <= 120:
            self.pX = 2
            self.pY = 6
        elif 160 <= self.x <= 180 and 160 <= self.y <= 180:
            self.pX = 3
            self.pY = 3
        elif 240 <= self.x <= 260 and 160 <= self.y <= 180:
            self.pX = 3
            self.pY = 4
        elif 320 <= self.x <= 340 and 160 <= self.y <= 180:
            self.pX = 3
            self.pY = 5
        elif 40 <= self.x <= 60 and 240 <= self.y <= 260:
            self.pX = 4
            self.pY = 1
        elif 100 <= self.x <= 120 and 240 <= self.y <= 260:
            self.pX = 4
            self.pY = 2
        elif 160 <= self.x <= 180 and 240 <= self.y <= 260:
            self.pX = 4
            self.pY = 3
        elif 320 <= self.x <= 340 and 240 <= self.y <= 260:
            self.pX = 4
            self.pY = 5
        elif 380 <= self.x <= 400 and 240 <= self.y <= 260:
            self.pX = 4
            self.pY = 6
        elif 440 <= self.x <= 460 and 240 <= self.y <= 260:
            self.pX = 4
            self.pY = 7
        elif 160 <= self.x <= 180 and 320 <= self.y <= 340:
            self.pX = 5
            self.pY = 3
        elif 240 <= self.x <= 260 and 320 <= self.y <= 340:
            self.pX = 5
            self.pY = 4
        elif 320 <= self.x <= 340 and 320 <= self.y <= 340:
            self.pX = 5
            self.pY = 5
        elif 100 <= self.x <= 120 and 380 <= self.y <= 400:
            self.pX = 6
            self.pY = 2
        elif 240 <= self.x <= 260 and 380 <= self.y <= 400:
            self.pX = 6
            self.pY = 4
        elif 380 <= self.x <= 400 and 380 <= self.y <= 400:
            self.pX = 6
            self.pY = 6
        if 40 <= self.x <= 60 and 440 <= self.y <= 460:
            self.pX = 7
            self.pY = 1
        elif 240 <= self.x <= 260 and 440 <= self.y <= 460:
            self.pX = 7
            self.pY = 4
        elif 440 <= self.x <= 460 and 440 <= self.y <= 460:
            self.pX = 7
            self.pY = 7
        else:
            print('pas de relation')
        print("pX : ", self.pX)
        print("pY : ", self.pY)

    def lien_entry_pion(self, X, Y):
        match X, Y:
            case 1, 1:
                return self.pion11
            case 1, 4:
                return self.pion14
            case 1, 7:
                return self.pion17
            case 2, 2:
                return self.pion22
            case 2, 4:
                return self.pion24
            case 2, 6:
                return self.pion26
            case 3, 3:
                return self.pion33
            case 3, 4:
                return self.pion34
            case 3, 5:
                return self.pion35
            case 4, 1:
                return self.pion41
            case 4, 2:
                return self.pion42
            case 4, 3:
                return self.pion43
            case 4, 5:
                return self.pion45
            case 4, 6:
                return self.pion46
            case 4, 7:
                return self.pion47
            case 5, 3:
                return self.pion53
            case 5, 4:
                return self.pion54
            case 5, 5:
                return self.pion55
            case 6, 2:
                return self.pion62
            case 6, 4:
                return self.pion64
            case 6, 6:
                return self.pion66
            case 7, 1:
                return self.pion71
            case 7, 4:
                return self.pion74
            case 7, 7:
                return self.pion77
            case _:
                return 'pas de relation'

    """ Phase 1 : Pose de pion """
    def piecePose(self, event):
        if self.tourRun <= 7:
            self.damier.itemconfig(self.textRetirer, text=" ")
            item = event.widget.find_closest(event.x, event.y)
            print("boolPose : ", self.boolPose)
            print("e.x : ", event.x)
            print("e.y : ", event.y)
            self.y = event.y
            self.x = event.x
            self.lien_entry_position()
            if self.boolPose:
                self.damier.itemconfigure(item, fill="red")
                self.damier.itemconfig(self.textTour, text="Au tour du player 2")
                self.damier.itemconfig(self.textTour, fill="blue")
                self.damier.itemconfig(self.textTour, font=('Pursia', 25, "bold italic"))
                self.moteur.pose(self.pX, self.pY)
                self.boolPose = False
            else:
                self.damier.itemconfigure(item, fill="blue")
                self.damier.itemconfig(self.textTour, text="Au tour du player 1")
                self.damier.itemconfig(self.textTour, fill="red")
                self.damier.itemconfig(self.textTour, font=('Pursia', 25, "bold italic"))
                self.moteur.pose(self.pX, self.pY)
                self.boolPose = True
            self.tourRun += 1
            print("boolR avant : ", self.moteur.boolRetirer)
            self.moteur.verif_moulinfait()
            print("boolR apres : ", self.moteur.boolRetirer)
            if self.moteur.boolRetirer:
                self.damier.itemconfig(self.textRetirer, text="Retirez un pion à votre adversaire")
                self.damier.itemconfig(self.textTour, text="Ton adversaire a réalisé un MOULIN")
                self.damier.itemconfig(self.textTour, font=('Pursia', 15, "bold italic"))
            else:
                print("Pas de Moulin")
        else:
            self.textMouv = self.damier.create_text(680, 90, text="Phase de mouvement", fill="black",
                                                    font=('Pursia', 25, "bold italic"))
        print(self.tourRun)

    """ Phase 2 : Mouvement de pion """
    def pieceMouv(self, entryX1, entryY1, entryX2, entryY2):
        X1 = int(entryX1.get())
        print(X1)
        Y1 = int(entryY1.get())
        print(Y1)
        X2 = int(entryX2.get())
        print(X2)
        Y2 = int(entryY2.get())
        print(Y2)
        if self.boolMouv:
            self.damier.itemconfig(self.lien_entry_pion(X2, Y2), fill="red")
            self.damier.itemconfig(self.textTour, fill="blue")
            self.damier.itemconfig(self.textTour, text="Au tour du player 2")
            self.damier.itemconfig(self.textTour, font=('Pursia', 25, "bold italic"))
            self.boolMouv = False
        else:
            self.damier.itemconfig(self.lien_entry_pion(X2, Y2), fill="blue")
            self.damier.itemconfig(self.textTour, fill="red")
            self.damier.itemconfig(self.textTour, text="Au tour du player 1")
            self.damier.itemconfig(self.textTour, font=('Pursia', 25, "bold italic"))
            self.boolMouv = True
        self.damier.itemconfig(self.lien_entry_pion(X1, Y1), fill="white")
        self.moteur.mouvement(X1, Y1, X2, Y2)
        print("boolR avant : ", self.moteur.boolRetirer)
        self.moteur.verif_moulinfait()
        print("boolR apres : ", self.moteur.boolRetirer)
        if self.moteur.boolRetirer:
            self.damier.itemconfig(self.textRetirer, text="Retirez un pion à votre adversaire")
            self.damier.itemconfig(self.textTour, text="Ton adversaire a réalisé un MOULIN")
            self.damier.itemconfig(self.textTour, font = ('Pursia', 15, "bold italic"))
        else:
            print("Pas de Moulin")
        if len(self.moteur.pion_blue) == 2 or len(self.moteur.pion_red) == 2:
            return self.damier.create_text(400, 250, text="Game over",
                                fill="red",
                                font=('Pursia', 70, "bold italic"))

    def pieceRetirer(self, entryX3, entryY3):
        X3 = int(entryX3.get())
        print(X3)
        Y3 = int(entryY3.get())
        print(Y3)
        self.lien_entry_position()
        self.damier.itemconfigure(self.lien_entry_pion(X3, Y3), fill="white")
        self.moteur.retirer_pion(X3, Y3)
        print("boolR apres retirer : ", self.moteur.boolRetirer)
        self.damier.itemconfig(self.textRetirer, text=" ")
        self.damier.itemconfig(self.textTour, text="A ton tour de poser un pion")

    def create(self):

        self.p = [(40, 40, 60, 60),
                  (240, 40, 260, 60),
                  (440, 40, 460, 60),
                  (100, 100, 120, 120),
                  (240, 100, 260, 120),
                  (380, 100, 400, 120),
                  (160, 160, 180, 180),
                  (240, 160, 260, 180),
                  (320, 160, 340, 180),
                  (40, 240, 60, 260),
                  (100, 240, 120, 260),
                  (160, 240, 180, 260),
                  (320, 240, 340, 260),
                  (380, 240, 400, 260),
                  (440, 240, 460, 260),
                  (160, 320, 180, 340),
                  (240, 320, 260, 340),
                  (320, 320, 340, 340),
                  (100, 380, 120, 400),
                  (240, 380, 260, 400),
                  (380, 380, 400, 400),
                  (40, 440, 60, 460),
                  (240, 440, 260, 460),
                  (440, 440, 460, 460), ]

        """ Création des rectangles """
        self.damier.create_rectangle(50, 50, 450, 450)
        self.damier.create_rectangle(110, 110, 390, 390)
        self.damier.create_rectangle(170, 170, 330, 330)

        """ Création des lignes """
        self.damier.create_line(50, 250, 170, 250)
        self.damier.create_line(330, 250, 450, 250)
        self.damier.create_line(250, 50, 250, 170)
        self.damier.create_line(250, 330, 250, 450)
        self.damier.create_rectangle(500, 465, 800, 485, outline="green")

        """ Création des pions """
        self.pion11 = self.damier.create_oval(self.p[0], fill='white')
        self.pion14 = self.damier.create_oval(self.p[1], fill='white')
        self.pion17 = self.damier.create_oval(self.p[2], fill='white')
        self.pion22 = self.damier.create_oval(self.p[3], fill='white')
        self.pion24 = self.damier.create_oval(self.p[4], fill='white')
        self.pion26 = self.damier.create_oval(self.p[5], fill='white')
        self.pion33 = self.damier.create_oval(self.p[6], fill='white')
        self.pion34 = self.damier.create_oval(self.p[7], fill='white')
        self.pion35 = self.damier.create_oval(self.p[8], fill='white')
        self.pion41 = self.damier.create_oval(self.p[9], fill='white')
        self.pion42 = self.damier.create_oval(self.p[10], fill='white')
        self.pion43 = self.damier.create_oval(self.p[11], fill='white')
        self.pion45 = self.damier.create_oval(self.p[12], fill='white')
        self.pion46 = self.damier.create_oval(self.p[13], fill='white')
        self.pion47 = self.damier.create_oval(self.p[14], fill='white')
        self.pion53 = self.damier.create_oval(self.p[15], fill='white')
        self.pion54 = self.damier.create_oval(self.p[16], fill='white')
        self.pion55 = self.damier.create_oval(self.p[17], fill='white')
        self.pion62 = self.damier.create_oval(self.p[18], fill='white')
        self.pion64 = self.damier.create_oval(self.p[19], fill='white')
        self.pion66 = self.damier.create_oval(self.p[20], fill='white')
        self.pion71 = self.damier.create_oval(self.p[21], fill='white')
        self.pion74 = self.damier.create_oval(self.p[22], fill='white')
        self.pion77 = self.damier.create_oval(self.p[23], fill='white')

        """ Création tag_bind """
        self.damier.tag_bind(self.pion11, '<Button>', func=self.piecePose)
        self.damier.tag_bind(self.pion14, '<Button>', func=self.piecePose)
        self.damier.tag_bind(self.pion17, '<Button>', func=self.piecePose)
        self.damier.tag_bind(self.pion22, '<Button>', func=self.piecePose)
        self.damier.tag_bind(self.pion24, '<Button>', func=self.piecePose)
        self.damier.tag_bind(self.pion26, '<Button>', func=self.piecePose)
        self.damier.tag_bind(self.pion33, '<Button>', func=self.piecePose)
        self.damier.tag_bind(self.pion34, '<Button>', func=self.piecePose)
        self.damier.tag_bind(self.pion35, '<Button>', func=self.piecePose)
        self.damier.tag_bind(self.pion41, '<Button>', func=self.piecePose)
        self.damier.tag_bind(self.pion42, '<Button>', func=self.piecePose)
        self.damier.tag_bind(self.pion43, '<Button>', func=self.piecePose)
        self.damier.tag_bind(self.pion45, '<Button>', func=self.piecePose)
        self.damier.tag_bind(self.pion46, '<Button>', func=self.piecePose)
        self.damier.tag_bind(self.pion47, '<Button>', func=self.piecePose)
        self.damier.tag_bind(self.pion53, '<Button>', func=self.piecePose)
        self.damier.tag_bind(self.pion54, '<Button>', func=self.piecePose)
        self.damier.tag_bind(self.pion55, '<Button>', func=self.piecePose)
        self.damier.tag_bind(self.pion62, '<Button>', func=self.piecePose)
        self.damier.tag_bind(self.pion64, '<Button>', func=self.piecePose)
        self.damier.tag_bind(self.pion66, '<Button>', func=self.piecePose)
        self.damier.tag_bind(self.pion71, '<Button>', func=self.piecePose)
        self.damier.tag_bind(self.pion74, '<Button>', func=self.piecePose)
        self.damier.tag_bind(self.pion77, '<Button>', func=self.piecePose)

        """ Saisie du text """
        self.textTour = self.damier.create_text(680, 425, text="Au tour du player 1", fill="red",
                                                font=('Pursia', 25, "bold italic"))
        self.textRetirer = self.damier.create_text(680, 275, text=" ",
                                                   fill="black",
                                                   font=('Pursia', 20, "bold italic"))
        self.damier.create_text(650, 475, text="Ne pas oubliez de vider le champ après le click",
                                                   fill="Green",
                                                   font=('Pursia', 10, "bold italic"))

        """ Text Pion """
        self.damier.create_text(35, 35, text="1.1", fill="black", font=('Pursia', 7, "bold italic"))
        self.damier.create_text(235, 35, text="1.4", fill="black", font=('Pursia', 7, "bold italic"))
        self.damier.create_text(435, 35, text="1.7", fill="black", font=('Pursia', 7, "bold italic"))
        self.damier.create_text(95, 95, text="2.2", fill="black", font=('Pursia', 7, "bold italic"))
        self.damier.create_text(235, 95, text="2.4", fill="black", font=('Pursia', 7, "bold italic"))
        self.damier.create_text(375, 95, text="2.7", fill="black", font=('Pursia', 7, "bold italic"))
        self.damier.create_text(155, 155, text="3.3", fill="black", font=('Pursia', 7, "bold italic"))
        self.damier.create_text(235, 155, text="3.4", fill="black", font=('Pursia', 7, "bold italic"))
        self.damier.create_text(315, 155, text="3.5", fill="black", font=('Pursia', 7, "bold italic"))
        self.damier.create_text(35, 235, text="4.1", fill="black", font=('Pursia', 7, "bold italic"))
        self.damier.create_text(95, 235, text="4.2", fill="black", font=('Pursia', 7, "bold italic"))
        self.damier.create_text(155, 235, text="4.3", fill="black", font=('Pursia', 7, "bold italic"))
        self.damier.create_text(315, 235, text="4.5", fill="black", font=('Pursia', 7, "bold italic"))
        self.damier.create_text(375, 235, text="4.6", fill="black", font=('Pursia', 7, "bold italic"))
        self.damier.create_text(435, 235, text="4.7", fill="black", font=('Pursia', 7, "bold italic"))
        self.damier.create_text(155, 315, text="5.3", fill="black", font=('Pursia', 7, "bold italic"))
        self.damier.create_text(235, 315, text="5.4", fill="black", font=('Pursia', 7, "bold italic"))
        self.damier.create_text(315, 315, text="5.5", fill="black", font=('Pursia', 7, "bold italic"))
        self.damier.create_text(95, 380, text="6.2", fill="black", font=('Pursia', 7, "bold italic"))
        self.damier.create_text(235, 380, text="6.4", fill="black", font=('Pursia', 7, "bold italic"))
        self.damier.create_text(375, 380, text="6.6", fill="black", font=('Pursia', 7, "bold italic"))
        self.damier.create_text(35, 440, text="7.1", fill="black", font=('Pursia', 7, "bold italic"))
        self.damier.create_text(235, 440, text="7.4", fill="black", font=('Pursia', 7, "bold italic"))
        self.damier.create_text(435, 440, text="7.7", fill="black", font=('Pursia', 7, "bold italic"))

        """ Saisie du player 1 """
        self.textP1_1 = self.damier.create_text(600, 150, text="Saisir la valeur de X de départ : ",
                                                font=('Pursia', 9, "bold italic"))
        self.entryX1 = tkinter.Entry()
        self.champ1_1 = self.damier.create_window(755, 150, window=self.entryX1)

        self.textP1_2 = self.damier.create_text(600, 175, text="Saisir la valeur de Y de départ : ",
                                                font=('Pursia', 9, "bold italic"))
        self.entryY1 = tkinter.Entry()
        self.champ1_2 = self.damier.create_window(755, 175, window=self.entryY1)

        """ Saisie du player 2 """
        self.textP2_1 = self.damier.create_text(600, 200, text="Saisir la valeur de X d'arrivée : ",
                                                font=('Pursia', 9, "bold italic"))
        self.entryX2 = tkinter.Entry()
        self.champ2_1 = self.damier.create_window(755, 200, window=self.entryX2)

        self.textP2_2 = self.damier.create_text(600, 225, text="Saisir la valeur de Y d'arrivée : ",
                                                font=('Pursia', 9, "bold italic"))
        self.entryY2 = tkinter.Entry()
        self.champ2_2=self.damier.create_window(755, 225, window=self.entryY2)

        """" Button click """
        button1 = tkinter.Button(text='Ok',
                                 command=lambda: self.pieceMouv(self.entryX1, self.entryY1, self.entryX2, self.entryY2),
                                 font=('Pursia', 13, "bold italic"))
        self.damier.create_window(850, 190, window=button1)
        button2 = tkinter.Button(text='Ok',
                                 command=lambda: self.pieceRetirer(self.entryX3, self.entryY3),
                                 font=('Pursia', 13, "bold italic"))
        self.damier.create_window(850, 337.5, window=button2)
        button2 = tkinter.Button(text='Quitter', command=self.damier.destroy)
        button2.pack(side=BOTTOM)
        self.damier.create_window(860, 475, window=button2)

        """ Saisie du pion à retirer """
        self.textP3_1 = self.damier.create_text(585, 325, text="Saisir la valeur de X du pion à retirer : ",
                                                font=('Pursia', 9, "bold italic"))
        self.entryX3 = tkinter.Entry()
        self.damier.create_window(755, 325, window=self.entryX3)

        self.textP3_2 = self.damier.create_text(585, 350, text="Saisir la valeur de Y du pion à retirer : ",
                                                font=('Pursia', 9, "bold italic"))
        self.entryY3 = tkinter.Entry()
        self.damier.create_window(755, 350, window=self.entryY3)


if __name__ == "__main__":
    master = Tk()
    m = Appli()
    master.title("Jeu du Moulin")
    mainloop()
