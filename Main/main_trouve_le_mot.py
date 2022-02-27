from random import*               
import sys
import os
import datetime
#trash=os.system('cls')
date = datetime.datetime.now()

fichier_inscription = open('base_inscrit.txt', 'a')

fichier_inscription.close()

fichier_pseudo = open('base_pseudo.txt', 'a')

fichier_pseudo.close()

fichier_MotDePass = open('base_MotDePass.txt', 'a')

fichier_MotDePass.close()

fichier_point = open('fichier_point.txt', 'w')
fichier_point.close()

fichier_point = open('fichier_point.txt', 'w')
fichier_point.close()







#Commencer le jeu
#-----------------------------------------------NIVEAU 1 DU JEU-------------------------------------------------------------------------------------


def niveau1():
    
    dico_mots_A = {"AGE":"Temps ecoulé depuis qu'une personne est en vie","AGRANDIR":"Rendre plus grand","AIMER":"Epprouver de l'affection"}
    dico_mots_B = {"BANDIT":"Malfaiteur vivant hors la lois","BARBE":"Poils du manton, des joues et de la levre superieur","BORDEL":"Maison de prostitution"}
    dico_mots_C = {"COLORER":"Revetir de couleur","COMBLER":"Remplir un vide","COMPETITION":"Epreuve sportive disputée entre plusieurs concurents"}
    dico_mots_D = {"DEUX":"Un plus un","DOIGT":"Chacun des cinq prolongements qui terminent la main de l'homme","DORMIR":"Être dans l'état de sommeil"}
    dico_mots_E = {"ENTRER":"Passer du dehors au dedans","ENLEVER":"Porter vers le haut.","ENDORMIR":"Faire dormir, amener au sommeil."}
    dico_mots_F = {"FIN":"Moment, instant auquel tout s'arrête","FAIM":"Sensation qui, normalement, accompagne le besoin de manger","FAUX":"Qui n'est pas vrai, qui est contraire à la vérité "}
    dico_mots_G = {"GRANDIR":"Devenir plus grand.","GAGNER":"S'assurer un profit matérie","GIFLER":"Frapper d'une gifle."}
    dico_mots_H = {"HOMME":"L'être humain, en général","HEURE":"Espace de temps égal à la vingt-quatrième partie du jour","HEUREUX":"Qui bénéficie d'une chance favorable, que le sort favorise"}
    dico_mots_I = {"INVINCIBLE":"Qui ne peut être vaincu","INTERDIRE":"Defendre qqch","INVISIBLE":"Qui n'est pas visible, qui échappe à la vue."}
    dico_mots_J = {"JALOUSIE":"émotion secondaire qui représente des pensées et sentiments d'insécurité, de peur et d'anxiété concernant la perte anticipée ou pas d'un statut, d'un objet ou d'un lien affectif ayant une importante valeur personnelle","JANVIER":"Premier mois de l'année.","JEU":"Activité physique ou mentale dont le but essentiel est le plaisir qu'elle procure."}
    dico_mots_K = {"KLAXON":"Avertissement sonore","K-O":"Battue par .....","KETCHUP":"Sauce à base de tomates legeremnt sucrée et épicée"}
    dico_mots_L = {"LOUER":"Prendre en location, à bail.","LOUPER":"Ne pouvoir prendre, laisser échapper.","LOUP":"Mammifère carnivore sauvage, qui ressemble à un grand chien"}
    dico_mots_M = {"MENTIR":"Affirmer ce qu'on sait être faux","MIER":"Mettre un enjeu","MERE":"Femme qui a mis au monde un ou plusierus enfants"}
    dico_mots_N = {"NEUTRE":"Qui ne participe pas à un conflit.","NAGER":"Se mouvoir sur ou dans l'eau par des mouvements appropriés.","NARCISSISME":"Admiration, contemplation de soi-même."}
    dico_mots_O = {"ORGUEIL":"Opinion très avantageuse qu'une personne a de sa propre valeur aux dépens de la considération due à autrui.","OU":"conjonction, Autrement dit. ","OCCUPER":"Prendre possession de"}
    dico_mots_P = {"PRINCE":"Celui qui possède une souverenité","POSSIBLE":"Qui peut etre realisé","PRETER":"Mettre qqch à la disposition de qqn pour un temps determiner"}
    dico_mots_Q = {"QUESTION":"Demande qu'on adresse à qlqn afin d'apprendre qqch","QUATRE":"Trois plus un","QUESTIONNER":"Poser des questions"}
    dico_mots_R = {"RATER":"Manquer son coup","REMERCIER":"Dire merci","REMARQUER":"Avoir la vue, l'atention frappée par qlch"}
    dico_mots_S = {"SOIR":"Fin du jour, moments qui précèdent et qui suivent le coucher du soleil.","SOLDAT":"Homme qui sert dans une armée.","SIESTE":"Repos pris après le repas de midi."}
    dico_mots_T = {"TERRAIN":"Étendue de terre","TERRE":"L'élément solide qui supporte les êtres vivants et où poussent les végétaux.","TERREUR":"Peur extrême qui bouleverse, paralyse."}
    dico_mots_U = {"UNIR":"Mettre ensemble ","URINER":"Évacuer l'urine.","USER":"Avoir recours à"}
    dico_mots_V = {"VIVRE":"Être en vie","VIN":"Boisson alcoolisée provenant de la fermentation du raisin.","VIDER":"Rendre vide"}
    dico_mots_W = {"WAGON":"Véhicule sur rails, tiré par une locomotive.","WEB":"Ensemble des données reliées par des liens hypertextes, sur Internet.","WEEK-END":"Congé de fin de semaine, comprenant le samedi et le dimanche"}
    dico_mots_X = {"XENOPHOBE":"Hostile par principe aux étrangers, à ce qui vient de l'étranger.","XENOPHOBIE":"Hostilité de principe envers les étrangers, ce qui vient de l'étranger.","XYLOPHAGE":"Qui ronge le bois."}
    dico_mots_Y = {"YAOURT":"Lait caillé et fermenté.","YOGA":"Doctrine et exercices traditionnels hindous, cherchant à réunir l'individu avec le principe de toute existence.","YOUPI":"Cri d'enthousiasme, souvent accompagné d'un geste exubérant."}
    dico_mots_Z = {"ZERO":"Nombre qui represente un ensemble vide","ZOMBI":"Esprit d'un mort qu'un sorcier met à son service","ZOO":"Parc zoologique"}

    liste_dico_mots = [dico_mots_A,dico_mots_B,dico_mots_C,dico_mots_D,dico_mots_E,dico_mots_F,dico_mots_G,dico_mots_H,dico_mots_I,dico_mots_J,dico_mots_K,dico_mots_L,dico_mots_M,dico_mots_N,dico_mots_O,dico_mots_P,dico_mots_Q,dico_mots_R,dico_mots_S,dico_mots_T,dico_mots_U,dico_mots_V,dico_mots_W,dico_mots_X,dico_mots_Y,dico_mots_Z]
    


    fichier_pseudo_copy = open('base_pseudo_copy.txt', 'r') # ouverture du fichier point

    ligne = fichier_pseudo_copy.readlines()
    for line in ligne:
        
        pseudo = line
	


    
    fichier_pseudo_copy.close()
    point = 0
    
    for i in range(3):
        num_lettre = randint(0, 25)
        choix_dico = liste_dico_mots[num_lettre]
        choix_mot_dico = choix_dico.keys()

        liste_mot = []                    
        liste_definition = []
    
        for mot in choix_dico.keys():
            liste_mot.append(mot)         #mettre les mots du dictionnaire dans une liste nouvelement crée

        for definition in choix_dico.values():
            liste_definition.append(definition)     #mettre les definition du dictionnaire dans une liste nouvelement crée
        
        mot1 = liste_mot[i]
        def1 = liste_definition[i]
    
        #AFFICHAGE DE LA PREMIERE QUESTION
        trash=os.system('cls')


    
        print("                        NIVEAU 1 DU JEU\n\n\n")

        
        print("Votre pseudo :",pseudo,"\n\n")
        print("Nombre de point:",point,"\n\n")
        

        
        nb_lettre = len(mot1)
        print("Question :",i+1)
        print("    Indice: ",def1)
        print("    Le mot commence par la lettre "+mot1[0]," et comporte ",(nb_lettre)," lettres")
        reponse = input("Votre reponse: ")
        REPONSE = reponse.upper()

        #VERIFICATION DE LA PREMIERE REPONSE
        if REPONSE != mot1:


        
            print("Woops, la reponse est fausse.")
        
            definition1 = def1[0:25]+"..."         #Prendre les 25 premieres lettres de la definition et remplacer le reste par ...
        
            fichier_reponse = open('fichier_reponse.txt', 'a')              # Mettre la reponse dans le fichier reponse

            line_rep = 'Indice:{}, Votre reponse :{} ,Vraie Reponse :{}\n'.format(definition1,REPONSE,mot1)
            fichier_reponse.write(line_rep)


            fichier_reponse.close()
        
        
    
        if REPONSE == mot1:
            point += 5
            print("Bravo, bonne reponse")
        
            definition1 = def1[0:25]+"..."         #Prendre les 25 premieres lettres de la definition et remplacer le reste par ...
        
            fichier_reponse = open('fichier_reponse.txt', 'a')              # Mettre la reponse dans le fichier reponse

            line_rep = 'Indice:{}, Votre reponse :{} \n'.format(definition1,REPONSE)
            fichier_reponse.write(line_rep)

            fichier_reponse.close()


    str_point = str(point)
    
    fichier_point = open('fichier_point.txt', 'w') 
    fichier_point.write(str_point)

    fichier_reponse.close()







       


        
           

        
            

