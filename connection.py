import re
from colors import print_color, format_string


def set_connection():
    ip = ''
    port = 0

    while True:
        input_server = input(f'\nSERVER IP [press enter to use default]: ')
        if input_server == 'localhost':
            ip = input_server
            break
        elif input_server != '':
            verify = re.fullmatch(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', input_server)
            if verify is None:
                print_color('\nERROR: INVALID SERVER IP', 'red')
                continue
            else:
                ip = input_server
                print_color(f'\nUSING IP {ip}...', 'yellow')
                break
        else:
            ip = 'localhost'
            print_color(f'\nUSING IP {ip}...', 'yellow')
            break

    while True:
        input_port = input('\nPORT [press enter to use default]: ')
        if input_port != '':
            verify = re.fullmatch(r'^\d*$', input_port)
            if verify is None:
                print_color(f'\nERROR: INVALID PORT NUMBER', 'red')
                continue
            else:
                port = int(input_port)
                print_color(f'\nUSING PORT {port}...', 'yellow')
                break
        else:
            port = 12000
            print_color(f'\nUSING PORT {port}...', 'yellow')
            break
    return [ip, port]
