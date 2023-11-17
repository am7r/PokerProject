import numpy as np
import pandas as pd

card1 = []
card2 = []
flop1 = []
flop2 = []
flop3 = []
turn = []
river = []
numCommunity = 0

def setHand():
    card1 = input("First Card: ")
    card2 = input("Second Card: ")

    if len(card1) > 2:
        card1 = (int(card1[0:2]), card1[-1])
        
    else:
        card1 = (int(card1[0]), card1[1])

    if len(card2) > 2:
        card2 = (int(card2[0:2]), card2[-1])
    else:
        card2 = (int(card2[0]), card2[1])

    print(card1[0])
    print(card2[0])

def calculatePair():
    if card1[0] == card2[0]:
        return 
    
    

    