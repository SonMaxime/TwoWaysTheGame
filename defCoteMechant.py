from random import randint
import index
pdv_joueur = index.pdv_joueur
ancien_pdv = index.ancien_pdv
pdv_capitaine = index.pdv_capitaine


def combat_pirates():
    global pdv_joueur,pdv_capitaine,ancien_pdv
    
    print("Vous choississez de vous cacher dans un bateau pour vous introduire dans la cité Marseillaise")
    input("")
    print("Vous vous rendez compte que ce bateau est un navire pirate, le capitaine nommé Awarigum vous trouve et vous menace")
    print("Le capitaine étant joueur il vous propose une énigme si vous arrivez a répondre il vous ramène a bon port sinon...")
    input("")
    reponse_enigme=input("Qu'est ce qui est trop chaud et trop frais en même temps ? :")
    if reponse_enigme=="Le capitaine":
        print("Soit vous avez triché soit vous êtes trop intelligent pour ce jeu, aller travailler dans la vraie vie")
    else:
        print("Eh malheureusement non, la réponse était Le capitaine, vous êtes nul vous méritez la mort")
        print("Le capitaine brandit son épee magique a énigmes et vous prend en duel !")
        input("")
        print("La seule manière d'esquiver les coups ,et de répondre correctement aux questions données par l'épée elle même.(sans article et sans majuscule)")
        input("")
    
        while pdv_joueur>0 and pdv_capitaine>0:
            print("La capitaine vous frappe,vous entendez une voix au plus profond de vous")
            input("")
            print("...")
            input("")
            print("Qu'est c-")
            print("Qu'est ce qui est-")
            def enigme_capitaine(enigme,reponse):
                global pdv_joueur,pdv_capitaine,ancien_pdv
                enigme=input(enigme)
                if reponse==enigme:
                    print("Bien joué ! Vous ne perdez aucun point de vie !")
                if reponse !=enigme:
                    degats_du_capitaine = randint(10,25)
                    pdv_joueur = pdv_joueur - degats_du_capitaine
                    ancien_pdv = pdv_joueur + degats_du_capitaine
                    print("C'est faux ! Vous perdez", degats_du_capitaine, "points de vie.Vous passez de",ancien_pdv,"à",pdv_joueur)
                return ("") 
            print(enigme_capitaine("Qu'est ce qui est jaune et qui attend ?","johnatan"))
            input("")
            print("C'est a vous d'attaquer ! :")
            def combat_capitaine():
                global pdv_joueur,pdv_capitaine,ancien_pdv
                coup=input("1:Uppercut  2:Coup de pied : ")
                if coup=="1":
                    print("Vous tentez un uppercut ! Votre coup est tres puissant mais il a une chance sur 2 de rater !")
                    uppercut=randint(1,2)
                    if uppercut==1:
                        perte_vie_capitaine=randint(50,80)
                        pdv_capitaine+=-perte_vie_capitaine
                        print("Vous avez de la chance cela fonctionne, le capitaine perd",perte_vie_capitaine,"point de vie, il est a",pdv_capitaine)
                    if uppercut==2:
                        print("Malheureusement vous n'avez pas de chance, le capitaine ne perd aucun point de vie, il en a",pdv_capitaine)
                if coup == "2":
                    print("Vous tapez de toutes vos forces sur la jambe en bois du capitaine, il tombe au sol !")
                    perte_vie_capitaine=randint(50,80)
                    pdv_capitaine = pdv_capitaine - perte_vie_capitaine
                    print("Vous lui avez fait perdre",perte_vie_capitaine,"point de vie, il est a",pdv_capitaine)
                return("")
            combat_capitaine()
            enigme_capitaine("On peut me trouver au fond d'un bateau de pêche ou au milieu d'un court de tennis.","filet")        
            combat_capitaine()