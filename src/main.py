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

    margin = 25
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

    solve_btn = win.add_button(
        frm,
        "Solve with DFS algorithm",
        maze.solve,
        pack_options={
            "ipadx": 10,
            "ipady": 5,
        }
    )

    def create_new_maze():
        global maze
        win.clear_canvas()
        maze = Maze(
            margin, margin,
            num_rows, num_cols,
            cell_size_x, cell_size_y,
            win,
        )
        solve_btn.configure(command=maze.solve)

    win.add_button(
        frm,
        "Next Maze",
        create_new_maze,
        pack_options={
            "ipadx": 10,
            "ipady": 5,
        }
    )

    win.wait_for_close()


main()
