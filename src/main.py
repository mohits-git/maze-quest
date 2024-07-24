from tkinter import Button
from graphics import Window
from maze import Maze


def main():
    window_width = 800
    window_height = 600
    win = Window(width=window_width, height=600, bg="black", color="white")

    win.add_title("MazeQuest")

    frm = win.add_frame(
        height=100,
        width=window_width,
        padx=10,
        pady=10
    )

    margin = 50
    num_rows = 10
    num_cols = 12
    cell_size_x = (window_width - margin*2)//num_cols
    cell_size_y = (window_height - margin)//num_rows

    maze = Maze(
        margin, margin,
        num_rows, num_cols,
        cell_size_x, cell_size_y,
        win,
    )

    win.add_button(
        frm,
        "Solve with DFS algorithm",
        maze.solve,
        pack_options={
            "pady": 10,
            "ipadx": 10,
            "ipady": 5,
        }
    )

    win.wait_for_close()


main()
