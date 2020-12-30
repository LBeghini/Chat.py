from socket import *
import threading
import re
import os
import sys

COLOR = {
    "PURPLE": '\033[95m',
    "CYAN": '\033[96m',
    "DARKCYAN": '\033[36m',
    "BLUE": '\033[94m',
    "GREEN": '\033[92m',
    "YELLOW": '\033[93m',
    "RED": '\033[91m',
    "BOLD": '\033[1m',
    "UNDERLINE": '\033[4m',
    "END": '\033[0m'
}

SERVER_SOCKET = socket(AF_INET, SOCK_STREAM)
SERVER_IP = ''
SERVER_PORT = 0

CLIENTS = list()
ADDRESSES = list()
USERS = list()


os.system('cls')


def set_connection():
    global SERVER_IP
    global SERVER_PORT
    global SERVER_SOCKET

    while True:
        input_server = input(f'\nSERVER IP [press enter to use default]: ')
        if input_server == 'localhost':
            SERVER_IP = input_server
            break
        elif input_server != '':
            verify = re.fullmatch(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', input_server)
            if verify is None:
                print(f'{COLOR["RED"]}\nERROR: INVALID SERVER IP{COLOR["END"]}')
                continue
            else:
                SERVER_IP = input_server
                print(f'{COLOR["YELLOW"]}\nUSING IP {SERVER_IP}...{COLOR["END"]}')
                break
        else:
            SERVER_IP = 'localhost'
            print(f'{COLOR["YELLOW"]}\nUSING IP {SERVER_IP}...{COLOR["END"]}')
            break

    while True:
        input_port = input(f'\nPORT [press enter to use default]: ')
        if input_port != '':
            verify = re.fullmatch(r'^\d*$', input_port)
            if verify is None:
                print(f'{COLOR["RED"]}\nERROR: INVALID PORT NUMBER{COLOR["END"]}')
                continue
            else:
                SERVER_PORT = int(input_port)
                print(f'{COLOR["YELLOW"]}\nUSING PORT {SERVER_PORT}...{COLOR["END"]}')
                break
        else:
            SERVER_PORT = 12000
            print(f'{COLOR["YELLOW"]}\nUSING PORT {SERVER_PORT}...{COLOR["END"]}')
            break


def print_connections():
    os.system('cls')
    print(f'{COLOR["GREEN"]}\nReady to receive at {SERVER_IP}:{SERVER_PORT}\n{COLOR["END"]}')
    if len(ADDRESSES) > 0:
        print(f'{COLOR["GREEN"]}\nCONNECTIONS: \n{COLOR["END"]}')
    for address in ADDRESSES:
        print(f'{COLOR["CYAN"]}\tConnected with {address}{COLOR["END"]}')


def broadcast(message, sender=None):
    for client in CLIENTS:
        if client == sender:
            continue
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            index = CLIENTS.index(client)
            CLIENTS.remove(client)
            client.close()
            user = USERS[index]
            broadcast(f'{COLOR["RED"]}{user} left!{COLOR["END"]}'.encode())
            USERS.remove(user)
            del ADDRESSES[index]
            print_connections()
            break


def receive():
    while True:
        connection_socket, addr = SERVER_SOCKET.accept()

        connection_socket.send('USER'.encode())
        user = connection_socket.recv(1024).decode()

        USERS.append(user)
        CLIENTS.append(connection_socket)
        ADDRESSES.append(addr)

        print_connections()

        broadcast(f'{user} joined'.encode(), sender=connection_socket)
        connection_socket.send(f'{COLOR["GREEN"]}Connected to server!{COLOR["END"]}'.encode())

        client_thread = threading.Thread(target=handle, args=(connection_socket,))
        client_thread.start()


print("  _______ _____ _____     _____                           \n"
      " |__   __/ ____|  __ \   / ____|                          \n"
      "    | | | |    | |__) | | (___   ___ _ ____   _____ _ __  \n"
      "    | | | |    |  ___/   \___ \ / _ \ '__\ \ / / _ \ '__| \n"
      "    | | | |____| |       ____) |  __/ |   \ V /  __/ |    \n"
      "    |_|  \_____|_|      |_____/ \___|_|    \_/ \___|_|    \n"
      )
input("PRESS ENTER TO START")
os.system('cls')

if 'default' in sys.argv:
    SERVER_IP = 'localhost'
    SERVER_PORT = 12000
else:
    set_connection()

print(f'{COLOR["YELLOW"]}\nOpening server...{COLOR["END"]}')

try:
    SERVER_SOCKET.bind((SERVER_IP, SERVER_PORT))
except OSError as e:
    print(f'{COLOR["RED"]}\n{e}{COLOR["END"]}')
    exit(-1)

SERVER_SOCKET.listen()

print(f'{COLOR["GREEN"]}\nReady to receive at {SERVER_IP}:{SERVER_PORT}\n{COLOR["END"]}')

receive()
