from socket import *
import threading

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
username = 'USER'


def receive():
    while True:
        try:
            message = clientSocket.recv(1024).decode()
            if message == 'USER':
                clientSocket.send(username.encode())
            else:
                print(message)
        except:
            print("An error occured!")
            clientSocket.close()
            break


def wait_for_input():
    while True:
        message = f'{username}: {input("")}'
        clientSocket.send(message.encode())


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=wait_for_input)
write_thread.start()