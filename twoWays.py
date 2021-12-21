from random import randint
from time import sleep # Pour effectuer un temps de pause entre les différents print() et clear()
import os
import cotéMéchant

def clear(): # Cette fonction permettera au code d'éviter de surcharger la console, donc de la nettoyer complètement afin rendre celle-ci plus légère et agréable pendant l'aventure.
  if os.name == "posix": # Si le code fontionne sur une plateforme Linux
    os.system('clear') # Commande clear sur Linux
  elif os.name in ("nt", "dos", "ce"): # Si le code fontionne sur une plateforme Windows
    os.system('CLS') # Commande clear sur Windows
  # Ces deux conditions permettent à la fonction de s'éxécuter sans problème sur les deux platformes

portefeuille = 50 # Portefeuille du joueur, initiallement définis sur 50 écumes (la monnaie qui sera utilisée dans le jeu).
pdv_joueur = 100 # PV du joueur, on débute à 100.
lvl = 1 # Niveau du joueur, on débute à 1.
épée = 1 # Niveau de l'épée du héros.
pvépée = 57 # Points de vie de l'épée du héros.

ancien_pdv=100
pdv_capitaine=300

def bataille(): # Fonction de la 1ère bataille du jeu en tant que héros.
  global pdv_joueur
  print("Très bien.")
  sleep(1)
  clear()
  print("L'ennemi se trouvenant devant vous se situe au niveau 1, de quoi pouvoir le battre à mains nu, ses PV sont de 150 et la seule arme que vous possédez sont vos poings.")
  pvEnnemi1 = 150 # PV de l'ennemi n°1
  while pvEnnemi1 > 0 and pdv_joueur > 0: # Tant que les pv de l'ennemi ne sont pas à 0 et ceux du joueur au dessus de 0
    choixAttaqueEnnemi1 = int(input("Attaquer ?\n1.Oui      2.Fuir: "))
    if choixAttaqueEnnemi1 == 1: # SI le joueur attaque
      attaqueContreEnnemi1 = randint(30, 50) # Dégats random entre 30 et 50
      pvEnnemi1 = pvEnnemi1 - attaqueContreEnnemi1 # Affligement des dégats à l'ennemi
      if pvEnnemi1 > 0: # Si les PV de l'ennemi sont encore au dessus de 0
        print("Vous avez infligé", attaqueContreEnnemi1, "PV à votre ennemi, il en possède désormais", pvEnnemi1 , "et ce dernier décide faire de même.")
        attaqueEnnemi1Réussie = randint(1, 2) # Savoir si l'ennemi reéussira à contre-attaquer
        if attaqueEnnemi1Réussie == 1: # Si contre attaque réussie
          degatsInfligéJoueur = randint(25, 30) # Dégats random entre 25 et 30
          pdv_joueur = pdv_joueur - degatsInfligéJoueur # Affligement des dégats au joueur
          if pdv_joueur > 0: # Si les PV du jouer sont toujours au dessus de 0
            print("Il ne vous a pas manqué, vous êtes désormais à", pdv_joueur, "PV")
            input("")
            clear()
          elif pdv_joueur < 0: # Dans le cas inverse
            print("Il ne vous a pas manqué, vous êtes désormais à", pdv_joueur, "PV, vous êtes donc mort et votre aventure s'arrête ici.")
            break # Le jeu s'arrête
        elif attaqueEnnemi1Réussie == 2: # Dans le cas où l'ennemi rate son attaque.
          print("Mais cela fût un échec, il vous a raté.")
          input("")
          clear()
      elif pvEnnemi1 <= 0: # Si les PV de l'ennemi sont à 0
        print("Vous avez infligé", attaqueContreEnnemi1, "PV à votre ennemi, il en possède désormais", pvEnnemi1 , "vous l'avez donc vaincu.")
        victoireBatailleN1 = 1
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
    
  print("Cependant, étant donné qu'il s'agit d'une arme de bas niveau, et qu'elle fût usé auparavant , celle-ci peut se dégrader très rapidement, il va faloir être précis et agréssif dans vos coups.")
  sleep(3)
  print("Vous pouvez toujours régénérer cette dernière en rendant visite à un forgeron à l'aide des", portefeuille, "écumes dont le royaume vous a fait crédit.")
  input("")
  clear()

  seRendreAuForgeronN1 = int(input("Voulez-vous vous rendre au forgeron pour réparer votre arme ?\n1. Oui               2. Non: "))
  if seRendreAuForgeronN1 == 1:
    print(f'\033[3mBienvenue jeune chevalier, que puis-je pour vous ?\033[0m')
    sleep(1)
    print(f'\033[3mOh mais que vois-je ? Votre épée ne serait-elle pas en pitoieuse état ?\033[0m')
    sleep(1)
    print(f'\033[3mJe peux vous la réparer si vous le souhaitez.\033[0m')
    sleep(1)
    réparerEpée1 = int(input(f'\033[3mSouhaitez-vous que je le fasses ? \n1. Oui       2.Non: \033[0m'))
    if réparerEpée1 == 1:
      print(f'\033[3mParfait ! Etant donné que vous êtes le chevalier le plus réputé du royaume, je vous propose volontier de vous la réparer pour rien du tout !\033[0m')
      for i in range(3):
        print(".", end="")
        sleep(1)
      pvépée = 100
      print("Félicitations, votre épée possède désormais", pvépée, "PV.")
      input("")
    elif réparerEpée1 == 2:
      print("Dommage.")
  elif seRendreAuForgeronN1 == 2:
    print("Vous avez décidé de ne pas faire inspecter votre arme chez le forgeron, votre épée est encore donc dans un pitoyable état, mais devrai être suffisant pour éliminer de faibles ennemis.")

