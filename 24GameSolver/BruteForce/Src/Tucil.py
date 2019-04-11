#Tugas Kecil Stima "24 Game Solver" 
#Author : Haris Salman Al-Ghifary

import time
def main_program():
    print("\n")
    print("---------------------------------------------")
    print("----------Welcome to 24 Game Solver----------")
    print("---------------------------------------------")
    print("\n")

    #Bagian input program
    list_angka = a,b,c,d = [str(n) for n in input("Enter your 4 numbers in positive number: ").split()]
    while (int(a)<0 or int(b)<0 or int(c)<0 or int(d)<0):
        print("Please insert a positive number")
        list_angka = a,b,c,d = [str(n) for n in input("Enter your 4 numbers in positive number: ").split()]
    
    #inisialisasi kombinatorik operator
    operator = ['*','/','+','-']
    kombinasi_opr = []
    for opr1 in range(4):
        for opr2 in range(4):
            for opr3 in range(4):
                    kombinasi_opr.append([operator[opr1],operator[opr2],operator[opr3]])
    
    #inisialisasi untuk menghitung waktu eksekusi 
    start_time = time.time()

    #inisialisasi kombinatorik angka
    temp = []
    for angka1 in range(4):
        for angka2 in range(4):
            for angka3 in range(4):
                for angka4 in range(4):
                    if (angka1!=angka2 and angka1!=angka3 and angka1!=angka4 and angka2!=angka3 and angka2!=angka4 and angka3!=angka4):
                        temp.append([list_angka[angka1],list_angka[angka2],list_angka[angka3],list_angka[angka4]])
    
   
    kombinasi_angka = []
    for n in temp:
        kombinasi_angka.append(tuple(n))
    kombinasi_angka = list(set(kombinasi_angka))

    #inisialisasi kombinatorik parenthesis,angka,opertor
    kombinasi_all = []
    for i in range(len(kombinasi_angka)):
        for j in range(len(kombinasi_opr)):
            kombinasi_all= kombinasi_all + [	'(' + kombinasi_angka[i][0] + kombinasi_opr[j][0] + kombinasi_angka[i][1] + ')' + kombinasi_opr[j][1] + '(' + kombinasi_angka[i][2] + kombinasi_opr[j][2] + kombinasi_angka[i][3] + ')',
										'((' + kombinasi_angka[i][0] + kombinasi_opr[j][0] + kombinasi_angka[i][1] + ')' + kombinasi_opr[j][1] + kombinasi_angka[i][2] + ')' + kombinasi_opr[j][2] + kombinasi_angka[i][3],
										'(' + kombinasi_angka[i][0] + kombinasi_opr[j][0] + '(' + kombinasi_angka[i][1] + kombinasi_opr[j][1] + kombinasi_angka[i][2] + '))' + kombinasi_opr[j][2] + kombinasi_angka[i][3],
										kombinasi_angka[i][0] + kombinasi_opr[j][0] + '((' + kombinasi_angka[i][1] + kombinasi_opr[j][1] + kombinasi_angka[i][2] + ')' + kombinasi_opr[j][2] + kombinasi_angka[i][3] + ')',
										kombinasi_angka[i][0] + kombinasi_opr[j][0] + '(' + kombinasi_angka[i][1] + kombinasi_opr[j][1] + '(' + kombinasi_angka[i][2] + kombinasi_opr[j][2] + kombinasi_angka[i][3] + '))' ]
    
    #Banyak solusi
    count = 0

    for n in range(len(kombinasi_all)):
        try:
            if (round(eval(kombinasi_all[n]),6)==24):
                print("==>", kombinasi_all[n])
                count = count+1
        except ZeroDivisionError:
            pass
    print("\n")
    print("Oh", count , "solution found")
  
    end = time.time()
    print("Time excecution = ",end-start_time)
    print("\n")
main_program()