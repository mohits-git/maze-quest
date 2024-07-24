from graphics import Window
from maze import Maze


def main():
    window_width = 800
    window_height = 600
    win = Window(width=window_width, height=600, bg="black", color="white")

    margin = 50
    num_rows = 10
    num_cols = 12
    cell_size_x = (window_width - margin*2)//num_cols
    cell_size_y = (window_height - margin*2)//num_rows

    maze = Maze(
        margin, margin,
        num_rows, num_cols,
        cell_size_x, cell_size_y,
        win,
    )

    maze.solve()

    win.wait_for_close()


main()
