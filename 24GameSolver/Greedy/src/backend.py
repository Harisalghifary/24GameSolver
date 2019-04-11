#Fungsi untuk mengubah string menjadi integer sesuai nilai kartu
def cardsToNb(listNb):
    convertedList = []
    for x in listNb:
        if x == 'A':
            convertedList.append(1)
        elif x == 'J':
            convertedList.append(1)
        elif x == 'Q':
            convertedList.append(1)
        elif x == 'K':
            convertedList.append(1)
        else:
            convertedList.append(int(x))

    return convertedList

#Fungsi untuk membuat list solusi angka dan operator 
def solve(listNb, listOp):
    #Sorting list input mulai dari yang terbesar ke terkecil
    nb = sorted(listNb, reverse=True)
    
    op = solusiOp(nb, listOp)
    #Inisialisasi list solusi operator
    solusi = [str(nb[0]),op[0],str(nb[1]),op[1],str(nb[2]),op[2],str(nb[3])]

    return solusi

#Fungsi untuk membuat list operator yang dipilih melalui algoritma greedy
def solusiOp(sortedListNb, listOp):

    #Inisialisasi list solusi operator
    op = []

    #Algoritma greedy untuk memasukkan solusi ke dalam list
    x = sortedListNb[0]

    for i in sortedListNb[1:]:
        closestNb = 999
        for j in listOp:
            Nb = eval(str(x) + j + str(i))
            diff = abs(Nb - 24)
            if (diff <= abs(closestNb - 24)):
                closestNb = Nb
                selectedOp = j
        x = closestNb
        op.append(selectedOp)
            
    return op
    