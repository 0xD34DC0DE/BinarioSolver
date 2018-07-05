import numpy as np
import matplotlib.pyplot as plt


def show_puzzle(puzzle: np.array):
    fig, ax = plt.subplots()
    for i in range(10):
        for j in range(10):
            c = puzzle[j, i]
            if c != 0:
                ax.text(i, j, str(c - 1), va='center', ha='center')
    ax.matshow(puzzle, cmap='Blues')
    plt.show()
