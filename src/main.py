from cell import Cell
from graphics import Window


def main():
    win = Window(width=800, height=600)

    cell1 = Cell(win)
    cell2 = Cell(win)
    cell2.has_left_wall = False
    cell3 = Cell(win)
    cell3.has_left_wall = False
    cell3.has_top_wall = False
    cell4 = Cell(win)
    cell4.has_left_wall = False
    cell4.has_top_wall = False
    cell4.has_right_wall = False
    cell5 = Cell(win)
    cell5.has_bottom_wall = False
    cell5.has_top_wall = False
    cell5.has_right_wall = False

    cell1.draw(50, 50, 100, 100)
    cell2.draw(150, 50, 200, 100)
    cell3.draw(250, 50, 300, 100)
    cell4.draw(350, 50, 400, 100)
    cell5.draw(450, 50, 500, 100)

    win.wait_for_close()


main()
