#GUI untuk menampilkan kartu

from tkinter import *

def cardGUI(listCards, op, strSolusi):
    sortedCards = sorted(listCards, key=lambda x:x[1], reverse=True)

    root = Tk()

    canv = Canvas(root, width=1200, height=640, bg='grey')
    x1 = 200
    x2 = 200
    x3 = 330

    card1 = []
    card2 = []
    card3 = []

    #Menampilkan kartu awal
    for i, a in enumerate(listCards):
        card1.append(PhotoImage(file = "../img/" + a[0] + str(a[1]) + ".png"))
        canv.create_image(x1, 50, anchor = NE, image = card1[i])
        x1 = x1 + 130

    #Menampilkan kartu yang disusun membentuk solusi
    for j, b in enumerate(sortedCards):
        card2.append(PhotoImage(file = "../img/" + b[0] + str(b[1]) + ".png"))
        canv.create_image(x2, 300, anchor = NE, image = card2[j])
        x2 = x2 + 260

    for k, c in enumerate(op):
        if c == '+':
            card3.append(PhotoImage(file = "../img/plus.png"))
            canv.create_image(x3, 300, anchor = NE, image = card3[k])
        elif (c == '-'):
            card3.append(PhotoImage(file = "../img/minus.png"))
            canv.create_image(x3, 300, anchor = NE, image = card3[k])
        elif c == '*':
            card3.append(PhotoImage(file = "../img/times.png"))
            canv.create_image(x3, 300, anchor = NE, image = card3[k])
        elif c == '/':
            card3.append(PhotoImage(file = "../img/divide.png"))
            canv.create_image(x3, 300, anchor = NE, image = card3[k])
        x3 = x3 + 260
    
    labelfont = ('calibri', 20, 'bold')

    if eval(strSolusi) == 24:
        widget1 = Label(root, text='Solusi ditemukan')
        widget1.config(bg='white', fg='black')  
        widget1.config(font=labelfont)           
        widget1.config(height=1, width=20)       
        widget1.pack(expand=YES, fill=BOTH)
    else :
        widget1 = Label(root, text='Solusi tidak ditemukan')
        widget1.config(bg='white', fg='black')  
        widget1.config(font=labelfont)           
        widget1.config(height=1, width=20)       
        widget1.pack(expand=YES, fill=BOTH)

    widget2 = Label(root, text=(strSolusi + ' = ' + str(eval(strSolusi))))
    widget2.config(bg='white', fg='black')  
    widget2.config(font=labelfont)           
    widget2.config(height=1, width=20)       
    widget2.pack(expand=YES, fill=BOTH)

    canv.pack()
    root.mainloop()