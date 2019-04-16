#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 08:10:12 2019

@author: vla35123
"""

import random

def malapismena():
    try:
        JmenoVS = input ('\nZadej jméno vstupního souboru: ')
        SouborVS = open (JmenoVS, 'r')
        JmenoVY = input ('Zadej jméno výstupního souboru: ')
        SouborVY = open (JmenoVY, 'w')
        while True:
            radek = SouborVS.readline()
            if radek == '':
                break
            else:
                SouborVY.write(radek.lower())
        print ('\nHotovo')
        SouborVS.close()
        SouborVY.close()
    except IOError:
        print ('\nChyba, zkus to znova')

def nahrada():
    try:
        JmenoVS = input ('\nZadej jméno vstupního souboru: ')
        SouborVS = open (JmenoVS, 'r')
        JmenoVY = input ('Zadej jméno výstupního souboru: ')
        SouborVY = open (JmenoVY, 'w')
        Stary = input ('Který znak se má nahradit: ')
        Novy = input ('Jakým znakem se má nahradit: ')
        while True:
            radek = SouborVS.readline()
            if radek == '':
                break
            else:
                SouborVY.write(radek.replace(Stary, Novy))
        print ('\nHotovo')
        SouborVS.close()
        SouborVY.close()
    except IOError:
        print ('\nChyba, zkus to znova')

def statistika():
    try:
        JmenoVS = input ('\nZadej jméno vstupního souboru: ')
        SouborVS = open (JmenoVS, 'r')
        radky = 0
        znaky = 0
        slova = 0
        cetnost = {}
        while True:
            radek = SouborVS.readline()
            if radek == '':
                break
            else:
                radky += 1
                znaky += len(radek)
                slova += len(radek.split())
                for STznak in radek:
                    znak = STznak.upper()
                    if znak in (' ', '\t', '\n'):
                        continue
                    if znak in cetnost:
                        cetnost[znak] += 1
                    else:
                        cetnost[znak] = 1
        
        for znak in sorted(cetnost):
            print (znak, '=', cetnost[znak])
        print ('Počet řádků:', radky)
        print ('Počet slov:', slova)
        print ('Počet znaků:', znaky)
        SouborVS.close()
        print ('\nHotovo')
    except IOError:
        print ('\nChyba, zkus to znova')

def nahodnytext():
    try:
        JmenoVY = input ('\nZadej jméno výstupního souboru: ')
        SouborVY = open (JmenoVY, 'w')
        samohlasky = 'aeiyou'
        souhlasky = 'qwrtzpsdfghjklxcvbnm'
        for i in range (50):
            delka = random.randint (1,10)
            zacatek = random.randint (False, True)
            for i in range (delka):
                if zacatek:
                    SouborVY.write(random.choice(souhlasky))
                else:
                    SouborVY.write(random.choice(samohlasky))
                zacatek = not(zacatek)
            SouborVY.write(' ')
        SouborVY.close()
        print ('\nHotovo')
    except IOError:
        print ('\nChyba, zkus to znova')
    
while True:
    print ('\nMenu')
    print ('1) Převod na malá písmena')
    print ('2) Nahrazení znaků')
    print ('3) Statistika souboru')
    print ('4) Generování náhodného textu')
    print ('5) Konec')
    try:
        volba = int(input('Tvá volba: '))
        if volba == 1:
            malapismena()
        elif volba == 2:
            nahrada()
        elif volba == 3:
            statistika ()
        elif volba == 4:
            nahodnytext()
        elif volba == 5:
            exit (0)
        else:
            print ('Vyber číslo 1 - 5: ')
    except ValueError:
        print ('Vyber číslo 1 - 5: ')
    except EOFError:
        exit (0)