#------------------------------------------------NIVEAU 2---------------------------------------------------------------------------------------------

def niveau2():
    
    dico_mots_A = {"AGE":"Temps ecoulé depuis qu'une personne est en vie","AGRANDIR":"Rendre plus grand","AIMER":"Epprouver de l'affection"}
    dico_mots_B = {"BANDIT":"Malfaiteur vivant hors la lois","BARBE":"Poils du manton, des joues et de la levre superieur","BORDEL":"Maison de prostitution"}
    dico_mots_C = {"COLORER":"Revetir de couleur","COMBLER":"Remplir un vide","COMPETITION":"Epreuve sportive disputée entre plusieurs concurents"}
    dico_mots_D = {"DEUX":"Un plus un","DOIGT":"Chacun des cinq prolongements qui terminent la main de l'homme","DORMIR":"Être dans l'état de sommeil"}
    dico_mots_E = {"ENTRER":"Passer du dehors au dedans","ENLEVER":"Porter vers le haut.","ENDORMIR":"Faire dormir, amener au sommeil."}
    dico_mots_F = {"FIN":"Moment, instant auquel tout s'arrête","FAIM":"Sensation qui, normalement, accompagne le besoin de manger","FAUX":"Qui n'est pas vrai, qui est contraire à la vérité "}
    dico_mots_G = {"GRANDIR":"Devenir plus grand.","GAGNER":"S'assurer un profit matérie","GIFLER":"Frapper d'une gifle."}
    dico_mots_H = {"HOMME":"L'être humain, en général","HEURE":"Espace de temps égal à la vingt-quatrième partie du jour","HEUREUX":"Qui bénéficie d'une chance favorable, que le sort favorise"}
    dico_mots_I = {"INVINCIBLE":"Qui ne peut être vaincu","INTERDIRE":"Defendre qqch","INVISIBLE":"Qui n'est pas visible, qui échappe à la vue."}
    dico_mots_J = {"JALOUSIE":"émotion secondaire qui représente des pensées et sentiments d'insécurité, de peur et d'anxiété concernant la perte anticipée ou pas d'un statut, d'un objet ou d'un lien affectif ayant une importante valeur personnelle","JANVIER":"Premier mois de l'année.","JEU":"Activité physique ou mentale dont le but essentiel est le plaisir qu'elle procure."}
    dico_mots_K = {"KLAXON":"Avertissement sonore","K-O":"Battue par .....","KETCHUP":"Sauce à base de tomates legeremnt sucrée et épicée"}
    dico_mots_L = {"LOUER":"Prendre en location, à bail.","LOUPER":"Ne pouvoir prendre, laisser échapper.","LOUP":"Mammifère carnivore sauvage, qui ressemble à un grand chien"}
    dico_mots_M = {"MENTIR":"Affirmer ce qu'on sait être faux","MIER":"Mettre un enjeu","MERE":"Femme qui a mis au monde un ou plusierus enfants"}
    dico_mots_N = {"NEUTRE":"Qui ne participe pas à un conflit.","NAGER":"Se mouvoir sur ou dans l'eau par des mouvements appropriés.","NARCISSISME":"Admiration, contemplation de soi-même."}
    dico_mots_O = {"ORGUEIL":"Opinion très avantageuse qu'une personne a de sa propre valeur aux dépens de la considération due à autrui.","OU":"conjonction, Autrement dit. ","OCCUPER":"Prendre possession de"}
    dico_mots_P = {"PRINCE":"Celui qui possède une souverenité","POSSIBLE":"Qui peut etre realisé","PRETER":"Mettre qqch à la disposition de qqn pour un temps determiner"}
    dico_mots_Q = {"QUESTION":"Demande qu'on adresse à qlqn afin d'apprendre qqch","QUATRE":"Trois plus un","QUESTIONNER":"Poser des questions"}
    dico_mots_R = {"RATER":"Manquer son coup","REMERCIER":"Dire merci","REMARQUER":"Avoir la vue, l'atention frappée par qlch"}
    dico_mots_S = {"SOIR":"Fin du jour, moments qui précèdent et qui suivent le coucher du soleil.","SOLDAT":"Homme qui sert dans une armée.","SIESTE":"Repos pris après le repas de midi."}
    dico_mots_T = {"TERRAIN":"Étendue de terre","TERRE":"L'élément solide qui supporte les êtres vivants et où poussent les végétaux.","TERREUR":"Peur extrême qui bouleverse, paralyse."}
    dico_mots_U = {"UNIR":"Mettre ensemble ","URINER":"Évacuer l'urine.","USER":"Avoir recours à"}
    dico_mots_V = {"VIVRE":"Être en vie","VIN":"Boisson alcoolisée provenant de la fermentation du raisin.","VIDER":"Rendre vide"}
    dico_mots_W = {"WAGON":"Véhicule sur rails, tiré par une locomotive.","WEB":"Ensemble des données reliées par des liens hypertextes, sur Internet.","WEEK-END":"Congé de fin de semaine, comprenant le samedi et le dimanche"}
    dico_mots_X = {"XENOPHOBE":"Hostile par principe aux étrangers, à ce qui vient de l'étranger.","XENOPHOBIE":"Hostilité de principe envers les étrangers, ce qui vient de l'étranger.","XYLOPHAGE":"Qui ronge le bois."}
    dico_mots_Y = {"YAOURT":"Lait caillé et fermenté.","YOGA":"Doctrine et exercices traditionnels hindous, cherchant à réunir l'individu avec le principe de toute existence.","YOUPI":"Cri d'enthousiasme, souvent accompagné d'un geste exubérant."}
    dico_mots_Z = {"ZERO":"Nombre qui represente un ensemble vide","ZOMBI":"Esprit d'un mort qu'un sorcier met à son service","ZOO":"Parc zoologique"}

    liste_dico_mots = [dico_mots_A,dico_mots_B,dico_mots_C,dico_mots_D,dico_mots_E,dico_mots_F,dico_mots_G,dico_mots_H,dico_mots_I,dico_mots_J,dico_mots_K,dico_mots_L,dico_mots_M,dico_mots_N,dico_mots_O,dico_mots_P,dico_mots_Q,dico_mots_R,dico_mots_S,dico_mots_T,dico_mots_U,dico_mots_V,dico_mots_W,dico_mots_X,dico_mots_Y,dico_mots_Z]



    fichier_pseudo_copy = open('base_pseudo_copy.txt', 'r') # ouverture du fichier point

    ligne = fichier_pseudo_copy.readlines()
    for line in ligne:
        
        pseudo = line
	


    
    fichier_pseudo_copy.close()







    fichier_point = open('fichier_point.txt', 'r') # ouverture du fichier point

    lignes = fichier_point.readlines()
    for ligne in lignes:
        
        point = ligne
        int_point = int(point)
	


    
    fichier_point.close()

    
    
    for i in range(3):
        num_lettre = randint(0, 25)
        choix_dico = liste_dico_mots[num_lettre]
        choix_mot_dico = choix_dico.keys()

        liste_mot = []                    
        liste_definition = []
    
        for mot in choix_dico.keys():
            liste_mot.append(mot)         #mettre les mots du dictionnaire dans une liste nouvelement crée

        for definition in choix_dico.values():
            liste_definition.append(definition)     #mettre les definition du dictionnaire dans une liste nouvelement crée
        
        mot1 = liste_mot[i]
        def1 = liste_definition[i]
    
        #AFFICHAGE DE LA PREMIERE QUESTION
        trash=os.system('cls')


    
        print("                        NIVEAU 2 DU JEU\n\n\n")
        print("Votre pseudo :",pseudo,"\n\n")
        print("Nombre de point:",int_point,"\n\n")
        nb_lettre = len(mot1)
        print("Question :",i+1)
        print("    Indice: ",def1)
        print("    Le mot commence par la lettre "+mot1[0]," et comporte ",(nb_lettre)," lettres")
        reponse = input("Votre reponse: ")
        REPONSE = reponse.upper()

        #VERIFICATION DE LA PREMIERE REPONSE
        if REPONSE != mot1:


        
            print("Woops, la reponse est fausse.")
        
            definition1 = def1[0:25]+"..."         #Prendre les 25 premieres lettres de la definition et remplacer le reste par ...
        
            fichier_reponse = open('fichier_reponse.txt', 'a')              # Mettre la reponse dans le fichier reponse

            line_rep = 'Indice:{}, Votre reponse :{} ,Vraie Reponse :{}\n'.format(definition1,REPONSE,mot1)
            fichier_reponse.write(line_rep)


            fichier_reponse.close()
        
        
    
        if REPONSE == mot1:

            int_point += 5
            print("Bravo, bonne reponse")
        
            definition1 = def1[0:25]+"..."         #Prendre les 25 premieres lettres de la definition et remplacer le reste par ...
        
            fichier_reponse = open('fichier_reponse.txt', 'a')              # Mettre la reponse dans le fichier reponse

            line_rep = 'Indice:{}, Votre reponse :{} \n'.format(definition1,REPONSE)
            fichier_reponse.write(line_rep)

            fichier_reponse.close()               
    
    str_point = str(int_point)
    fichier_point = open('fichier_point.txt', 'w') 
    fichier_point.write(str_point)

    fichier_point.close()


