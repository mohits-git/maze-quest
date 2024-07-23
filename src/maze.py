from typing import List
from cell import Cell
from graphics import Window
from time import sleep


class Maze:
    def __init__(
        self,
        win: Window,
        x: int,
        y: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
    ):
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells: List[List[Cell]] = []
        self._create_cells()

    def _create_cells(self):
        for i in range(0, self._num_rows):
            self._cells.append([])
            for j in range(0, self._num_cols):
                self._cells[i].append(Cell(self._win))

        for i in range(0, self._num_rows):
            for j in range(0, self._num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int):
        x1 = self._x * (j+1)
        y1 = self._y * (i+1)
        x2 = self._x * (j+1) + self._cell_size_x
        y2 = self._y * (i+1) + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        sleep(0.05)
