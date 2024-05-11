import socket
import threading

def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")

    def receive_messages():
        while True:
            data = client_socket.recv(2048)
            if not data:
                break
            message = data.decode("utf-8")
            print(f"Received message from {address}: {message}")

    def send_messages():
        while True:
            message = input()
            if message.lower() == 'exit':
                client_socket.close()
                break
            client_socket.sendall(message.encode("utf-8"))

    receive_thread = threading.Thread(target=receive_messages)
    send_thread = threading.Thread(target=send_messages)

    receive_thread.start()
    send_thread.start()

    receive_thread.join()
    send_thread.join()

    print(f"Connection from {address} closed")

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