#------------------------------------------------NIVEAU 3---------------------------------------------------------------------------------------------

def niveau3():
    
    dico_mots_A = {"AGE":"Temps ecoulé depuis qu'une personne est en vie","AGRANDIR":"Rendre plus grand","AIMER":"Epprouver de l'affection"}
    dico_mots_B = {"BANDIT":"Malfaiteur vivant hors la lois","BARBE":"Poils du manton, des joues et de la levre superieur","BORDEL":"Maison de prostitution"}
    dico_mots_C = {"COLORER":"Revetir de couleur","COMBLER":"Remplir un vide","COMPETITION":"Epreuve sportive disputée entre plusieurs concurents"}
    dico_mots_D = {"DEUX":"Un plus un","DOIGT":"Chacun des cinq prolongements qui terminent la main de l'homme","DORMIR":"Être dans l'état de sommeil"}
    dico_mots_E = {"ENTRER":"Passer du dehors au dedans","ENLEVER":"Porter vers le haut.","ENDORMIR":"Faire dormir, amener au sommeil."}
    dico_mots_F = {"FIN":"Moment, instant auquel tout s'arrête","FAIM":"Sensation qui, normalement, accompagne le besoin de manger","FAUX":"Qui n'est pas vrai, qui est contraire à la vérité "}
    dico_mots_G = {"GRANDIR":"Devenir plus grand.","GAGNER":"S'assurer un profit matérie","GIFLER":"Frapper d'une gifle."}
    dico_mots_H = {"HOMME":"L'être humain, en général","HEURE":"Espace de temps égal à la vingt-quatrième partie du jour","HEUREUX":"Qui bénéficie d'une chance favorable, que le sort favorise"}
    dico_mots_I = {"INVINCIBLE":"Qui ne peut être vaincu","INTERDIRE":"Defendre qqch","INVISIBLE":"Qui n'est pas visible, qui échappe à la vue."}
    dico_mots_J = {"JALOUSIE":"émotion secondaire qui représente des pensées et sentiments d'insécurité, de peur et d'anxiété concernant la perte anticipée ou pas d'un statut, d'un objet ou d'un lien affectif ayant une importante valeur personnelle","JANVIER":"Premier mois de l'année.","JEU":"Activité physique ou mentale dont le but essentiel est le plaisir qu'elle procure."}
    dico_mots_K = {"KLAXON":"Avertissement sonore","K-O":"Battue par .....","KETCHUP":"Sauce à base de tomates legeremnt sucrée et épicée"}
    dico_mots_L = {"LOUER":"Prendre en location, à bail.","LOUPER":"Ne pouvoir prendre, laisser échapper.","LOUP":"Mammifère carnivore sauvage, qui ressemble à un grand chien"}
    dico_mots_M = {"MENTIR":"Affirmer ce qu'on sait être faux","MIER":"Mettre un enjeu","MERE":"Femme qui a mis au monde un ou plusierus enfants"}
    dico_mots_N = {"NEUTRE":"Qui ne participe pas à un conflit.","NAGER":"Se mouvoir sur ou dans l'eau par des mouvements appropriés.","NARCISSISME":"Admiration, contemplation de soi-même."}
    dico_mots_O = {"ORGUEIL":"Opinion très avantageuse qu'une personne a de sa propre valeur aux dépens de la considération due à autrui.","OU":"conjonction, Autrement dit. ","OCCUPER":"Prendre possession de"}
    dico_mots_P = {"PRINCE":"Celui qui possède une souverenité","POSSIBLE":"Qui peut etre realisé","PRETER":"Mettre qqch à la disposition de qqn pour un temps determiner"}
    dico_mots_Q = {"QUESTION":"Demande qu'on adresse à qlqn afin d'apprendre qqch","QUATRE":"Trois plus un","QUESTIONNER":"Poser des questions"}
    dico_mots_R = {"RATER":"Manquer son coup","REMERCIER":"Dire merci","REMARQUER":"Avoir la vue, l'atention frappée par qlch"}
    dico_mots_S = {"SOIR":"Fin du jour, moments qui précèdent et qui suivent le coucher du soleil.","SOLDAT":"Homme qui sert dans une armée.","SIESTE":"Repos pris après le repas de midi."}
    dico_mots_T = {"TERRAIN":"Étendue de terre","TERRE":"L'élément solide qui supporte les êtres vivants et où poussent les végétaux.","TERREUR":"Peur extrême qui bouleverse, paralyse."}
    dico_mots_U = {"UNIR":"Mettre ensemble ","URINER":"Évacuer l'urine.","USER":"Avoir recours à"}
    dico_mots_V = {"VIVRE":"Être en vie","VIN":"Boisson alcoolisée provenant de la fermentation du raisin.","VIDER":"Rendre vide"}
    dico_mots_W = {"WAGON":"Véhicule sur rails, tiré par une locomotive.","WEB":"Ensemble des données reliées par des liens hypertextes, sur Internet.","WEEK-END":"Congé de fin de semaine, comprenant le samedi et le dimanche"}
    dico_mots_X = {"XENOPHOBE":"Hostile par principe aux étrangers, à ce qui vient de l'étranger.","XENOPHOBIE":"Hostilité de principe envers les étrangers, ce qui vient de l'étranger.","XYLOPHAGE":"Qui ronge le bois."}
    dico_mots_Y = {"YAOURT":"Lait caillé et fermenté.","YOGA":"Doctrine et exercices traditionnels hindous, cherchant à réunir l'individu avec le principe de toute existence.","YOUPI":"Cri d'enthousiasme, souvent accompagné d'un geste exubérant."}
    dico_mots_Z = {"ZERO":"Nombre qui represente un ensemble vide","ZOMBI":"Esprit d'un mort qu'un sorcier met à son service","ZOO":"Parc zoologique"}

    liste_dico_mots = [dico_mots_A,dico_mots_B,dico_mots_C,dico_mots_D,dico_mots_E,dico_mots_F,dico_mots_G,dico_mots_H,dico_mots_I,dico_mots_J,dico_mots_K,dico_mots_L,dico_mots_M,dico_mots_N,dico_mots_O,dico_mots_P,dico_mots_Q,dico_mots_R,dico_mots_S,dico_mots_T,dico_mots_U,dico_mots_V,dico_mots_W,dico_mots_X,dico_mots_Y,dico_mots_Z]
    fichier_pseudo_copy = open('base_pseudo_copy.txt', 'r') 

    lines = fichier_pseudo_copy.readlines()
    for ligne in lines:
        
        pseudo = ligne
	
    fichier_pseudo_copy.close()
    

    fichier_point = open('fichier_point.txt', 'r')
    
    lignes = fichier_point.readlines()
    for ligne in lignes:
        
        mes_point = ligne
        point_int = int(mes_point)
	


    
    fichier_point.close()
    
    for i in range(3):
        num_lettre = randint(0, 25)
        choix_dico = liste_dico_mots[num_lettre]
        choix_mot_dico = choix_dico.keys()

        liste_mot = []                    
        liste_definition = []
    
        for mot in choix_dico.keys():
            liste_mot.append(mot)         #mettre les mots du dictionnaire dans une liste nouvelement crée

        for definition in choix_dico.values():
            liste_definition.append(definition)     #mettre les definition du dictionnaire dans une liste nouvelement crée
        
        mot1 = liste_mot[i]
        def1 = liste_definition[i]
    
        #AFFICHAGE DE LA PREMIERE QUESTION
        trash=os.system('cls')


        print("                        NIVEAU 3 DU JEU\n\n\n")
        print("Votre pseudo :",pseudo,"\n\n")
        print("Nombre de point:",point_int,"\n\n")
        nb_lettre = len(mot1)
        print("Question :",i+1)
        print("    Indice: ",def1)
        print("    Le mot commence par la lettre "+mot1[0]," et comporte ",(nb_lettre)," lettres")
        reponse = input("Votre reponse: ")
        REPONSE = reponse.upper()

        #VERIFICATION DE LA PREMIERE REPONSE
        if REPONSE != mot1:


        
            print("Woops, la reponse est fausse.")
        
            definition1 = def1[0:25]+"..."         #Prendre les 25 premieres lettres de la definition et remplacer le reste par ...
        
            fichier_reponse = open('fichier_reponse.txt', 'a')              # Mettre la reponse dans le fichier reponse

            line_rep = 'Indice:{}, Votre reponse :{} ,Vraie Reponse :{}\n'.format(definition1,REPONSE,mot1)
            fichier_reponse.write(line_rep)


            fichier_reponse.close()
        
        
    
        if REPONSE == mot1:
            point_int = point_int + 5
            print("Bravo, bonne reponse")
        
            definition1 = def1[0:25]+"..."         #Prendre les 25 premieres lettres de la definition et remplacer le reste par ...
        
            fichier_reponse = open('fichier_reponse.txt', 'a')              # Mettre la reponse dans le fichier reponse

            line_rep = 'Indice:{}, Votre reponse :{} \n'.format(definition1,REPONSE)
            fichier_reponse.write(line_rep)

            fichier_reponse.close()

        
    print(" \n\n")
    print(pseudo," vous avez eu en tout ",point_int,"points")   
    os.system('pause')
    point_str = str(point_int)
    fichier_point = open('fichier_point.txt', 'w') 
    fichier_point.write(point_str)

    fichier_point.close()






