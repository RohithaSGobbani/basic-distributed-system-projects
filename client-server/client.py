import socket

host = '127.0.0.1'
port = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

while(True):
    msg = input("Enter a msg:")

    client.send(msg.encode())

    rec = client.recv(1024).decode()

    if(rec == "exit"):
        client.close()
        break

    print("Recieved from server:", rec)

