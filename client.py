from socket import *
import threading
import re
import random
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

USER_COLORS = {
    "PURPLE": '\033[95m',
    "CYAN": '\033[96m',
    "DARKCYAN": '\033[36m',
    "BLUE": '\033[94m'
}

CLIENT_SOCKET = socket(AF_INET, SOCK_STREAM)
SERVER_IP = ''
SERVER_PORT = 0


def set_connection():
    global SERVER_IP
    global SERVER_PORT

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


def receive():
    while True:
        try:
            message = CLIENT_SOCKET.recv(1024).decode('ascii')
            if message == 'USER':
                CLIENT_SOCKET.send(USERNAME.encode())
            else:
                print(message)
        except:
            print(f'{COLOR["RED"]}An error occured!{COLOR["END"]}')


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
    set_connection()

print(f'{COLOR["YELLOW"]}\nOpening server...{COLOR["END"]}')

try:
    CLIENT_SOCKET.connect((SERVER_IP, SERVER_PORT))
except OSError as e:
    print(f'{COLOR["RED"]}\n{e}{COLOR["END"]}')
    exit(-1)

os.system('cls')

USERNAME = input('USERNAME: ')
print(random.choice(list(COLOR.values())))
USERNAME = f'{USER_COLORS[random.choice(list(USER_COLORS.keys()))]}{USERNAME}{COLOR["END"]}'

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=wait_for_input)
write_thread.start()
