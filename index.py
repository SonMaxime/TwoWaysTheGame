from random import randint
from time import sleep # Pour effectuer un temps de pause entre les différents print() et clear()
import os

import defCoteMechant
import defCoteGentil

def clear(): # Cette fonction permettera au code d'éviter de surcharger la console, donc de la nettoyer complètement afin rendre celle-ci plus légère et agréable pendant l'aventure.
  if os.name == "posix": # Si le code fontionne sur une plateforme Linux
    os.system('clear') # Fonction clear sur Linux
  elif os.name in ("nt", "dos", "ce"): # Si le code fontionne sur une plateforme Windows
    os.system('CLS') # Fonction clear sur Windows
  # Ces deux conditions permettent à la fonction de s'éxécuter sans problème sur les deux platformes

portefeuille = 50 # Portefeuille du joueur, initiallement définis sur 50 écumes (la monnaie qui sera utilisée dans le jeu).
pdv_joueur = 100 # PV du joueur, on débute à 100.
lvl = 1 # Niveau du joueur, on débute à 1.
épée = 1 # Niveau de l'épée du héros.
pvépée = 57 # Points de vie de l'épée du héros.

ancien_pdv=100
pdv_capitaine=300

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
  sleep(5)
  print("Laissant plusieures traces menant à la sortie de la ville...")
  input("")
  clear()
  print("Vous avancez avec prudence dans le but de chercher le moindre indice, ")
  input("")
  clear()

  # BATAILLE N°1
  print("Au court de votre marche, vous croisez un viellard paraissant en grande faiblesse.\nAprès avoir tenté de l'aider, ce dernier se transforme soudainement en chevalier ennemi, le 1er que vous croisez sur votre chemin.")
  input("")
  print("Vous avez deux solutions s'offrant à vous...")


  fuireennemi1 = input("Que décidez vous de faire: \n1.Se battre            2. Fuir le combat: ")

  if fuireennemi1 == "1": # Si le joueur accepte la bataille 
    victoireBatailleN1 = 0 # Variable qui va être modifé pour activer la condition
    defCoteGentil.batailleN1()
    if victoireBatailleN1 == 1: # Si le joueur a gagné la bataille
      defCoteGentil.forgeronN1() # Il peut avoir la possibilité de se rendre chez le forgeron n°1
  elif fuireennemi1 == "2": # Si le joueur fuit la première bataille.
    defCoteGentil.fuireBatailleN1()

  print("Après avoir croisez votre 1er ennemi, vous décidez de vous rafaichir la mémoire en consultant de nouveau votre carte")
  input("")
  print("Vous suivez donc le chemin méticuleusement...")

  input("")

  print("Votre carte vous indique que vous devez ")
  
  

  print("FINI")
  sleep(3)

elif choix_sauver_dennwesh == "2": # Partie méchante du jeu
  defCoteMechant.combat_pirates()