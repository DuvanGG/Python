PATH = 'archivo.txt'

def main():
    escribirArchivo()


def escribirArchivo():
    f = open(PATH, 'w')
    f.write("Escribiendo en txt\n")
    f.close
    f = open(PATH, 'r+')
    f.readline()
    f.write("Segunda vez escribiendo en txt")
    f.close


if __name__ == '__main__':
    main()