#---------------------------------------------------------------------------------------------------------------------------------------------------------
    



def copie_fichier_pseudo_in_liste(liste):
    fichier = open('base_pseudo.txt','r')
    with open('base_pseudo.txt') as file:
        for line in fichier:
            liste.append(line)


def copie_liste_pseudo_in_liste(liste_copie):
    liste = []
    copie_fichier_pseudo_in_liste(liste)
    taille_liste = len(liste)
    for i in range(taille_liste):
        pseudo = liste[i]
        taille_pseudo = len(pseudo)
        true_pseudo = pseudo[:taille_pseudo-1]
        true_taille_pseudo = len(true_pseudo)

        liste_copie.append(true_pseudo)

def localise_pseudo(liste,liste_position,mon_pseudo):
    copie_liste_pseudo_in_liste(liste)
    taille = len(liste)
    for pseudo in liste:
        if mon_pseudo == pseudo:
            mon_pseudo = pseudo
    position = liste.index(mon_pseudo)
    liste_position.append(position)





def scores_joeurs():
    print("AFFICHAGE DES POINTS ")
    


























def commencer_jeu():

    os.system('pause')
    niveau1()
    os.system('pause')
    niveau2()
    os.system('pause')
    niveau3()

    fichier_reponse = open('fichier_reponse.txt', 'r')
    os.system('cls')
    print("                        AFFICHAGE DU RESULTAT\n\n\n")
    lignes = fichier_reponse.readlines()
    for ligne in lignes:
        print(ligne, end='')
	


    
    fichier_reponse.close()
    fichier_reponse = open('fichier_reponse.txt', 'w')
    fichier_reponse.close()
    os.system('pause')
    menu_jeu_connexion()
    
    





    





	




    
            
                         
    
