#!/bin/env#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint

class Joueur():
    def __init__(self):
        super().__init__()
        self.pseudo=""
        self.health=20
        self.force=8
        self.armure=5

monstre=Joueur()
monstre.pseudo="Monstre"
monstre.health=randint(5,20)
monstre.force=randint(3,8)
monstre.armure=randint(0,5)

print(f"{monstre.pseudo} a {monstre.health} points de vie {monstre.force} points de force et {monstre.armure}")
