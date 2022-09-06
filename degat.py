#!/bin/env#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Joueur():
    def __init__(self):
        super().__init__()
        self.pseudo=""
        self.sante=20
        self.force=8
        self.armure=5

joueur = Joueur()

if joueur.sante >= 8:
   joueur.armure -=1
else:
    joueur.armure -=2  


nom=input("Quel est votre nom ? : ")
joueur.pseudo=nom
print(f"{joueur.pseudo} a {joueur.sante} points de vie {joueur.force} points de force et {joueur.armure}")
print(f"il vous reste {joueur.sante}")
print("nouvelle ligne")