def enigme1gagné():
  global portefeuille
  print("Vous avez remporté la 1ère énigme de votre aventure, vous repartez avez 10 pièces en plus pour votre aventure")
  portefeuille += 10

def batailleDalabok():
  print("Très bien.")
  sleep(1)
  clear()
  print("L'ennemi se trouvenant devant vous se situe au niveau 1, de quoi pouvoir le battre à mains nu, ses PV sont de 150 et la seule arme que vous possédez sont vos poings.")
  pvDalabok = 150 # PV de l'ennemi
  while pvDalabok > 0 and pdv_joueur > 0: # Tant que les pv de l'ennemi ne sont pas à 0 et ceux du joueur au dessus de 0
    choixAttaquerDalabok = int(input("Attaquer ?\n1.Oui      2.Fuir: "))
    if choixAttaquerDalabok == 1: # SI le joueur attaque
      attaqueContreDalabok = randint(30, 50) # Dégats random entre 30 et 50
      pvDalabok = pvDalabok - attaqueContreDalabok # Affligement des dégats à l'ennemi
      if pvDalabok > 0: # Si les PV de l'ennemi sont encore au dessus de 0
        print("Vous avez infligé", attaqueContreDalabok, "PV à votre ennemi, il en possède désormais", pvDalabok , "et ce dernier décide faire de même.")
        attaqueEnnemi1Réussie = randint(1, 2) # Savoir si l'ennemi reéussira à contre-attaquer
        if attaqueEnnemi1Réussie == 1: # Si contre attaque réussie
          degatsInfligéJoueur = randint(25, 30) # Dégats random entre 25 et 30
          pdv_joueur = pdv_joueur - degatsInfligéJoueur # Affligement des dégats au joueur
          if pdv_joueur > 0: # Si les PV du jouer sont toujours au dessus de 0
            print("Il ne vous a pas manqué, vous êtes désormais à", pdv_joueur, "PV")
            input("")
            clear()
          elif pdv_joueur < 0: # Dans le cas inverse
            print("Il ne vous a pas manqué, vous êtes désormais à", pdv_joueur, "PV, vous êtes donc mort et votre aventure s'arrête ici.")
            break # Le jeu s'arrête
        elif attaqueEnnemi1Réussie == 2: # Dans le cas où l'ennemi rate son attaque.
          print("Mais cela fût un échec, il vous a raté.")
          input("")
          clear()
      elif pvDalabok <= 0: # Si les PV de l'ennemi sont à 0
        print("Vous avez infligé", attaqueContreDalabok, "PV à votre ennemi, il en possède désormais", pvDalabok , "vous l'avez donc vaincu.")
        victoireBatailleDalabok = 1
        sleep(5)
    elif choixAttaquerDalabok == 2: # Si le joueur décide de fuir le combat
      print("Vous avez décidé de fuir le combat, vous repartez sans la princesse et l'aventure s'arrête pour vous.")
      sleep(2)
      print("Vous finirez donc chomeur au PMU du coin en portant la haine du peuple sur vos épaules.")
      input("")

