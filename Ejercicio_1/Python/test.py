import sys

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 1:
        with open(args[0]) as f:
            lines = f.readlines()
            print('Cantidad de numeros en la lista: ' + str(len(lines)))