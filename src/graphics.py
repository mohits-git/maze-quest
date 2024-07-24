from tkinter import BOTH, Tk, Canvas


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, fill_color: str = "black"):
        canvas.create_line(
            self.p1.x, self.p1.y,
            self.p2.x, self.p2.y,
            fill=fill_color,
            width=2
        )


class Window:
    def __init__(self, width: int, height: int, bg="#333332", color="black"):
        self.bg = bg
        self.color = color
        self.__root = Tk()
        self.__root.title("MazeQuest")
        self.__canvas = Canvas(
            self.__root,
            width=width,
            height=height,
            bg=bg
        )
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol('WM_DELETE_WINDOW', self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Closed")

    def close(self):
        self.__running = False

    def draw_line(self, line: Line, fill_color: str | None = None):
        color = self.color if fill_color is None else fill_color
        line.draw(self.__canvas, color)
