#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# nom de fichier : xml.py

import xml.etree.ElementTree as ET

class Individus:
    rang = 0
    def __init__(self, nom, prenom, email, tel):
        Individus.rang += 1
        self.ident = Individus.rang
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.tel = tel

    def afficher(self):
        print("Nom :{0} --- Prénom : {1} ---  Mail :{2} ---  Téléphone :{3} ".format(self.nom, self.prenom, self.email, self.tel ))

class Carnet:
    def __init__(self):
        self.Individus = list()

    def charger_fichier(self, individus):
        self.Individus.append(individus)

    def ajouter(self):

        print("\nAjout d'un contact")
        try:
            nom = input("Son nom: ")
            if nom in self.Individus:
                print("Ce contact existe déjà.")
                print("Voulez-vous le modifier ?")
            else:
                prenom = input("Son Prénom :")
                email = input("Son email : ")
                telephone = input("Son téléphone : ")
                nouveau = Individus(nom, prenom, email, telephone)
                self.Individus.append(nouveau)

        except IOError:
            '''Carnet non créé : vérification impossible'''
            prenom = input("Son Prénom :")
            email = input("Son email : ")
            telephone = input("Son téléphone : ")
            nom = Individus(nom, prenom, email, telephone)


    def afficher(self):
        for individus in self.Individus:
            individus.afficher()

    def charger(self, nomFichier):
        tree = ET.parse(nomFichier)
        for client in tree.iter('client'):
            self.charger_fichier(Individus(client.find("nom").text, client.find("prenom").text, client.find("email").text, client.find("tel").text))

    def modifier(self):
        exit(0)



    def rechercher(self):
        print("Recherche d'un contact")
        recherche = input("Saisisez le nom")
        for individu in self.Individus:
            if recherche == individu.nom:
                print("Nom :{0} --- Prénom : {1} ---  Mail :{2} ---  Téléphone :{3} ".format(individu.nom,individu.prenom,individu.email,                                                                                    individu.tel))

        else:
            print("Contact absent du listing.")

    def supprimer(self):
        exit(0)

    def effacer(self):
        exit(0)



#
#
#               While du programme
#
#

carnet = Carnet()
carnet.charger('data.xml')
running = True

while running:
    print(" .....Gestion du carnet d'adresse..... ")
    print("1. Ajouter un contact")
    print("2. Modifier un contact")
    print("3. Rechercher un contact")
    print("4. Supprimer un contact")
    print("5. Voir la liste des contacts")
    print("6. Effacer l'ensemble des contacts")
    print("7. Quitter")

    try:
        #saisie du choix
        rep = eval(input("Choix : "))

        #Conditions
        #Ajout d'un contact
        if rep == 1:
            carnet.ajouter()

        #Modifier un contact
        elif rep == 2:
            carnet.modifier()

        #Rechercher un contact
        elif rep == 3:
            carnet.rechercher()

        #Supprimer un contact
        elif rep == 4:
            carnet.supprimer()

        #Liste des contacts
        elif rep == 5:
            carnet.afficher()

        #Effacer l'ensemble du carnet
        elif rep == 6:
            carnet.effacer()

        #Quitter
        elif rep == 7:
            exit()

        else :
            print("Veuillez entrer un choix valide")

    except NameError:
        print("Veuillez entrer un choix valide.")
        continue
    except SyntaxError:
        print("Veuillez entrer un choix valide.")
        continue
    except EOFError:
        print("\nVeuillez entrer 7 comme choix pour quitter le programme.")
        continue
    except KeyboardInterrupt:
        print("\nVeuillez entrer 7 comme choix pour quitter le programme.")
        continue