from tkinter import LEFT
from graphics import Window
from maze import Maze


def main():
    window_width = 800
    window_height = 600
    win = Window(width=window_width, height=600, bg="black", color="white")

    win.add_title("MazeQuest")

    frm = win.add_frame(
        height=100,
        width=window_width/2,
        padx=10,
        pady=10,
        pack_options={
            "side": LEFT
        }
    )
    frm2 = win.add_frame(
        height=100,
        width=window_width/2,
        padx=10,
        pady=10,
        pack_options={
            "side": LEFT
        }
    )

    margin = 25
    num_rows = 12
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
            "ipadx": 20,
            "ipady": 5,
        }
    )

    solve_bfs_btn = win.add_button(
        frm,
        "Solve with BFS algorithm",
        maze.solve_bfs,
        pack_options={
            "ipadx": 20,
            "ipady": 5,
        }
    )

    solve_a_star_btn = win.add_button(
        frm,
        "Solve with A* search algorithm",
        maze.solve_a_star,
        pack_options={
            "ipadx": 3,
            "ipady": 5,
        }
    )

    def create_new_maze():
        global maze
        win.clear_canvas()
        num_rows = int(rows_input.get())
        num_cols = int(cols_input.get())
        cell_size_x = (window_width - margin*2)//num_cols
        cell_size_y = (window_height - margin*2)//num_rows
        maze = Maze(
            margin, margin,
            num_rows, num_cols,
            cell_size_x, cell_size_y,
            win,
        )
        solve_btn.configure(command=maze.solve)
        solve_bfs_btn.configure(command=maze.solve_bfs)
        solve_a_star_btn.configure(command=maze.solve_a_star)

    rows_input, cols_input = win.add_size_input(
        frm2,
        pack_options={
            "padx": 5,
            "pady": 5,
        }
    )
    rows_input.insert(0, '12')
    cols_input.insert(0, '12')

    win.add_button(
        frm2,
        "New Maze",
        create_new_maze,
        fg="#333333",
        pack_options={
            "side": LEFT,
            "ipadx": 30,
            "ipady": 5,
        }
    )

    win.wait_for_close()


main()
