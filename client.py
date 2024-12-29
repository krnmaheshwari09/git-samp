import socket

def start_client():
    # Server IP and Port
    SERVER_IP = "172.18.7.175"
    SERVER_PORT = 9999

    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))
    print(f"Connected to server {SERVER_IP}:{SERVER_PORT}")

    # Receive list of files
    while True:
        files_list = client_socket.recv(1024).decode()
        print("Files available on server:")
        print(files_list)

        # Request a file
        file_name = input("Enter the name of the file you want to open: ")
        client_socket.send(file_name.encode())
        if file_name == "exit":
            break

        # Receive file content or error message
        file_content = client_socket.recv(4096)  # Receive file content in chunks
        if file_content.startswith(b"ERROR"):
            print(file_content.decode())
        else:
            print(f"Content of '{file_name}':")
            print(file_content.decode(errors='ignore'))  # Decode and handle binary data

    client_socket.close()

if __name__ == "__main__":
    start_client()
