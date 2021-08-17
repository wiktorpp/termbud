import curses
import random

class Termbud:
    def __init__(self):
        global scr
        scr = curses.initscr()
        curses.noecho()
        self.position = 9
        self.time = 0
        self.health = 1.0

    def __str__(self):
        pass

    def generate(self=None, blush=" ", eye="o", mouth="w", pet=False):

        self.print_box()
        self.update()

        if pet:
            scr.addstr(1, self.position, "  _/ ")
        bud = f"{blush}{eye}{mouth}{eye}{blush}"

        scr.addstr(2, self.position, bud)

    def update(self):
        if self.time % 5 == 0:
            self.position = self.position + random.randint(-1, 1)
            if self.position <= 1:
                self.position = 2
            if self.position >= 17:
                self.position = 16
        self.time += 1

    def print_box(self):
        scr.addstr(0, 0, "┌─────────────────────┐")
        scr.addstr(1, 0, "│                     │")
        scr.addstr(2, 0, "│                     │")
        scr.addstr(3, 0, "│                     │")
        scr.addstr(4, 0, "│                     │")
        scr.addstr(5, 0, "└─────────────────────┘")

if __name__ == "__main__":
    """
    t = Termbud()
    t.print_box()
    t.generate(eye="^")
    scr.getkey()
    t.generate(blush="*")
    scr.getkey()
    t.generate(pet=True, eye="O", blush="*")
    scr.getkey()
    """
    t = Termbud()
    pet_level = 0
    t.generate()
    while True:
        button = scr.getkey()
        scr.addstr(0, 0, repr(button))
        if button == "q" or button == "\x1b":
            exit()
        else:
            pet_level += 1
        if pet_level == 0:
            t.generate()
        elif pet_level == 1:
            t.generate(pet=True, eye="^")
        elif pet_level == 5:
            t.generate(pet=True, eye="O", blush="*")