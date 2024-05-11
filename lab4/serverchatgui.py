import socket
import threading

# Function to handle client connections
def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received from {address}: {data.decode('utf-8')}")

        # Broadcast the received message to all other clients
        for other_client_socket in client_sockets:
            if other_client_socket != client_socket:
                try:
                    other_client_socket.send(data)
                except Exception as e:
                    print(f"Error sending message to client: {e}")

    print(f"Connection from {address} closed.")
    client_sockets.remove(client_socket)
    client_socket.close()

# Function to start the server
def start_server():
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5555))
    server_socket.listen(5)
    print("Server listening on port 5555...")

    while True:
        client_socket, address = server_socket.accept()
        client_sockets.append(client_socket)
        client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
        client_handler.start()

# List to store client sockets
client_sockets = []

# Start the server
start_server()
