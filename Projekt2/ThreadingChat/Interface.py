import tkinter as tk
class Interface:
    def __init__(self):
        window = tk.Tk()
        window.title('Chat app with threading')
        height = 720
        width = 1280
        window.geometry(f"{width}x{height}")
        window.mainloop()