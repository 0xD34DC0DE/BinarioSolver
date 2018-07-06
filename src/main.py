from utils import *

if __name__ == '__main__':

    async_webcam = VideoCaptureAsync()
    async_webcam.start()

    filename = 'data/puzzle.txt'

    file1 = load_puzzle(filename)
    puzzle = decode_file(file1)

    generate_puzzle_image(puzzle)
    solver(puzzle)
    generate_puzzle_image(puzzle)
    solver(puzzle)
    generate_puzzle_image(puzzle)
    solver(puzzle)
    generate_puzzle_image(puzzle)
    solver(puzzle)
    generate_puzzle_image(puzzle)
    solver(puzzle)
    generate_puzzle_image(puzzle)

    show_all_images()
    while not key_pressed('q'):
        pass

    # Tell the webcam thread to stop
    async_webcam.stop()
    close_all_plots()
    close_all_images()

    print(puzzle)
