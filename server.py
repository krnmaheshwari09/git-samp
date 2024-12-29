# import socket

# s = socket.socket()

# s.bind(("0.0.0.0", 9999))
# s.listen()
# # 172.18.7.175
# f = open("server.py", 'rb')
# c, add = s.accept()

# name = c.recv(1024).decode()
# print(f"Connected to {add} name {name}")
# while True:
#     chunk = f.read(1024)
#     if not chunk:
#         break
#     c.send(bytes(chunk))

# f.close()
# s.close()

import socket
import os

def start_server():
    # Server IP and Port
    SERVER_IP = "0.0.0.0"
    SERVER_PORT = 9999

    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(3)  # Listen for up to 5 connections
    print(f"Server started at {SERVER_IP}:{SERVER_PORT}")

    while True:
        print("Waiting for a connection...")
        client_socket, client_address = server_socket.accept()
        print(f"Connected to {client_address}")

        # Get list of files in the current directory
        files = os.listdir()
        files_list = "\n".join(files)
        client_socket.send(files_list.encode())  # Send file list to the client

        # Receive requested file name from the client
        file_name = client_socket.recv(1024).decode()
        print(f"Client requested file: {file_name}")

        # Check if the file exists and send its content
        if os.path.isfile(file_name):
            with open(file_name, "rb") as f:
                file_content = f.read()
            client_socket.send(file_content)  # Send file content
        else:
            client_socket.send(b"ERROR: File does not exist.")  # Send error message

        if file_name == "exit":
            break
        print(f"Connection to {client_address} closed.")
    server_socket.close()
if __name__ == "__main__":
    start_server()


print("Karan")
print("Karan Maheshwari")

print("Karan - A")
print("Karan Maheshwari - A")