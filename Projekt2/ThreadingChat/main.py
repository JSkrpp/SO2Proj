import tkinter as tk
from Interface import Interface

MAX_WINDOWS = 4
active_windows = []  # Lista referencji do otwartych okien

def open_chat_window(nick, launcher_window, join_button):
    def on_window_close():
        active_windows.remove(chat_window)
        chat_window.window.destroy()
        print(f"[INFO] Zamknięto okno czatu dla: {nick}")
        if len(active_windows) < MAX_WINDOWS:
            join_button.config(state=tk.NORMAL)

    chat_window = Interface(nick)
    chat_window.window.protocol("WM_DELETE_WINDOW", on_window_close)
    active_windows.append(chat_window)

    if len(active_windows) >= MAX_WINDOWS:
        join_button.config(state=tk.DISABLED)


def launch_main():
    root = tk.Tk()
    root.title("Chat Launcher")
    root.geometry("300x150")

    tk.Label(root, text="Wpisz swój nick:").pack(pady=10)
    nick_entry = tk.Entry(root)
    nick_entry.pack(pady=5)
    nick_entry.focus()

    def on_join():
        nick = nick_entry.get().strip()
        if nick:
            open_chat_window(nick, root, join_button)
            root.withdraw()


    join_button = tk.Button(root, text="Dołącz do czatu", command=on_join)
    join_button.pack(pady=10)

    root.mainloop()


if __name__ == '__main__':
    launch_main()
