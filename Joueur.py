#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Joueur:
    def __init__(self):
        self.nom=""
        self.sante = 100
        self.sante_max = 100
        self.force = 10
        self.armure = 10

nom = input("Entrez le nom du joueur : ")
player = Joueur()
player.nom = nom
print(f"Le joueur {player.nom} a {player.sante} de vie et {player.force} de force et {player.armure} d'armure")
