#!/bin/env#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Joueur():
    def __init__(self):
        super().__init__()
        self.pseudo=""
        self.health=20
        self.force=8
        self.armure=5

joueur=Joueur()
compteur=0
while joueur.health != 0:
    compteur += 1