#PAGE D'INSCRIPTION-------------------------------------------------------------------------------------------------------------------------------------

def Inscription(fichier_inscription,fichier_pseudo):
    trash=os.system('cls')
    print("                        INSCRIPTION\n\n\n")
    fichier_pseudo = open('base_pseudo.txt', 'r')

    nom = input("Entrer votre nom complet: ")
    pseudo = input("Entrer votre pseudo: ")
    for line in fichier_pseudo:
        while pseudo in line:
            pseudo = input("Ce pseudo existe deja, veuillez entrer un autre: ")
    mot_de_pass = input("Entrer votre mot de passe: ")
    dateIscription = str(date)
    
    fichier_pseudo.close()
    #liste = [nom,pseudo,mot_de_pass,dateIscription]
    fichier_inscription = open('base_inscrit.txt', 'a')
    fichier_pseudo = open('base_pseudo.txt', 'a')
    fichier_MotDePass = open('base_MotDePass.txt', 'a')
    line_inscription = 'Nom:{}, Pseudo:{}, Mot de passe:{}, Date de inscription:{}\n'.format(nom,pseudo,mot_de_pass,dateIscription)
    fichier_inscription.write(line_inscription)
    line_pseudo = '{}\n'.format(pseudo)
    fichier_pseudo.write(line_pseudo)
    line_mot_de_pass = '{}\n'.format(mot_de_pass)
    fichier_MotDePass.write(line_mot_de_pass)
    print("Vous vous etes inscrit avec succes ")
    os.system('pause')
    fichier_MotDePass.close()
    fichier_pseudo.close()
    fichier_inscription.close()
    menu()  







