import socket

host = '127.0.0.1'
port = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)
print(f'Server listening on {host}:{port}')

conn, addr = server.accept()
print(f'Connected by {addr}')

while(True):
    data = conn.recv(1024).decode()
    if data != "exit":

        print('Client sent:', data)

        response = data.upper()
        conn.send(response.encode())
        print('Sent to client:', response)

    elif(data == "exit"):
        exit_response = "exit"
        conn.send(exit_response.encode())

        conn.close()
        server.close()
        break



