"""main.py
operate the start

"""
from tkinter import Tk
from inverter_ui import FileInverterGUI

if __name__ == "__main__":
    root = Tk()
    app = FileInverterGUI(root)
    root.mainloop()
