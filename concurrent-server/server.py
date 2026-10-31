import socket
import time
import threading
import json

HOST = "127.0.0.1"
PORT = 5000

def predict(data):
    print(f"[{threading.current_thread().name}] Processing...")

    time.sleep(5)

    return {
        "prediction": "cat",
        "confidence": 0.98,
        "input": data.get("input")
    }


def handle_client(conn, addr):
    print(f"[{threading.current_thread().name}] Connected : {addr}")

    try:
        with conn:
            data = b""

            while b"\n" not in data:
                chunk = conn.recv(1024)

                if not chunk:
                    return

                data += chunk

                if len(data) >65536:
                    return

            request = json.loads(data.split(b"\n", 1)[0].decode())

            print(f"Recieved request from {addr} : {request}")

            result = predict(request)

            response = json.dumps(result) + "\n"

            conn.sendall(response.encode())

            print(f"Response sent to {addr}")

    except (OSError, ValueError, json.JSONDecodeError) as e:
        print(f"Error handling {addr}: {e}")

    finally:
        print(f"Connection closed: {addr}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))

server.listen()

print(f"Server listening on {HOST}:{PORT}")

while True:
    conn, addr = server.accept()

    thread = threading.Thread(target=handle_client,args=(conn,addr))

    thread.start()
