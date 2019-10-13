'''
Created on Dec 20, 2018

@author: Steve
'''
# Perform the Tarokka Card Reading

import random

def reading():
    suits = ["Swords", "Coins", "Stars", "Glyphs"]
    numbers = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Master"]
    highs = ["Artifact", "Beast", "Broken One", "Darklord", "Donjon", "Ghost", "Executioner", "Horseman", "Innocent", "Marionette", "Mists", "Raven", "Seer", "Tempter"]
    for card in range(1,4):
        rand_suit = random.randint(0,3)
        rand_num = random.randint(0,9)
        suit = suits[rand_suit]
        number = numbers[rand_num]
        output = "Card " + str(card) + " is the " + str(number) + " of " + str(suit) + "."
        print(str(output))
    for highcard in range(4,6):
        rand_high = random.randint(0,13)
        high = highs[rand_high]
        highoutput = "Card " + str(highcard) + " is the " + str(high) + "."
        print(str(highoutput))


if __name__ == '__main__':
    reading()