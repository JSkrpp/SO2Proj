import tkinter as tk
from tkinter import scrolledtext
from client import Client

class Interface:
    def __init__(self, nickname):
        self.window = tk.Toplevel()
        self.window.title(f'Chat: {nickname}')
        self.window.geometry('720x480')

        self.client = Client('127.0.0.1', 7632, self.display_message, nickname)

        self.chat_area = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, state='disabled')
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.entry_message = tk.Entry(self.window)
        self.entry_message.pack(padx=10, pady=5, fill=tk.X)
        self.entry_message.bind('<Return>', self.send_message)

        self.send_button = tk.Button(self.window, text="Wyślij", command=self.send_message)
        self.send_button.pack(pady=5)

        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

    def send_message(self, event=None):
        message = self.entry_message.get().strip()
        if message:
            if message.lower() == "bye":
                self.client.send_message(message)
                self.on_close()
                return
            self.client.send_message(message)
            self.entry_message.delete(0, tk.END)

    def display_message(self, message):
        print("GUI DEBUG: Wyświetlanie:", message)
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

    def on_close(self):
        self.client.disconnect()
        self.window.destroy()