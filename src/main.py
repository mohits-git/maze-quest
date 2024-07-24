from graphics import Window
from maze import Maze


def main():
    win = Window(width=800, height=600)

    Maze(
        x=50, y=50,
        num_rows=10, num_cols=12,
        cell_size_x=50, cell_size_y=50,
        win=win,
        seed=0
    )

    win.wait_for_close()


main()
