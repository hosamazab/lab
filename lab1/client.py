
from socket import *
def split_message(message):
    max_chunk_size = 2048
    chunks = []
    for i in range(0, len(message), max_chunk_size):
        chunks.append(message[i:i + max_chunk_size])
    return chunks

try:
    s=socket(AF_INET, SOCK_STREAM)
    host="127.0.0.1"
    port=7002
    s.connect((host,port))
    while True:
        y=input("client : ")
        s.send(y.encode('utf-8'))
        x=s.recv(2048) 
        z=len(x.encode('utf-8'))
        if z>2048:
            message_chunks = split_message(x)
            for chunk in message_chunks:
                print("server : ",chunk.decode('utf-8'))
        else: 
            print("server : ",x.decode('utf-8'))
    s.close()
except error as e:
    print(e)
except KeyboardInterrupt :
    print("chat is terminated")