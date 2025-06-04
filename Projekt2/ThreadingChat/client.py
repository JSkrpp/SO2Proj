import socket
from threading import Thread
import time

class Client:

    def __init__(self, HOST, PORT, display_callback=None, name="Anonim"):
        # inicjalizacja socketu klienta
        self.socket = socket.socket()
        self.socket.connect((HOST, PORT))
        self.name = name
        self.socket.send(self.name.encode())
        self.display_callback = display_callback
        self.running = True
        Thread(target=self.receive_message, daemon=True).start() # initializing a thread for the client


    def send_message(self, message):
        full_message = self.name + ": " + message
        self.socket.send(full_message.encode())

    def receive_message(self):
        while self.running:
            try: # try catch block for recieving messages
                server_message = self.socket.recv(1024).decode()
                print("DEBUG: Otrzymano:", server_message)
                if server_message.strip() and self.display_callback:
                    self.display_callback(server_message)
            except:
                break

    def disconnect(self):
        try:
            # typing "bye" allows to leave chat
            full_message = self.name + ": bye"
            self.socket.send(full_message.encode())
            time.sleep(0.3)
        except Exception as e:
            print("DEBUG Błąd przy wysyłaniu bye:", e)
        self.running = False
        try:
            self.socket.close()
        except:
            pass

