from cell import Cell
from graphics import Window


def main():
    win = Window(width=800, height=600)

    cell1 = Cell(win)
    cell1.has_left_wall = False
    cell2 = Cell(win)
    cell3 = Cell(win)
    cell4 = Cell(win)
    cell5 = Cell(win)
    cell5.has_bottom_wall = False

    cell1.draw(50, 50, 100, 100)
    cell2.draw(150, 50, 200, 100)
    cell3.draw(250, 50, 300, 100)
    cell4.draw(350, 50, 400, 100)
    cell5.draw(250, 150, 300, 200)

    cell1.draw_move(cell2)
    cell2.draw_move(cell3)
    cell4.draw_move(cell3, undo=True)
    cell3.draw_move(cell5)

    win.wait_for_close()


main()
