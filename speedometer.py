from WCK import Widget, FONT, FOREGROUND

import cmath, math

def rotate(xy, angle, center):
    # rotate the xy coordinate around the given center.  all coordinates
    # are given as complex numbers, angles in degrees.  for some background,
    # see <http://online.effbot.org/2004_09_01_archive.htm#tkinter-complex>
    return cmath.exp(angle*math.pi/-180j) * (xy - center) + center

def flatten(data):
    # flatten a list of complex numbers into a [real, imag, ...] int sequence
    xy = []
    for x in data:
        xy.append(int(x.real + 0.5))
        xy.append(int(x.imag + 0.5))
    return xy

class Gauge(Widget):
    # widget implementation

    ui_option_foreground = FOREGROUND

    ui_option_width = 200
    ui_option_height = 200

    ui_option_font = FONT

    ui_option_value = 0 # valid values are 0..100

    ui_option_min_label = "min"
    ui_option_max_label = "max"

    ui_doublebuffer = 1

    def ui_handle_config(self):
        return int(self.ui_option_width), int(self.ui_option_height)

    def ui_handle_resize(self, width, height):
        self.size = width, height # current width

    def ui_handle_repair(self, draw, x0, y0, x1, y1):

        width, height = self.size

        # use complex numbers as coordinates
        center = complex(width/2, height*0.8)
        scale = complex(width/2, height*0.2)

        # map input data value to angle
        def value2angle(i):
            return (i-50) * 0.8

        # draw scale
        xy = []
        for i in range(0, 100+1, 2):
            xy.append(rotate(scale, value2angle(i), center))
        xy = flatten(xy)
        draw.line(xy, self.ui_pen(self.ui_option_foreground, 1))

        # draw min/max labels
        font = self.ui_font(self.ui_option_foreground, self.ui_option_font)
        x, y = xy[:2]
        w, h = draw.textsize(self.ui_option_min_label, font)
        draw.text((x - w/2, y), self.ui_option_min_label, font)
        x, y = xy[-2:]
        w, h = draw.textsize(self.ui_option_max_label, font)
        draw.text((x - w/2, y), self.ui_option_max_label, font)

        # draw indicator
        value = value2angle(float(self.ui_option_value))
        xy = flatten((center, rotate(scale, value, center)))
        draw.line(xy, self.ui_pen(self.ui_option_foreground, 5))

if __name__ == "__main__":

    import Tkinter

    root = Tkinter.Tk()
    root.title("demoGauge")

    widget = Gauge(root)
    widget.pack(fill="both", expand=1)

    for i in range(0, 100):
        widget.update()
        widget.config(value=i)
        widget.after(10)

    root.mainloop()
