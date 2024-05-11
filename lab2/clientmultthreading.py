import socket
import threading

def receive_messages(client_socket):
    while True:
        response = client_socket.recv(2048)
        if not response:
            break
        print("Received:", response.decode("utf-8"))

def send_messages(client_socket):
    while True:
        message = input()
        if message.lower() == 'exit':
            break
        client_socket.sendall(message.encode("utf-8"))

def main():
    server_address = ('localhost', 8888)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))

    receive_thread.start()
    send_thread.start()

    receive_thread.join()
    send_thread.join()

    client_socket.close()

if __name__ == "__main__":
    main()
