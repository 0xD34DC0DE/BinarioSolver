import numpy as np


def solver(puzzle: np.array):
    changes = 0
    for i in range(10):
        for j in range(10):
            if puzzle[i, j] == 0:
                if i > 1:
                    if puzzle[i - 1, j] != 0:
                        if puzzle[i - 1, j] == puzzle[i - 2, j]:
                            puzzle[i, j] = 3 - puzzle[i - 1, j]
                            changes += 1
                if i < 8:
                    if puzzle[i + 1, j] != 0:
                        if puzzle[i + 1, j] == puzzle[i + 2, j]:
                            puzzle[i, j] = 3 - puzzle[i + 1, j]
                            changes += 1
                if j > 1:
                    if puzzle[i, j - 1] != 0:
                        if puzzle[i, j - 1] == puzzle[i, j - 2]:
                            puzzle[i, j] = 3 - puzzle[i, j - 1]
                            changes += 1
                if j < 8:
                    if puzzle[i, j + 1] != 0:
                        if puzzle[i, j + 1] == puzzle[i, j + 2]:
                            puzzle[i, j] = 3 - puzzle[i, j + 1]
                            changes += 1
                if 0 < i < 9:
                    if puzzle[i - 1, j] != 0:
                        if puzzle[i - 1, j] == puzzle[i + 1, j]:
                            puzzle[i, j] = 3 - puzzle[i - 1, j]
                            changes += 1
                if 0 < j < 9:
                    if puzzle[i, j - 1] != 0:
                        if puzzle[i, j - 1] == puzzle[i, j + 1]:
                            puzzle[i, j] = 3 - puzzle[i, j - 1]
                            changes += 1
    if changes == 0:
        # Horizontal i = row, j = column
        for i in range(10):
            zero_count = 0
            one_count = 0
            for j in range(10):
                if puzzle[i, j] == 1:
                    zero_count += 1
                elif puzzle[i, j] == 2:
                    one_count += 1
            if zero_count == 5:
                for j in range(10):
                    if puzzle[i, j] == 0:
                        puzzle[i, j] = 2
            if one_count == 5:
                for j in range(10):
                    if puzzle[i, j] == 0:
                        puzzle[i, j] = 1
        # Vertical j and i are inverted
        for i in range(10):
            zero_count = 0
            one_count = 0
            for j in range(10):
                if puzzle[j, i] == 1:
                    zero_count += 1
                elif puzzle[j, i] == 2:
                    one_count += 1
            if zero_count == 5:
                for j in range(10):
                    if puzzle[j, i] == 0:
                        puzzle[j, i] = 2
            if one_count == 5:
                for j in range(10):
                    if puzzle[j, i] == 0:
                        puzzle[j, i] = 1
