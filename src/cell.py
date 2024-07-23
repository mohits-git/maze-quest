from graphics import Line, Point, Window


class Cell:
    def __init__(
            self,
            win: Window,
    ):
        self._win = win
        self.has_bottom_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_left_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None

    def draw(
            self,
            x1: int, y1: int,
            x2: int, y2: int,
    ):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            lw = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(lw)
        if self.has_right_wall:
            rw = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(rw)
        if self.has_top_wall:
            tw = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(tw)
        if self.has_bottom_wall:
            tw = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(tw)
