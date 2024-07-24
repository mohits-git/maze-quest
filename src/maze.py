from typing import List
from cell import Cell
from graphics import Window
from time import sleep
import random


class Maze:
    def __init__(
        self,
        x: int,
        y: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window | None = None,
        seed: int | None = None,
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
        self._break_entrance_and_exit()
        if seed is not None:
            random.seed(seed)
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(0, self._num_rows):
            self._cells.append([])
            for j in range(0, self._num_cols):
                self._cells[i].append(Cell(self._win))

        for i in range(0, self._num_rows):
            for j in range(0, self._num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int):
        if self._win is None:
            return
        x1 = self._x * (j+1)
        y1 = self._y * (i+1)
        x2 = self._x * (j+1) + self._cell_size_x
        y2 = self._y * (i+1) + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self._num_rows-1][self._num_cols-1].has_bottom_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(self._num_rows-1, self._num_cols-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            row = [-1, 0, 1, 0]
            col = [0, -1, 0, 1]
            possible_directions: List[List[int]] = []

            for k in range(0, 4):
                if (
                        row[k] + i >= 0
                        and row[k] + i < self._num_rows
                        and col[k] + j >= 0
                        and col[k] + j < self._num_cols
                        and not self._cells[row[k] + i][col[k] + j].visited
                ):
                    possible_directions.append([row[k]+i, col[k] + j])

            if len(possible_directions) == 0:
                self._draw_cell(i, j)
                return

            direction = possible_directions[int(
                random.random() * len(possible_directions)
            )]

            if direction[0] > i:
                self._cells[i][j].has_right_wall = False
                self._cells[direction[0]][j].has_left_wall = False
            elif direction[0] < i:
                self._cells[i][j].has_left_wall = False
                self._cells[direction[0]][j].has_right_wall = False
            elif direction[1] < j:
                self._cells[i][j].has_top_wall = False
                self._cells[i][direction[1]].has_bottom_wall = False
            elif direction[1] > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][direction[1]].has_top_wall = False

            self._break_walls_r(direction[0], direction[1])

    def _reset_cells_visited(self):
        for i in range(0, self._num_rows):
            for j in range(0, self._num_cols):
                self._cells[i][j].visited = False
