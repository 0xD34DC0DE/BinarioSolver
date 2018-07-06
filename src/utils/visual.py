import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import warnings


def show_puzzle(puzzle: np.array, display_now='yes'):
    plt.rcParams["figure.figsize"] = (2, 2)
    fig, ax = plt.subplots()

    for (i, j), z in np.ndenumerate(puzzle):
        if z != 0:
            ax.text(j, i, '{:0.0f}'.format(z - 1), ha='center', va='center')

    ax.matshow(puzzle, cmap='Paired')
    minor_ticks = [.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(minor_ticks, minor=True)
    ax.grid(which='minor', linewidth=1.1, color='k')

    # Set major ticks locations
    major_ticks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ax.xaxis.set_major_locator(ticker.FixedLocator(major_ticks))
    ax.yaxis.set_major_locator(ticker.FixedLocator(major_ticks))

    # Customize minor tick labels
    ax.xaxis.set_minor_locator(ticker.FixedLocator(minor_ticks))
    ax.yaxis.set_minor_locator(ticker.FixedLocator(minor_ticks))

    char_array = np.arange(10)

    # Strip the '.0' and convert to string representation of number
    char_array = [str(x) for x in char_array]

    # Set major axis labels
    ax.xaxis.set_major_formatter(ticker.FixedFormatter(char_array))
    ax.yaxis.set_major_formatter(ticker.FixedFormatter(char_array))



    if display_now == 'yes':
        plt.show()
    elif display_now != 'no':
        warnings.warn("display_now should be set to 'yes' or 'no' only", RuntimeWarning, stacklevel=2)
