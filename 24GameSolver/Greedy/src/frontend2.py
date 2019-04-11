import sys
import file as f
import backend as engine

listOp = ['+','-','*','/']   
    
def main():
    #Membaca file input
    Nb = f.openFile(sys.argv[1])

    #Mengubah string menjadi list of char
    listNb = Nb.split(' ')

    #Mengubah list of char menjadi list of integer sesuai nilai kartu
    listNb = engine.cardsToNb(listNb)

    strSolusi = ''.join(engine.solve(listNb, listOp))
    #Validasi apakah solusi bernilai 24
    if eval(strSolusi) == 24:
        print(strSolusi)
    else:
        print('Solusi tidak ditemukan.')

    #Mengeluarkan file output
    f.writeFile(sys.argv[2], strSolusi)

    return 0

main()

