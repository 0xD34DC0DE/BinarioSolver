import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

images = []


def get_image(index: int):
    return images[index]


def get_global_images():
    global images
    return images

def process_plot_event():
    plt.pause(0)


def close_all_plots():
    plt.close()


def generate_puzzle_image(puzzle: np.array):
    global images
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

    images.append(fig2data(fig))


def fig2data(fig):
    """
    @brief Convert a Matplotlib figure to a 4D numpy array with RGBA channels and return it
    @param fig a matplotlib figure
    @return a numpy 3D array of RGBA values
    """
    # draw the renderer
    fig.canvas.draw()

    # Get the RGBA buffer from the figure
    w, h = fig.canvas.get_width_height()
    buf = np.fromstring(fig.canvas.tostring_argb(), dtype=np.uint8)
    buf.shape = (w, h, 4)
    # ARGB to BGRA
    buf = buf[:, :, [3, 2, 1, 0]]
    return buf