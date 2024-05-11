import tkinter as tk
import socket
import threading

def send_message():
    message = message_entry.get()
    client_socket.send(message.encode('utf-8'))

def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024)
            if data:
                chat_log.insert(tk.END, f"Server: {data.decode('utf-8')}\n")
        except Exception as e:
            print(f"Error receiving message from server: {e}")
            break

def close_connection():
    client_socket.close()
    root.quit()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5555))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

root = tk.Tk()
root.title("Client")

chat_log = tk.Text(root, width=40, height=10)
chat_log.pack(pady=10)

message_entry = tk.Entry(root, width=30)
message_entry.pack(pady=5)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

close_button = tk.Button(root, text="Close Connection", command=close_connection)
close_button.pack(pady=5)

root.mainloop()