#PAGE DE CONNEXION---------------------------------------------------------------------------------------------------------------------------------

#La connexion au jeu


def menu_jeu_connexion():
    trash=os.system('cls')
    
    print("                        BIENVENU DANS LE JEU\n\n\n")
    print("1.Commencer")
    print("2.Quitter")
    choix= input(" Votre choix svp : ")
    while choix != "1" and choix != "2" :
        choix= input(" Votre choix svp : ")
    if choix == "1" :
        commencer_jeu()
        menu()
            
    if choix == "2" :
        print("      ::")
        print("    ::")
        print("  :::::::::")
        print(":::::::::::")
        print("  :::::::::")
        print("    ::")
        print("      ::")
       

        




def Connexion(fichier_pseudo,fichier_MotDePass):
    print("                        CONNEXION \n\n\n")
    pseudo = input("Pseudo :")
    mot_de_pass = input("Mot de passe :")

    fichier_pseudo = open('base_pseudo.txt', 'r')
    fichier_MotDePass = open('base_MotDePass.txt', 'r')
    verifP = 0
    verifM = 0
    for line_p in fichier_pseudo:
        if pseudo in line_p:
            fichier_pseudo_copy = open('base_pseudo_copy.txt', 'w')
            vrai_pseudo = line_p
            fichier_pseudo_copy.write(vrai_pseudo)
            fichier_pseudo_copy.close()
            verifP += 1  
    for line_m in fichier_MotDePass:
        if mot_de_pass in line_m:
            verifM += 1
    if verifP > 0 and verifM > 0:
        menu_jeu_connexion()
        
            
    if verifP == 0 or verifM == 0:
        print("Vous n'etes pas inscrit\nVEUILLEZ VOUS INSCRIRE")
        os.system('pause')
        trash=os.system('cls')
        print("1.Inscription\n2.Quitter")
        choix = input(" Votre choix svp : ")
        while choix != "1" and choix != "2":
            choix = input("VEUILLEZ ENTRER UNE VRAIE VALEUR :") 
        if choix == "1":
            Inscription(fichier_inscription,fichier_pseudo)
            print("1.Connectez-vous pour jouer\n2.Retour au menu principal")
            rep = ("Votre choix svp :")
            
            while rep != "1" and rep !="2":
                rep = input("VEUILLEZ ENTRER UNE VRAIE VALEUR :")

            if rep == "1":
                Connexion(fichier_pseudo,fichier_MotDePass)

            if rep == "2":
                print(":::::::::::::")
                
                
            
        if choix == "2":
            print("Retour au menu Principal")
            os.system('pause')
            #menu()
            
        
    
            #os.system('pause')

    
    
    
        
        
    fichier_MotDePass.close()

    
    fichier_pseudo.close()
    
    
    























