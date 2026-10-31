import socket
import json
import sys
import time

HOST = "127.0.0.1"
PORT = 5000

client_id = sys.argv[1] if len(sys.argv) > 1 else "Client-1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

start = time.perf_counter()

client.connect((HOST, PORT))

request = {
    "task": "predict",
    "input": f"{client_id}_image.jpg"
}

message = json.dumps(request) + "\n"

client.sendall(message.encode())

response = b""

while b"\n" not in response:
    chunk = client.recv(1024)

    if not chunk:
        break

    response += chunk

if response:
    result = json.loads(response.split(b"\n", 1)[0].decode())
    print(f"{client_id} received: {result}")

client.close()

elapsed = time.perf_counter() - start

print(f"{client_id} completed in {elapsed:.2f} seconds")    