# INTRODUCTION A L'HISTOIRE

clear()
print("Dans une contrée fort fort lointaine, se trouve la contrée magique et totalement dépourvu de Mal ou de haine...")
input("")
print("Marseille, le paradis ou le bien régnait en tout temps...")
input("")
print("C'est d'ailleurs ici que notre jeune héros Famacito, vivait en harmonie avec ses fratés...")
input("")
clear()

print("En rentrant chez lui Famacito avait une fois de plus reçu une lettre anonyme amoureuse, il en est venu a la conclusion que c'était de la part de Dennwesh.")
input("")
print("Il arriva donc devant chez elle, mais malgrè le fait qu'il était midi passé, elle ne fut toujours pas éveillé, Famacito savait que si elle n'avait pas fait ses ''flammes'' sur la très prisée application Snapchat c'est qu'elle fut été capturé par Dalabok !! \n    ")
input("")
clear()

# DEMANDE DU NOM DU JOUEUR

nom_joueur = input("Avant de commencer votre aventure, veuiller décliner votre identité cher joueur : ")
sleep(1)

# CHOIX DU CÔTE DE L'AVENTURE

print("Ravis de te connaître cher(e)", nom_joueur, ", Dennwesh a été enlevé, vous avez le choix entre être le héros ou bien le méchant de l'aventure.")
choix_sauver_dennwesh = input("Quel côté du jeu souhaitez vous exprérimenter ? \n1. Héros          2. Méchant: ")

