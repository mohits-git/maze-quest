from tkinter import CENTER, Button, Frame, Label, Tk, Canvas
from typing import Callable


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
        self.__root.configure(background=bg)
        self.__canvas = Canvas(
            self.__root,
            width=width,
            height=height,
            bg=bg,
            highlightbackground=bg
        )
        self.__canvas.pack(
            fill="x",
            expand=1
        )
        self.__running = False
        self.__root.protocol('WM_DELETE_WINDOW', self.close)

    def clear_canvas(self):
        self.__canvas.delete("all")

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

    def write_text(self, x: int, y: int, text: str, **kwargs):
        self.__canvas.create_text(
            x,
            y,
            text=text,
            justify=CENTER,
            **kwargs,
        )

    def add_title(self, text):
        frm = self.add_frame(
            height=50,
            pady=10,
            pack_options={
                "before": self.__canvas
            }
        )
        label = Label(
            frm,
            text=text,
            font=("Sans-serif", 30, "bold"),
            justify=CENTER,
            bg=self.bg,
            highlightbackground=self.bg
        )
        label.pack(
            fill="x",
            expand=1
        )
        return label

    def add_frame(self, height: int, **kwargs):
        pack_options = kwargs.pop("pack_options", {})
        bg = kwargs.pop("bg") if "bg" in kwargs else self.bg
        frm = Frame(
            self.__root,
            height=height,
            bg=bg,
            **kwargs
        )
        frm.pack(
            fill="x",
            expand=1,
            **pack_options
        )
        return frm

    def add_button(self, parent, text: str, command: Callable, **kwargs):
        pack_options = kwargs.pop("pack_options", {})
        bg = kwargs.pop("bg") if "bg" in kwargs else self.bg
        btn = Button(
            parent,
            text=text,
            command=command,
            bg=bg,
            **kwargs
        )
        btn.pack(
            **pack_options
        )
        return btn
