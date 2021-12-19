from random import randint
from time import sleep
import index # Import du fichier principal qui contient toutes les variables et la fonction clear

def batailleN1(): # Fonction de la 1ère bataille du jeu en tant que héros.
  print("Très bien.")
  sleep(1)
  index.clear()
  print("L'ennemi se trouvenant devant vous se situe au niveau 1, de quoi pouvoir le battre à mains nu, ses PV sont de 150 et la seule arme que vous possédez sont vos poings.")
  pvEnnemi1 = 150 # PV de l'ennemi n°1
  while pvEnnemi1 > 0 and index.pdv_joueur > 0: # Tant que les pv de l'ennemi ne sont pas à 0 et ceux du joueur au dessus de 0
    choixAttaqueEnnemi1 = int(input("Attaquer ?\n1.Oui      2.Fuir: "))
    if choixAttaqueEnnemi1 == 1: # SI le joueur attaque
      attaqueContreEnnemi1 = randint(30, 50) # Dégats random entre 30 et 50
      pvEnnemi1 = pvEnnemi1 - attaqueContreEnnemi1 # Affligement des dégats à l'ennemi
      if pvEnnemi1 > 0: # Si les PV de l'ennemi sont encore au dessus de 0
        print("Vous avez infligé", attaqueContreEnnemi1, "PV à votre ennemi, il en possède désormais", pvEnnemi1 , "et ce dernier décide faire de même.")
        attaqueEnnemi1Réussie = randint(1, 2) # Savoir si l'ennemi reéussira à contre-attaquer
        if attaqueEnnemi1Réussie == 1: # Si contre attaque réussie
          degatsInfligéJoueur = randint(25, 30) # Dégats random entre 25 et 30
          index.pdv_joueur = index.pdv_joueur - degatsInfligéJoueur # Affligement des dégats au joueur
          if index.pdv_joueur > 0: # Si les PV du jouer sont toujours au dessus de 0
            print("Il ne vous a pas manqué, vous êtes désormais à", index.pdv_joueur, "PV")
            sleep(2)
            index.clear()
          elif index.pdv_joueur < 0: # Dans le cas inverse
            print("Il ne vous a pas manqué, vous êtes désormais à", index.pdv_joueur, "PV, vous êtes donc mort et votre aventure s'arrête ici.")
            break # Le jeu s'arrête
        elif attaqueEnnemi1Réussie == 2: # Dans le cas où l'ennemi rate son attaque.
          print("Mais cela fût un échec, il vous a raté.")
          sleep(2)
          index.clear()
      elif pvEnnemi1 <= 0: # Si les PV de l'ennemi sont à 0
        print("Vous avez infligé", attaqueContreEnnemi1, "PV à votre ennemi, il en possède désormais", pvEnnemi1 , "vous l'avez donc vaincu.")
        index.victoireBatailleN1 = 1 # Indique au fichier index.py que le combat a été remporté
        sleep(5)
    elif choixAttaqueEnnemi1 == 2: # Si le joueur décide de fuir le combat
      print("Vous avez décidé de fuir le combat, vous auriez eu peu de chances de vous en sortir.")
      sleep(5)

def fuireBatailleN1(): # Fonction activé si le joueur décide de fuire le 1er combat (PS: très peu recommandé)
  print("Vous decidez de partir très loin en courrant. Vous auriez eu peu de chance...")
  sleep(3)

def forgeronN1(): # Fonction qui permets de nous rends chez le forgeron après la victoire de la 1ere bataille si ce dernier accepte
  print("Vous avez gagné votre 1er combat, vous repartez avec une épée de 1er niveau, vous êtes désormais armé et prêt à affronter de nouveaux ennemis de manière sure.")
  sleep(3)
    
  print("Cependant, étant donné qu'il s'agit d'une arme de bas niveau, et qu'elle fût usé auparavant , celle-ci peut se dégrader très rapide, il va faloir être précis et dans vos coups.")
  sleep(3)
  print("Vous pouvez toujours régénérer cette dernière en rendant visite à un forgeron à l'aide des", index.portefeuille, "écumes dont le royaume vous a fait crédit.")
  input("")
  index.clear()
  seRendreAuForgeronN1 = int(input("Voulez-vous vous rendre au forgeron pour réparer votre arme ?\n1. Oui               2. Non: "))
  if seRendreAuForgeronN1 == 1:
    print(f'\033[3mBienvenue jeune chevalier, que puis-je pour toi ?\033[0m')
    sleep(1)
    print(f'\033[3mOh mais que vois-je ? Ton épée ne serait-elle pas en pitoieuse état ?\033[0m')
    sleep(1)
    print(f'\033[3mJe peux te la réparer si tu le souhaites.\033[0m')
    sleep(1)
    réparerEpée1 = int(input(f'\033[3mVeux tu que je le fasses ? \n1. Oui       2.Non: \033[0m'))
    if réparerEpée1 == 1:
      print(f'\033[3mParfait ! Etant donné que tu est chevalier pro. et non amateur, je te propose volontier de te la réparer pour rien du tout !\033[0m')
      for i in range(3):
        print(".", end="")
        sleep(1)
      sleep(3)
      print(f'\033[3mEt voilà le travail, ton épée est désormais à\033[0m', index.pvépée, f'\033[3mPV !\033[0m')
    elif réparerEpée1 == 2:
      print("Dommage.")
  elif seRendreAuForgeronN1 == 2:
    print("Vous avez décidé de ne pas faire inspecter votre arme chez le forgeron, votre épée est encore donc dans un pitoyable état, mais devrai être suffisant pour éliminer de faibles ennemis.")