if choix_sauver_dennwesh == "1": # Partie Héros du jeu
  print("A l'aventure !")
  sleep(2)
  clear()

  print("Vous êtes désormais l'aventurier du royaume !")
  print("Votre rôle en tant que héros et de briser les barières qui pourront vous être mis en face. \nCes fameuses barrières pourront être des énigmes, des batailles contre des chevaliers enemis ou encore le besoin de s'améliorer à travers différentes potions que vous pourrez acheter au fil de votre aventure.")
  input("")
  clear()
  print("En tant que 1ère quête, vous devez vous trouver de quoi vous protéger, en effet vous êtes actuellement dépourvu de toute protection contre vos ennemis.")
  input("")
  print("Et pour cela, le royaume vous a fait crédit de la somme de", portefeuille, "écumes afin de vous procurer le neécessaire chez un marchant/sorcier.")
  input("")
  clear()
  print("Pour prendre vos repères, vous décidez d'abord d'enquêter sur la disparition de la princesse. \nPour cela vous commencer par interoger quelques habitants afin de savoir si ces derniers n'auraient rien observé d'étrange.")
  input("")
  clear()
  print("Vous tombez d'abord sur le doyen du village, il vous propose une de ces potions vous permettant d'augmenter votre capacité de PV, étant actuellement de", pdv_joueur)
  
  choix_accepter_proposition_doyen = input("Acceptez vous de la prendre ? \n1. Oui           2. Non: ")

  if choix_accepter_proposition_doyen == "1":
    pdv_joueur = pdv_joueur + 50
    print("Félicitations, vous avez gagné une extention de votre vie de 50 PV, vous en êtes désormais à", pdv_joueur)
  elif choix_accepter_proposition_doyen == "2":
    print("Dommage.")

  print("Après avoir disctuté avec ce dernier, il vous confie avoir apperçu la princesse faire un tour dehors, le tout en vous détaillant qu'elle paraissait perdue, comme si elle avait perdu ses repères dans les rues de la ville, il fût à peine avoir eu le temps de se retourner que la princesse avait disparue.")
  input("")
  print("Laissant plusieures traces menant à la sortie de la ville...")
  input("")
  clear()
  print("Vous avancez avec prudence dans le but de chercher le moindre indice, ")
  input("")
  clear()

  # BATAILLE N°1
  print("Au cours de votre marche, vous croisez un viellard paraissant en grande faiblesse.\nAprès avoir tenté de l'aider, ce dernier se transforme soudainement en chevalier ennemi, le 1er que vous croisez sur votre chemin.")
  input("")
  print("Vous avez deux solutions s'offrant à vous...")


  fuireennemi1 = input("Que décidez vous de faire: \n1.Se battre            2. Fuir le combat: ")

  if fuireennemi1 == "1": # Si le joueur accepte la bataille 
    victoireBatailleN1 = 0 # Variable qui va être modifé pour activer la condition
    bataille()
    if victoireBatailleN1 == 1: # Si le joueur a gagné la bataille
      forgeronN1() # Il peut avoir la possibilité de se rendre chez le forgeron n°1
  elif fuireennemi1 == "2": # Si le joueur fuit la première bataille.
    fuireBatailleN1()
  else:
    print("Vous n'avez pas provenu de bonne réponse, votre aventure d'arrête ici.")
    exit()

  # ENIGME N°1

  clear()
  print("Après avoir croisez votre 1er ennemi, vous décidez de vous rafaichir la mémoire en consultant de nouveau votre carte")
  input("")
  print("Cette dernière vous indique de vous rendre au pont de la Seine mais vous pouvez également prendre un autre chemin qui fera éviter le monstre du pont.")
  input("")

  allerAuPont = input("Emprunter le pont ou l'autre chemin ? \n1. Le Pont\n2. L'autre chemin : ")

  victoireEnigmeN1 = 0

  if allerAuPont == "1": # Si le joueur accepte l'énigme
    print(f'\033[3mBien le bonjour à vous jeune chevalier, je suis le monstre du pont et pour passer ce dernier vous allez devoir résoudre une petite enigme.\033[0m')
    input("")

    for i in range(3):
      enigme1 = input(f'\033[3mJe ne peux pas marcher, j’ai pourtant un dos et quatre pieds. Qui suis-je ? (majuscule sans article) \033[0m')
      if enigme1 == "Chaise":
        print("Bravo à vous, vous pouvez désormais passer.")
        victoireEnigmeN1 = 1
        break # Arrêt de la boucle
      else:
        print("Eh non, votre aventure d'arrête ici.")
    if victoireEnigmeN1 == 1: # Si le joueur a remporté l'énigme
      enigme1gagné() 
  elif allerAuPont == "2": # Si le joueur fuit la première énigme.
    print("Vous avez décidé d'emprunter l'autre voie.")
  else:
    print("Vous n'avez pas provenu de bonne réponse, votre aventure d'arrête ici.")
    exit()

  # Avancé, de l'histoire

  print("En avancant sur votre chemin vous empruntez une grotte qui vous permettant de rejoindre le chatêau de Dalabok plus rapidement.")
  print("Grâce à votre lampe magique, vous parvenez à appercevoir une sorte de boite pouvant s'apparenter à un trésor.")
  input("")
  clear()

  prendreTrésor = input("Prendre le trésor ?\n 1. Oui \n 2. Non")

  if prendreTrésor == "1":
    print("Vous avez décidé de prendre le trésor")
    print("." * 3, end="")
    pvépée += 40
    sleep(1)
    print("Vous avez reçu 40 PV supplémentaire pour votre épée, ce qui fait grimper celle-ci à ", pvépée)
  elif prendreTrésor == "2":
    print("Vous decidez de tracez votre chemin.")
  else:
    print("Vous n'avez pas provenu de bonne réponse, votre aventure d'arrête ici.")
    exit()
  
  input("")
  print("Après avoir marché des kilomètes à la recherche de votre bien aimé, vous finissez par arriver au chateau, vous êtes enfin arrivé en face du chatêau où se sittue le ")
  print("")

  fuireDalabok = input("Que décidez vous de faire: \n1.Se battre contre Dalabok ?        2. Fuir le combat ? : ")

  if fuireDalabok == "1": # Si le joueur accepte la bataille 
    victoireBatailleDalabok = 0 # Variable qui va être modifé pour activer la condition
    batailleDalabok()
    if victoireBatailleDalabok == 1: # Si le joueur a gagné la bataille
      print("Vous avez battu Dalabok ! Vous pourrez donc repartir avec la princesse saine et sauve.")
      sleep(1)
      print("Vous serez aclamé par le peuple et nommé futur prétendant de la princesse.")
  elif fuireDalabok == "2": # Si le joueur fuit la première bataille.
    print("Vous avez décidé de fuir le combat, vous repartez sans la princesse et l'aventure s'arrête pour vous.")
    sleep(2)
    print("Vous finirez donc chomeur au PMU du coin en portant la haine du peuple sur vos épaules.")
    input("")
  
  print("Fin.")
  sleep(3)

elif choix_sauver_dennwesh == "2": # Partie méchante du jeu
  cotéMéchant.mechant()

  print("Fin.")