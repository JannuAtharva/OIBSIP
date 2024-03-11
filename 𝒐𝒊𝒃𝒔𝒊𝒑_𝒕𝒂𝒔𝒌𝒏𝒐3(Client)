import socket

# Define the server's address and port
host = '127.0.0.1'
port = 63732

# Create a socket object for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
try:
    client_socket.connect((host, port))
except ConnectionRefusedError:
    print("Error: Connection refused. Make sure the server is running.")
    exit()

# Loop to send and receive messages
message = input("Message from client -->")  # take input
while message.lower() != 'bye':

    # Send message to the server
    client_socket.send(message.encode())

    # Receive response from the server
    message_recv = client_socket.recv(1024).decode()
    
    # Print the received response
    print('Received from server: ' + message_recv)
    
    message = input("Message from client -->")  # again take input

# Close the client socket
client_socket.close()
