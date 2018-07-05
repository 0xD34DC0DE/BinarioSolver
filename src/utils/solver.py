import numpy as np


def solver(puzzle: np.array):
    for i in range(10):
        for j in range(10):
            if puzzle[i, j] == 0:
                if i > 1:
                    if puzzle[i - 1, j] != 0:
                        if puzzle[i - 1, j]== puzzle[i - 2, j]:
                            puzzle[i, j] = 3 - puzzle[i - 1, j]
                if i < 8:
                    if puzzle[i + 1, j] != 0:
                        if puzzle[i + 1, j] == puzzle[i + 2, j]:
                            puzzle[i, j] = 3 - puzzle[i + 1, j]
                if j > 1:
                    if puzzle[i, j - 1] != 0:
                        if puzzle[i, j - 1] == puzzle[i, j - 2]:
                            puzzle[i, j] = 3 - puzzle[i, j - 1]
                if j < 8:
                    if puzzle[i, j + 1] != 0:
                        if puzzle[i, j + 1] == puzzle[i, j + 2]:
                            puzzle[i, j] = 3 - puzzle[i, j + 1]

