# :speech_balloon: Chat.py

## About

Chat.py is a simple program developed for an assignment of a Computer Networks class. It implements the usage of TCP to send messages between Client and Server.

## Technologies

- Python

## Setup

### Requirements
To run and edit this project locally, certify that you have installed the following programs:

- [Python](https://www.python.org/downloads/)
- A code editor

After that, you'll need to clone this repo:

```
git clone https://github.com/LBeghini/Chat.py.git
``` 

## Usage

To run this project, you'll only need two files:

- server.py
- client.py

Open ```cmd``` in the folder where you installed these files.

### Server

To run the server, execute:
```
python server.py
```
The script accepts a default argument that sets the server at localhost in the port 12000:

```
python server.py default
```

### Client

After setting and running the server, on another ```cmd```, run the client:

```
python client.py
```
Just like the server, the script also accepts a default argument that tries to connect in localhost under the port 12000:

```
python client.py default
```

You don't need to be forever alone and send messages only to yourself. It can work between your friends!  
It can be done using [Hamachi](https://vpn.net). You and your friends will need to download it.

It's simple to use, and what it does is simulate that all the connections are in the same local network.

After downloading it, create an network and set the IP of the ```server.py``` as the public IP given by Hamachi. The port can be settled as default.

Then, ask your friends to connect with your network through Hamachi. Then, give them the file ```client.py``` with the IP and port you've settled for the server.

As an last step, Windows Firewall will block Hamachi connections, but there's a way to [give permission to Hamachi](https://appuals.com/how-to-fix-inbound-traffic-blocked-on-hamachi/).

And that's it!




