# :speech_balloon: Chat.py

## About

TCP Chat is a simple program developed for an assignment of a Computer Networks class. It implements the usage of TCP to send messages between Client and Server.

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

- TCPServerChat.py
- TCPClientChat.py

Open ```cmd``` in the folder where you installed these files.

Then, run the server:
```
python TCPServerChat.py
```

After that, on another ```cmd```, run the client:

```
python TCPClientChat.py
```

> You won't see any broadcast if you run just one client. You need to run another client to see that happening.   
Then, you'll see messages that were sended in one terminal in the others that you've opened.
