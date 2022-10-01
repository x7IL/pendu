while True:
    devine = input("Choisir un mot a deviner:").lower()
    if not devine.isalpha():
        print("choissisez un mot sans chiffre, sans caracteres speciaux ou bien avec accent")
        continue
    else:
        break

s = devine[0]
e = devine[-1]
longueur = len(devine)

cacher = ["_" for i in range(longueur)]
cacher[0] = s
cacher[-1] = e

for i in range(longueur):
    if devine[i] == s:
        cacher[i] = s
    elif devine[i] == e:
        cacher[i] = e


complet = ["#############", #13
           "    #    #   ",
           "    #    #   ",
           "   ###   #   ",
           "  #   #  #   ",
           "   ###   #   ",
           "    #    #   ",
           "   ###   #   ",
           "  # # #  #   ",
           "    #    #   ",
           "   # #   #   ",
           "  #   #  #   ",
           " ####### #   ",
           " #     # #   ",
           "#############",]  # 15

vie = 0
mort = 0

def afficher(tab):

    for i in range(len(tab)):
        print(tab[i])

vide = [" " for i in range(15)]

faux = []

while True:
    print("".join(cacher))
    lettre = input("\n\nSaisir une lettre:")
    print("liste des lettres utilisé:",faux)

    if lettre.isalpha():
        if len(lettre) == 1:
            if lettre.lower() in faux:
                print("la lettre a déjà été utilisé")
                print("la liste :", faux)
            else:
                vrai = True
                for i in range(longueur):
                    if lettre.lower() == devine[i]:
                        cacher[i] = lettre.lower()
                        vrai = False
                if vrai:
                    print("la lettre ne se trouve pas dans le mot")
                    faux.append(lettre)
                    mort += 1
                    vie += 1
                elif not vrai:
                    print("La lettre s'y trouve :", "".join(cacher))
                    faux.append(lettre.lower())

        else:
            print("Il faut saisir une lettre !")
    else:
        print("Il faut seulement saisir ds lettres")

    if mort==1:
        vide[14] = complet[14]
    elif mort == 2:
        vide[13] = "         #   "
        vide[12] = "         #   "
        vide[11] = "         #   "
        vide[10] = "         #   "
        vide[9] = "         #   "
        vide[8] = "         #   "
        vide[7] = "         #   "
        vide[6] = "         #   "
        vide[5] = "         #   "
        vide[4] = "         #   "
        vide[3] = "         #   "
        vide[2] = "         #   "
        vide[1] = "         #   "
    elif mort == 3:
        vide[0] = complet[0]
    elif mort == 4:
        vide[13] = " #     # #   "
        vide[12] = " ####### #   "
    elif mort == 5:
        vide[1] = "    #    #   "
        vide[2] = "    #    #   "
    elif mort == 6:
        vide[3] = "   ###   #   "
        vide[4] = "  #   #  #   "
        vide[5] = "   ###   #   "

    elif mort == 7:
        vide[6] = "    #    #   "
        vide[7] = "    #    #   "
        vide[8] = "    #    #   "
        vide[9] = "    #    #   "

    elif mort == 8:
        vide[7] = "   ##    #   "
        vide[8] = "  # #    #   "

    elif mort == 9:
        vide[7] = "   ###   #   "
        vide[8] = "  # # #  #   "
    elif mort == 10:
        vide[10] = "   #     #   "
        vide[11] = "  #      #   "
    elif mort == 11:
        vide[10] = "   # #   #   "
        vide[11] = "  #   #  #   "
    elif mort == 12:
        vide[13] = "         #   "
        vide[12] = "         #   "

    afficher(vide)
    print("\n")

    if devine == "".join(cacher):
        print("C'est gagné! le mot etait,", devine)
        break
    elif vie == 12:
        print("C'est perdu, il a été pendu,, le mot était",devine)
        break