#LE MENU DE CHOIX------------------------------------------------------------------------------------------------------------------------------------    

def menu():


    fichier_inscription = open('base_inscrit.txt', 'a')
    fichier_pseudo = open('base_pseudo.txt', 'a')
    fichier_MotDePass = open('base_MotDePass.txt', 'r')
    fichier_score = open('base_inscrit.txt', 'a')
    fichier_joker = open('base_inscrit.txt', 'a')
    fichier_niveau = open('base_inscrit.txt', 'a')
    liste_pseudo = []

    
    print("                        BIENVENU SUR TROUVE LE MOT\n\n\n\n\n")
    print("PRINCIPE DU JEU\n\n")
    print("Le jeu consiste à deviner le mot generer par l'ordinateur \nen vous basant sur sa definition et sa premiere lettre\nNB :les caracteres speciaux comme - et _ sont considere comme des lettres")
    print("\n\n\n\n")
    print("1. Connexion")
    print("2. Inscription")
    print("3. Sortir")
    choix = input("Votre choix:")
    
    while choix != "1" and choix != "2" and choix !="3"  :
        choix= input(" Votre choix svp : ")
    if choix == "1" :
        Connexion(fichier_pseudo,fichier_MotDePass)
           
    if choix == "2" :
        Inscription(fichier_inscription,fichier_pseudo)

    if choix == "3" :
        print("Bye Bye (-.-)")
    

    fichier_niveau.close()
    fichier_joker.close()
    fichier_score.close()
    fichier_MotDePass.close()        
    fichier_pseudo.close()
    fichier_inscription.close()
    
















