import curses

class Termbud:
    def __init__(self):
        scr = curses.initscr()

    def __str__(self):
        pass

    def generate(self=None, blink=False, pet=False, bigEyes=False, blushing=False, squinting=False):
        if not bigEyes:
            eye = "o"
        else:
            eye = "O"
        if blink:
            eye = "-"
        if squinting:
            eye = "^"

        if not blushing:
            blush = " "
        else:
            blush = "*"
        mouth = "w"
        output = ""
        output += f"┌─────────────────────┐\n"
        output += f"│                     │\n"
        output += f"│        {blush}{eye}{mouth}{eye}{blush}        │\n"
        output += f"│                     │\n"
        output += f"└─────────────────────┘\n"
        return output

if __name__ == "__main__":
    print(Termbud.generate())
    print(Termbud.generate(squinting=True))
    print(Termbud.generate(blushing=True))
    import pdb; pdb.set_trace()