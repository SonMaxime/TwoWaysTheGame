from random import randint
from time import sleep
pdv_joueur=100
ancien_pdv=100
pdv_capitaine=300
point=0 #On initialise les variables
vies=4
epee_requin=2 
pdv_joueur_garde=100#Points de Vie Joueur
vie_garde=150 #Pdv Garde
durabilite_arme_garde=3

def mechant():
    global pdv_joueur,pdv_capitaine,ancien_pdv
    
    #Introduction Mechant
    print("Vous incarnez donc Dalabok un jeune monstre qui n'a qu'une seule envie, conuqérir DennWesh la fille dont il est amoureux")
    print("Après avoir tout tenté, messages d'amour, poèmes, chansons...Vous décidez d'utiliser la violence !")
    print("Vous partez pour enlever DennWesh qui habite à Marseille")
    print("Vous choississez de vous cacher dans un bateau a destination de Marseille pour vous introduire dans la cité Marseillaise...")
    input("")
    print("Vous vous rendez compte que ce bateau est un navire pirate, le capitaine nommé Awarigum vous trouve et vous menace")
    print("Le capitaine étant joueur il vous propose une énigme si vous arrivez a répondre il vous ramène a bon port sinon...")
    input("") #Sert a faire une pause
    reponse_enigme=input("QUESTION : Qu'est ce qui est trop chaud et trop frais en même temps ? :")
    if reponse_enigme=="Le capitaine":#Enigme avec condition
        print("Vous avez triché ou vous êtes trop intelligent, vous méritez la mort")
    else:
        print("Eh malheureusement non, la réponse était Le capitaine, vous êtes nul vous méritez la mort")
        print("Le capitaine brandit son épee magique a énigmes et vous prend en duel !")
        input("")
        print("La seule manière d'esquiver les coups ,et de répondre correctement aux questions données par l'épée elle même.(sans article et sans majuscule)")
        input("")
    
    
        while pdv_joueur>0 and pdv_capitaine>0:#Boucle pour mettre fin au jeu
            print("La capitaine vous frappe,vous entendez une voix au plus profond de vous")
            input("")
            print("...")
            input("")
            print("Qu'est c-")
            print("Qu'est ce qui est-")
            def enigme_capitaine(enigme,reponse,reponse2,reponse3,reponse4): #Création d'une fonction pour les énigmes
                global pdv_joueur,pdv_capitaine,ancien_pdv#On Met les variables en global pour les utiliser dans une fonction
                if pdv_capitaine>0 and pdv_joueur>0:     
                        enigme=input(enigme)
                        if reponse==enigme or reponse2==enigme or reponse3==enigme or reponse4==enigme:
                            print("Bien joué ! Vous ne perdez aucun point de vie !")
                        if reponse!=enigme and reponse2!=enigme and reponse3!=enigme and reponse4!=enigme:
                            degats_du_capitaine=randint(15,27)
                            pdv_joueur=pdv_joueur-degats_du_capitaine
                            ancien_pdv=pdv_joueur+degats_du_capitaine
                            print("C'est faux !La reponse était",reponse,".Vous perdez",degats_du_capitaine,"points de vie.Vous passez de",ancien_pdv,"à",pdv_joueur)
                            
                            
            print(enigme_capitaine("QUESTION :Qu'est ce qui est jaune et qui attend ?(sans majuscule)","johnatan","jonhatan","jonathan","jonatan"))
            input("")
            print("C'est a vous d'attaquer ! :")
            
            
            def combat_capitaine():#Fonction Pour Attaquer
                global pdv_joueur,pdv_capitaine,ancien_pdv
                if pdv_capitaine>0 and pdv_joueur>0:  
                    coup=input("QUESTION :1:Uppercut  2:Coup de pied : ")
                    if coup=="1":
                        print("Vous tentez un uppercut ! Votre coup est tres puissant mais il a une chance sur 2 de rater !")
                        uppercut=randint(1,2)
                        if uppercut==1:
                            perte_vie_capitaine=randint(50,80)
                            pdv_capitaine+=-perte_vie_capitaine
                            print("Vous avez de la chance cela fonctionne, le capitaine perd",perte_vie_capitaine,"point de vie, il est a",pdv_capitaine)
                            input("")
                        elif uppercut==2:
                                print("Malheureusement vous n'avez pas de chance, le capitaine ne perd aucun point de vie, il en a",pdv_capitaine)
                                input("")
                    if coup=="2":
                        print("Vous tapez de toutes vos forces sur la jambe en bois du capitaine, il tombe au sol !")
                        perte_vie_capitaine=randint(50,80)
                        pdv_capitaine+=-perte_vie_capitaine
                        print("Vous lui avez fait perdre",perte_vie_capitaine,"point de vie, il est a",pdv_capitaine)
                        input("")
                    return("")    
            combat_capitaine()  #On utilise les fonctions  
            enigme_capitaine("QUESTION :On peut me trouver au fond d'un bateau de pêche ou au milieu d'un court de tennis. ?","filet","Filet","Un filet","un filet")        
            combat_capitaine()
            enigme_capitaine("QUESTION :Je ne fais pas de bruit quand je me réveille mais je réveille tout le monde.Qui suis-je ?","soleil","Soleil","Le soleil","le soleil")
            combat_capitaine()
            enigme_capitaine("QUESTION :Je ne peux pas marcher, j’ai pourtant un dos et quatre pieds. Qui suis-je ?","chaise","Chaise","une chaise","Une chaise")
            combat_capitaine()
            enigme_capitaine("QUESTION :Un fermier a 17 vaches ; elles meurent toutes sauf 9. Combien en reste-t-il ?","9","neuf","9","9")
            combat_capitaine()
            enigme_capitaine("QUESTION :Didier paye 200 cafés a 40 centimes, combien d'euros a t'il du dépenser pour les copains ?","80","quatre-vingt","quatrevingt","80")
            combat_capitaine()
            enigme_capitaine("QUESTION :Qu'est ce qui est né grand et meurt petit ?","bougie","Bougie","Une bougie","une bougie")
    if pdv_joueur<0:
        print("Vous avez perdu... Retentez votre chance !")
    if pdv_joueur>0:
        def partie_requin():
                global point,vies
                print("Ce qui semble etre un homme deguisé en requin saute sur le bateau ! De peur vous prenez votre arme mais il la casse !")
                print("Il vous propose un jeu pour gagner une arme en dent de requin,l'arme la plus solide existante...")
                input("")
                print("Etant fan de dessin il vous dessinera une forme et vous avez pour mission de deviner ce qui est représenté. ")
                print("Vous gagnez la partie quand vous obtenez au moins 8 points mais attention vous n'avez que 4 vies !")
                input("")
                print("<(o )___")
                print(" ( ._> /")
                print("  `---'")
                print("Il prend son pinceau pour vous faire un exemple,ici la réponse est canard !")
                input("")
                print("Maintenant c'est a vous de jouer !")
                input("")
                def enigme_requin(reponse_requin,reponse_requin2,reponse_requin3,reponse_requin4): #Fonction pour vérification de la réponse
                    global point,vies #On les met en global pour les utilser dans la fonction
                    if vies>0:
                        reponse_joueur=input("QUESTION : Qu'est ce qui est représenté ? ")
                        if reponse_joueur==reponse_requin or reponse_joueur==reponse_requin2 or reponse_joueur==reponse_requin3 or reponse_joueur==reponse_requin4:#Action selon la réponse du joueur
                            point += 1
                            print("Bien joué ! Vous gagnez un point,votre nombre de points est de",point)
                            input("")
                        if reponse_joueur!=reponse_requin and reponse_joueur!=reponse_requin2 and reponse_joueur!=reponse_requin3 and reponse_joueur!=reponse_requin4:
                            print("Faux ! La réponse était",reponse_requin)
                            vies=vies-1
                            print("Vous avez", point,"points et votre nombre de vies est de",vies)
                            input("")
                
                    
                    
                if vies>0:
                    print("  ;****;")#On utlise la fonction print pour faire des dessins, on impriovise avec les moyens qu'on a pour respecter le cahier de charges
                    print("o( @..@ )o")
                    print(" '(---)'")
                    enigme_requin("singe","Singe","singe","Singe") #On met plusieurs réponses pour éviter les fautes d'orthographes
                    print(" __")
                    print("/o \_____")
                    print("\__/-='='`")
                    enigme_requin("clé","clef","Clé","Clef", "une clé", "une clef")
                if vies>0:            
                    print("@};---")
                    enigme_requin("rose","Rose","rose"," une rose")
                if vies>0:            
                    print("  ,---.   ,---.   ,---.")
                    print(",'     `.'     `.'     `.")
                    print("|     ,-|-.   ,-|-.     |")
                    print("`.  ,' ,'. `.' ,'. `.  ,'")
                    print("  `-|-'   `-|-'   `-|-'")
                    print("    `.     ,',     ,'")
                    print("      `---'   `---'")
                    enigme_requin("Jeux Olympiques","jeux olympiques","J.0","JO")
                if vies>0:            
                    print("            ,-~¨^  ^¨-,           _,")
                    print("           /          / ;^-._...,¨/")
                    print("          /          / /         /")
                    print("         /          / /         /")
                    print("        /          / /         /")
                    print("       /,.-:''-,_ / /         /")
                    print("       _,.-:--._ ^ ^:-._ __../")
                    print("     /^         / /¨:.._¨__.;")
                    print("    /          / /      ^  /")
                    print("   /          / /         /")
                    print("  /          / /         /")
                    print(" /_,.--:^-._/ /         /")
                    print("             ^¨¨-.___.:^")
                    enigme_requin("windows","Windows","windows","windows")
                if vies>0:        
                    print("      ___------__")
                    print("|\__-- /\       _-")
                    print("|/    __      -")
                    print("//\  /  \    /__")
                    print(" |  o|  0|__     --")
                    print(" \\____-- __ \   ___-")
                    print("(@@    __/  / /_")
                    print("   -_____---   --_")
                    print("     //  \ \\   ___-")
                    print("   //|\__/  \\  \ ")
                    print("   \_-\_____/  \-\ ")
                    print("        // \\--\|")
                    print("   ____//  ||")
                    print("  /_____\ /___\ ")
                    enigme_requin("Sonic","sonic","sonic","sonic")
                if vies>0:
                    print("                                     ,-.")
                    print("                                     `\ `.")
                    print("                                       (`- `.")
                    print("                           __          `c.- \ ")
                    print("                           (_ `---..__   `\"_ \ ")
                    print("                             `(`-.__  `-._ (_c |")
                    print("                               `--.____ ( `,-  | |/")
                    print("                                  `---(___| ,---/         ,.")
                    print("                                    ,-;::,'|_/\-|       ,' /")
                    print("                            _.._    ||   `-'\@/@|_      | ||-.")
                    print("                    _.--.--'    `-. \`--/,-._/    `\_,--',/|,-\ ")
                    print("                  .',- _     _.__  `-:_|/   (      /      )|-'|")
                    print("                 /_/_,;-  ,-'    `-._ _)_,-,-,___,'---'\___.-'")
                    print("                 |___,,.  | _    _.-'' ((_{_// /")
                    print("                 \.-'  | (-' \.-'       `---'`'")
                    print("                    ,-'\__>  /|         /")
                    print("                  .',-'/|.   \ \        |")
                    print("                 / / _|``.`.  `/\_     /|  ,,.")
                    print("                /  \  |  |  `-.`(_),. /((((   )")
                    print("                |   `--\ `.`=. `-._`'|__|  `''")
                    print("                |  ,'  |`-|   T``'',----.")
                    print("                |      |  `.__|-,-',----.|")
                    print("                \     / ,-' _,-;,-'      |")
                    print("                 `---'  | ,;-''       _,'")
                    print("                        `//       _,-'")
                    print("                         \____.-'' ")
                    enigme_requin("asterix","Asterix","Astérix","astérix")
                if vies>0:
                    
                    print("         $$$$$               ###$$$               #####")
                    print("         $$$$$$              #$#$#$              ######")
                    print("         $$$$$$            $$$#$#$#$#            ######")
                    print("         $$$$$$$        $$$$$$$$########        #######")
                    print("          $$$$$$$     $$$$$$$$$  #########     #######")
                    print("          $$$$$$$    $$$$$$$$      ########    #######")
                    print("          $$$$$$$  $$$$$$$$$        #########  #######")
                    print("            $$$$$ $$$$$$          ###### #####")
                    print("             $$$$$$$$                   ########")
                    print("              $$$$$$$$$$$$$          #############")
                    print("            $$$$$$$$$$$$$$$$$      #################")
                    print("            $$$$$$$$$$$$   $$$    ###   ############")
                    print("           $$$$$$$$$$$$$  $$$$$  ####  #############")
                    print("           $$$$$$$$$$$$$$$$$$$$$#####################")
                    print("            $$$$$$$$$$$$$$$$$$$  ###################")
                    print("             $$$$$$$$$$$$$$$$$    #################")
                    print("                $$$$$$$$$$            ##########")
                    print("              $$$$$$$$$$$$$          #############")

                    enigme_requin("playboy","PlayBoy","Playboy","playBoy")
                if vies>0:
                    print("                                _,.------....___,.' ',.-.")
                    print("                             ,-'          _,.--'        |")
                    print("                           ,'         _.-'              .")
                    print("                          /   ,     ,'                   `")
                    print("                         .   /     /                     ``.")
                    print("                         |  |     .                       \.\ ")
                    print("                       __|___._.  |       __               \ `.")
                    print("             .'    `---''       ``'-.--''`  \               .  \ ")
                    print("            .  ,            __               `              |   .")
                    print("            `,'         ,-''  .               \             |    L")
                    print("           ,'          '    _.'                -._          /    |")
                    print("          ,`-.    ,'.   `--'                      >.      ,'     |")
                    print("         . .'\'   `-'       __    ,  ,-.         /  `.__.-      ,'")
                    print("         ||:, .           ,'  ;  /  / \ `        `.    .      .'/")
                    print("         j|:D  \          `--'  ' ,'_  . .         `.__, \   , /")
                    print("        / L:_  |                 .  '' :_;                `.'.'")
                    print("        .    '''                  ''''''                    V")
                    print("         `.                                 .    `.   _,..  `")
                    print("           `,_   .    .                _,-'/    .. `,'   __  `")
                    print("            ) \`._        ___....----''  ,'   .'  \ |   '  \  .")
                    print("           /   `. '`-.--''         _,' ,'     `---' |    `./  |")
                    print("          .   _  `'''--.._____..--'   ,             '         |")
                    print("          | .' `. `-.                /-.           /          |")
                    print("          | `._.'    `,_            ;  /         ,'          .")
                    print("         .'          /| `-.        . ,'         ,           ,")
                    print("         '-.__ __ _,','    '`-..___;-...__   ,.'\ ____.___.'")
                    print("         `'^--'..'   '-`-^-''--    `-^-'`.'''''''`.,^.`.--'")
                    enigme_requin("Bulbizarre","bulbizarre","bulbizarre","bulbizarre")
                if vies>0:
                    print("  |\/\/\/\/\/|")
                    print("  |          | ")
                    print("  |          | ")
                    print("  |          | ")
                    print("  |    __  __| ")
                    print("  |   /  \/  \ ")
                    print("  |  (o   )o  )")
                    print(" /C   \__/ --.")
                    print(" \_   ,     -'")
                    print("  |  '\_______)")
                    print("  |      _)")
                    print("  |     |")
                    print(" /`-----'\ ")
                    print("/         \ ")
                    enigme_requin("Bart","bart","Bart Simpson","bart simpson")
                if vies>0:
                    print("                           ,,,, ")
                    print("                     ,;) .';;;;',")
                    print("         ;;,,_,-.-.,;;'_,|I\;;;/),,_")
                    print("          `';;/:|:);{ ;;;|| \;/ /;;;\__")
                    print("              L;/-';/ \;;\',/;\/;;;.') \ ")
                    print("              .:`''` - \;;'.__/;;;/  . _'-._ ")
                    print("            .'/   \     \;;;;;;/.'_7:.  '). \_")
                    print("          .''/     | '._ );}{;//.'    '-:  '.,L")
                    print("        .'. /       \  ( |;;;/_/         \._./;\   _,")
                    print("         . /        |\ ( /;;/_/             ';;;\,;;_,")
                    enigme_requin("spiderman","Spiderman","Spider-Man","spider-man")
                if vies>0:
                    print("            /|         , ")
                    print("          ,///        /| ")
                    print("         // //     ,/// ")
                    print("        // //     // // ")
                    print("       // //     || || ")
                    print("       || ||    // // ")
                    print("       || ||   // // ")
                    print("       || ||  // // ")
                    print("       || || || || ")
                    print("       \\,\|,|\_// ")
                    print("        \\)\)\\|/ ")
                    print("        )-."" .-( ")
                    print("       //^\` `/^\\ ")
                    print("      //  |   |  \\ ")
                    print("    ,/_| 0| _ | 0|_\,")
                    print("  /`    `'='=.v.='`   `\ ")
                    print(" /`    _.'{_,_}'='._   `\ ")
                    print(" `/`  ` \  |||  / `  `\`")
                    print("  `',_  \\=^~^=//  _,'`")
                    print("      '=,\'-=-'/,='")
                    print("          '---''=')")
                    enigme_requin("Bugs Bunny","bugs bunny","Bugs","bugs")
                if vies>0:
                    print("__________________|")
                    print("     ,--.    ,--.  ")
                    print("    |oo  | _  \  `.")
                    print("o  o|~~  |(_) /   ;")
                    print("    |/\/\|   '._,' ")
                    print("__________________ ")
                    print("                  |")
                    enigme_requin("PacMan","pacman","Pac-Man","pac-man")
                if vies<=0:
                    print("Malheureusement, vous avez perdu, vous n'avez pas eu 8 points...Le faux requin retourne au fond de l'océan en vous privant de votre arme")
                    epee_requin=1 #On donne une valeur a l'arme pour savoir si le joueur l'a ou pas pour changer l'histoire selon son obtention
                if vies>0 and point>=0:
                    print("Bien joué ! Vous avez gagné et le faux requin vous remet l'épee la plus solide existante !")
                    epee_requin=2


        partie_requin()

        print("Vous arrivez enfin devant chez DennWesh mais son garde personnel vous empêche de l'atteindre")
        print("Vous dégainez votre épée et vous le prenez en duel !")
        input("")
    
        def combat_garde():
            global epee_requin,pdv_joueur_garde,vie_garde,durabilite_arme_garde
            print("Le garde attaque !")
            input("")
            if durabilite_arme_garde==3:
                degats_joueur=randint(20,30)
                print("La durabilté de l'arme du garde est de niveau 3 !Les degats infligés par le garde se situent entre 20 et 30.")
            if durabilite_arme_garde==2:
                degats_joueur=randint(15,25)
                print("La durabilté de l'arme du garde est de niveau 2 !Les degats infligés par le garde se situent entre 15 et 25.")
            if durabilite_arme_garde==1:
                degats_joueur=randint(10,20)
                print("La durabilté de l'arme du garde est de niveau 1!Les degats infligés par le garde se situent entre 10 et 20.")
            input("")
            choix_joueur_garde=input("Voulez vous : 1.Attaquer 2.Esquiver 3.Parer(reduit la durabilté de l'arme du garde) :")
            
            
            #Attaque
            if choix_joueur_garde=="1"or choix_joueur_garde=="Attaquer":
                if epee_requin==1:
                    degats_garde=randint(10,20)
                if epee_requin==2:
                    degats_garde=randint(20,30)
                vie_garde=vie_garde-degats_garde
                print("Vous brandissez votre arme et vous frappez de toutes vos forces")
                print("Vous infligez",degats_garde,"dégâts au garde,il a",vie_garde,"points de vie")
                input("")
                if vie_garde>0:
                    pdv_joueur_garde+=-degats_joueur
                    print("Le garde vous attaque aussi.Vous perdez",degats_joueur,"points de vie, il vous en reste",pdv_joueur_garde,)
            
            
            
            #Esquive
            if choix_joueur_garde=="2":
                esquive=randint(1,2)
                if esquive==1:
                    print("Bien joué ! Vous esquivez le coup vous contre-attaquez !")
                    coup_garde=input("QUESTION :1:Coup de tête  2:Balayette : ")
                    if coup_garde=="1":
                        print("Vous tentez un coup de tête ! Votre coup est tres puissant mais il a une chance sur 2 de rater !")
                        coup_tete=randint(1,2)
                        if coup_tete==1:
                            degats_garde=randint(25,35)
                            vie_garde=vie_garde-degats_garde
                            print("Vous avez de la chance cela fonctionne, le garde perd",degats_garde,"point de vie, il est a",vie_garde)
                            input("")
                        elif coup_tete==2:
                                print("Malheureusement vous n'avez pas de chance, le garde ne perd aucun point de vie, il en a",vie_garde)
                                input("")
                    if coup_garde=="2":
                        print("Votre coup est faible mais il marche à tout les coups !")
                        degats_garde=randint(15,25,)
                        vie_garde=vie_garde-degats_garde
                        print("le garde perd",degats_garde,"points de vie, il est a",vie_garde)
                if esquive==2:
                    print("Votre esquive rate, cela vous met en mauvaise posture !")
                    coup_garde=randint(1,2)
                    if coup_garde==1:
                        print("Par chance le garde rate son coup !")
                    else:
                        degats_garde=randint(10,15)
                        pdv_joueur_garde+=-degats_joueur
                        print("Le garde vous inflige",degats_garde,"dégats, vous avez",pdv_joueur_garde,"points de vie")
            
            
            #Parage
            if choix_joueur_garde=="3":
                if epee_requin==1:
                    print("Pas bien malin de parer un coup avec un bout de bois, si seulement vous aviez eu l'épée en dent de requin....Votre parage échoue vous perdez 20 points de vie")
                    pdv_joueur_garde+=-10
                    print("vous avez",pdv_joueur_garde,"points de vie")
                if epee_requin==2:
                    parage=randint(1,3)
                    if parage!=1:
                        if durabilite_arme_garde!=0:
                            print("Votre arme en dent de requin vous permet d'arrêter le coup facilement ! L'arme de l'adversaire s'est détérioré il fera moins de degâts")
                            durabilite_arme_garde+=-1
                        if durabilite_arme_garde==0:
                            print("Le garde est devenu plus méfiant, il ne se laissera plus avoir")
                    if parage==1:
                        print("Votre parage rate ! L'ennemi contre-attaque !")
                        coup_garde_parage=randint(1,2)
                        if coup_garde_parage==1:
                            print("Par chance le garde rate son coup !")
                        else:
                            degats_garde=randint(5,10)
                            pdv_joueur_garde+=-degats_garde
                            print("Le garde vous inflige",degats_garde,"dégats, vous avez",pdv_joueur_garde,"points de vie")
                        
                        
                        
                        
        while pdv_joueur_garde>0 and vie_garde>0:
            combat_garde()
        if pdv_joueur_garde<=0:
            print("Vous avez perdu mais vous étiez prêt du but...Retentez votre chance !")
        if vie_garde<=0 and pdv_joueur_garde>0:
            print("Vous passer le garde et vous arrivez enfin devant votre dulcinée.")
            sleep(1)
            print("Quand elle vous voit DennWesh vous traite comme un ami, elle ne semble pas remarquer votre apparence monstrueuse...")
            sleep(1)
            print("Pendant quelques instants vous éprouvez du remord a faire ce que vous faites mais à ce moment là vous entendez, le fiancé de DennWesh à la fenêtre !")
            sleep(1)
            print("De panique vous la prenez de force et vous vous enfuyez vers votre château...")
            sleep(1)
            
        combat_garde()