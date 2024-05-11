import socket
import threading

# Global list to store client sockets
client_sockets = []

def handle_client(client_socket, address):
    global client_sockets

    print(f"Accepted connection from {address}")
    client_sockets.append(client_socket)

    try:
        while True:
            data = client_socket.recv(2048)
            if not data:
                break
            message = data.decode("utf-8")
            print(f"Received message from {address}: {message}")

            # Broadcast the message to all other clients
            for client in client_sockets:
                if client != client_socket:
                    client.sendall(data)
    except ConnectionResetError:
        pass
    finally:
        print(f"Connection from {address} closed")
        client_sockets.remove(client_socket)
        client_socket.close()

def main():
    server_address = ('localhost', 8888)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(5)

    print("Server is listening for connections...")

    while True:
        client_socket, address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
        client_handler.start()

if __name__ == "__main__":
    main()
