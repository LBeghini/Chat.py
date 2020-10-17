from socket import *
import threading

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen()

clients = list()
usernames = list()


def reply(message, sender=None):
    for client in clients:
        if client == sender:
            continue
        client.send(message)


def handle(client):
    while 1:
        try:
            message = client.recv(1024)
            reply(message, client)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            user = usernames[index]
            reply(f'{user} left!'.encode())
            usernames.remove(user)
            break


def receive():
    while 1:
        connectionSocket, addr = serverSocket.accept()
        print(f"Connected with {addr}")

        connectionSocket.send('USER'.encode())
        user = connectionSocket.recv(1024).decode()
        usernames.append(user)
        clients.append(connectionSocket)

        reply(f'{user} joined'.encode())
        connectionSocket.send('Connected to server!'.encode())

        client_thread = threading.Thread(target=handle, args=(connectionSocket,))
        client_thread.start()


print("Ready to receive...")
receive()
