from socket import *
import threading
import os
import sys
from connection import set_connection
from colors import print_color, format_string

CLIENT_SOCKET = socket(AF_INET, SOCK_STREAM)
SERVER_IP = ''
SERVER_PORT = 0


def receive():
    while True:
        try:
            message = CLIENT_SOCKET.recv(1024).decode('ascii')
            if message == 'USER':
                CLIENT_SOCKET.send(USERNAME.encode())
            else:
                print(message)
        except:
            print_color('An error occurred!', 'red')


def wait_for_input():
    while True:
        message = f'{USERNAME}: {input("")}'
        CLIENT_SOCKET.send(message.encode())


print("  _______ _____ _____     _____ _ _            _    \n"
      " |__   __/ ____|  __ \   / ____| (_)          | |   \n"
      "    | | | |    | |__) | | |    | |_  ___ _ __ | |_  \n"
      "    | | | |    |  ___/  | |    | | |/ _ \ '_ \| __| \n"
      "    | | | |____| |      | |____| | |  __/ | | | |_  \n"
      "    |_|  \_____|_|       \_____|_|_|\___|_| |_|\__| \n"
      )
input("PRESS ENTER TO START")
os.system('cls')

if 'default' in sys.argv:
    SERVER_IP = 'localhost'
    SERVER_PORT = 12000
else:
    SERVER_IP, SERVER_PORT = set_connection()

print_color(f'\nOpening server...', 'yellow')

try:
    CLIENT_SOCKET.connect((SERVER_IP, SERVER_PORT))
except OSError as e:
    print(f'\n{e}', 'red')
    exit(-1)

os.system('cls')

USERNAME = input('USERNAME: ')
USERNAME = format_string(USERNAME, 'random')

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=wait_for_input)
write_thread.start()
