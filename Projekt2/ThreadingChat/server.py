import socket
from threading import Thread, Lock

class Server:
    Clients = []
    lock = Lock()

    def __init__(self, HOST, PORT):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((HOST, PORT))
        self.socket.listen(5)
        print('Serwer czeka na połączenie')

    def listen(self):
        while True:
            client_socket, address = self.socket.accept()
            print("Connection from" + str(address))

            client_name = client_socket.recv(1024).decode()
            client = {'client_name': client_name, 'client_socket': client_socket}

            self.broadcast_message(client_name, client_name + " dolaczyl do czatu")

            with self.lock:
                Server.Clients.append(client)

            Thread(target=self.handle_new_client, args=(client,)).start()

    def handle_new_client(self, client):
        client_name = client['client_name']
        client_socket = client['client_socket']
        try:
            while True:
                client_message = client_socket.recv(1024).decode()

                if client_message.lower().strip().endswith("bye") or not client_message.strip():
                    self.broadcast_message(client_name, f"{client_name} opuścił czat")
                    break
                else:
                    self.broadcast_message(client_name, client_message)
        except (ConnectionResetError, ConnectionAbortedError):
            self.broadcast_message(client_name, client_name + " rozłączony (awaria)")
        finally:
            with self.lock:
                if client in Server.Clients:
                    Server.Clients.remove(client)
                client_socket.close()

    def broadcast_message(self, sender_name, message):
        with self.lock:
            for client in self.Clients:
                try:
                    client_socket = client['client_socket']
                    client_socket.send(message.encode())
                except Exception as e:
                    print("SERVER BŁĄD:", e)

if __name__ == '__main__':
    server = Server('127.0.0.1', 7632)
    server.listen()
