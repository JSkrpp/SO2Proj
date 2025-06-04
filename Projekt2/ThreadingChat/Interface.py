import tkinter as tk
from tkinter import scrolledtext
from client import Client
from datetime import datetime


class Interface:
    def __init__(self, nickname):
        # initialize user interface
        self.window = tk.Toplevel()
        self.window.title(f'Chat: {nickname}')
        self.window.geometry('720x480')

        self.client = Client('127.0.0.1', 7632, self.display_message, nickname)
        self.client.nickname = nickname

        self.chat_area = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, state='disabled')
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.entry_message = tk.Entry(self.window)
        self.entry_message.pack(padx=10, pady=5, fill=tk.X)
        self.entry_message.bind('<Return>', self.send_message)

        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=5)

        self.send_button = tk.Button(button_frame, text="Wyślij", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(button_frame, text="Wyczyść czat", command=self.clear_chat)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        self.setup_chat_tags()

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
        # split the message into name and content
        try:
            name, msg_content = message.split(":", 1)
        except ValueError:
            # catching wrong message formats, shouldn't happen
            self.chat_area.config(state='normal')
            self.chat_area.insert(tk.END, f"{message}\n", 'error')
            self.chat_area.config(state='disabled')
            self.chat_area.yview(tk.END)
            return

        print("GUI DEBUG: Displaying:", message)

        self.chat_area.config(state='normal')

        # Determine if the message is sent or received
        if name.strip() == self.client.nickname:  # Check against the client's nickname
            tag = 'sent'
        else:
            tag = 'received'

        current_time = datetime.now().strftime("%H:%M:%S")

        self.chat_area.insert(tk.END, f"[{current_time}] {name.strip()}: ", tag)
        self.chat_area.insert(tk.END, f"{msg_content.strip()}\n")

        # Lock the text widget again
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

    def setup_chat_tags(self):
        # styles for sent and recieved messages
        self.chat_area.tag_configure('sent', foreground='blue', font=('Arial', 10, 'bold'))
        self.chat_area.tag_configure('received', foreground='green', font=('Arial', 10, 'bold'))
        self.chat_area.tag_configure('error', foreground='red', font=('Arial', 10, 'italic'))

    def on_close(self):
        self.client.disconnect()
        self.window.destroy()

    def clear_chat(self):
        self.chat_area.config(state='normal')
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.config(state='disabled')