#LA FONCTION PRINCIPAL MAIN--------------------------------------------------------------------------------------------------------------------------


def main():
   
    
    trash=os.system('cls')
    menu()
    
    
		
if __name__== '__main__':
    main()


















































































"""
def affiche_clubs(liste):     #Afficher tous les clubs de la liste
    print("AFFICHAGE DE TOUS LES CLUBS DE LA LISTE\n\n")
    taille=len(liste)
    for i in range(0,taille):
        liste_c=liste[i]
        print(liste_c)
        
def affiche_triee(liste):     #Afficher la liste des clubs triees
    
    print("AFFICHAGE TRIEE DE TOUS LES CLUBS DE LA LISTE\n\n")
    taille=len(liste)
    for i in range(0,taille): 
        liste.sort()
        liste_c=liste[i]
        print(liste_c)
    

def affiche_dernier(liste_cu):   #Afficher les clubs en commencant par le dernier

    print("AFFICHAGE INVERSE DE TOUS LES CLUBS DE LA LISTE\n\n")
    taille=len(liste_cu)
    i = (taille-1)
    while i>(-1):
        liste_c = liste_cu[i]
        print(liste_c)
        i -= 1

def menu_principal_affiche():
    
    print("LE MENU D AFFICHAGE\n\n")
    print("1.Afficher tous les clubs de la liste")
    print("2.Afficher la liste des clubs triees")
    print("3.Afficher la liste en commencant par le dernier club")
    print("4.Quitter")


def menu_affiche(liste):
    trash=os.system('cls')
    #liste_clubs = ["Barcelone","Real Madrid","Benfica","Liverpool","Manchester City","PSG","Naples"]
    menu_principal_affiche()
    choix=input("Votre choix : ")
    while choix != "4" :
        if choix == "1" :
            trash=os.system('cls')
            affiche_clubs(liste)
            #affiche_clubs(liste_clubs)
        if choix == "2" :
            trash=os.system('cls')
            affiche_triee(liste)
            #affiche_triee(liste_clubs)
        if choix == "3" :
            trash=os.system('cls')
            #liste=["Barcelone","Real Madrid","Benfica","Liverpool","Manchester City","PSG","Naples"]
            #liste_clubs = ["Barcelone","Real Madrid","Benfica","Liverpool","Manchester City","PSG","Naples"]
            affiche_dernier(liste)
         
        menu_principal_affiche() 
        choix=input("Votre choix : ")              




        

def Affichage(liste_clubs):    
    menu_affiche(liste_clubs)

"""
