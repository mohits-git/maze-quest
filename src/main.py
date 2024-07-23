from graphics import Window
from maze import Maze


def main():
    win = Window(width=800, height=600)

    Maze(win, 50, 50, 6, 6, 50, 50)

    win.wait_for_close()


main()
