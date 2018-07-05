from utils import *

if __name__ == '__main__':

    filename = 'data/puzzle.txt'

    file1 = load_puzzle(filename)
    data = decode_file(file1)
    show_puzzle(data)
    print(data)
