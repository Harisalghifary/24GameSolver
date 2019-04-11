#Front-end untuk membaca input dan menghasilkan file output

def openFile(file_name):
    with open(file_name, 'r') as f_in:
        Nb = f_in.read()

    return Nb

def writeFile(file_name, solution):
    with open(file_name, 'w+') as f_out:
        f_out.write(solution)