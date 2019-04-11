import sys
import file as f
import cardGUI as cgui
import backend as engine
import random

#Inisiasi operator
listOp = ['+','-','*','/'] 

def generateCards():
    hand = []
    for i in range(4):
        while True:
            num1 = random.randint(1,13)
            num2 = random.randint(1,4)
            if num2 == 1:
                suit = 'Heart'
            if num2 == 2:
                suit = 'Spade'
            if num2 == 3:
                suit = 'Diamond'
            if num2 == 4:
                suit = 'Club'
            if ([suit,num1] not in hand):
                hand.append([suit,num1])
                break

    return hand

    
def main():
    #Generate 4 kartu
    listCards = generateCards() #listCard[suit][num]

    listNb = []
    for x in listCards:
        listNb.append(x[1])

    #Sort descending
    sortedCards = sorted(listCards, key=lambda x:x[1], reverse=True)
    listNb = []
    for x in sortedCards:
        listNb.append(x[1])

    op = engine.solusiOp(listNb, listOp)

    solusi = engine.solve(listNb, listOp)

    strSolusi = ''.join(solusi)
    
    if eval(strSolusi) == 24:
        print('Solusi ditemukan')
        print(strSolusi)
    else:
        print('Solusi tidak ditemukan')
        print(strSolusi + ' = ' + str(eval(strSolusi)))

    cgui.cardGUI(listCards, op, strSolusi)

    return 0

main()