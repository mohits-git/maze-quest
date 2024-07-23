from graphics import Line, Point, Window


def main():
    p1 = Point(20, 300)
    p2 = Point(780, 300)
    line = Line(p1, p2)
    win = Window(width=800, height=600)
    win.draw_line(line)
    win.wait_for_close()


main()
