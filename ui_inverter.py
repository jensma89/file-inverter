import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk

class FileInverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("File Inverter")
        self.root.geometry("960x520")

        # Font
        self.font_size = 20
        self.font = tkfont.Font(size=self.font_size)
        self.root.option_add("*Font", self.font)

        # Call the method to create widgets
        self.create_widgets()

    def create_widgets(self):
        """Top frame for buttons."""
        top_frame = tk.Frame(self.root)
        top_frame.pack(fill="x", padx=10, pady=10)

        # Style for ttk buttons
        style = ttk.Style()
        style.configure("Grey.TButton",
                        foreground="white",
                        background="darkgrey",
                        borderwidth=4,
                        focusthickness=3,
                        focuscolor='none',
                        font=("Helvetica", self.font_size)
                        )

        # Left buttons
        left_buttons = tk.Frame(top_frame)
        left_buttons.pack(side="left", anchor="w")

        # Open Files button
        self.button_open = ttk.Button(left_buttons,
                                      text="Open Files",
                                      style="Grey.TButton",
                                      padding=(24,16))
        self.button_open.pack(side="left", padx=6)

        # Start Invert button
        self.button_start = ttk.Button(left_buttons,
                                       text="Start Invert",
                                       style="Grey.TButton",
                                       padding=(24,16))
        self.button_start.pack(side="left", padx=6)

        # Right buttons
        right_buttons = tk.Frame(top_frame)
        right_buttons.pack(side="right", anchor="e")

        # Save to... button
        self.button_save = ttk.Button(right_buttons,
                                      text="Save to...",
                                      style="Grey.TButton",
                                      padding=(24,16))
        self.button_save.pack(side="right", padx=6)


if __name__ == "__main__":
    root = tk.Tk()
    app = FileInverterGUI(root)
    root.mainloop()