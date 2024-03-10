import socket

# Define the host address and port to bind the server socket
host = '127.0.0.1'
port = 63732

# Function to handle communication with a client
def handle_client(client_socket, client_address):
    print(f"Connected with {client_address}")

    # Loop to receive and process messages from the client
    while True:
        # Receive message from the client
        message_recv = client_socket.recv(1024).decode()
        # If the message is empty, the client has disconnected, so break out of the loop
        if not message_recv:
            break
        # Print the received message
        print("From connected user: " + message_recv)
        # Prompt for a response from the server
        data = input(' -> ')
        # Send the response back to the client
        client_socket.send(data.encode())

    # Close the client socket after communication is finished
    print(f"Disconnected from {client_address}")
    client_socket.close()

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created!!")

# Bind the server socket to the specified host and port
server_socket.bind((host, port))

# Listen for incoming connections, allowing up to 3 queued connections
server_socket.listen(3)

# Print a message indicating that the server is waiting for connections
print(f"Waiting for connection on {host}:{port}")

# Accept an incoming connection from a client
client_socket, client_address = server_socket.accept()

# Call the handle_client function to handle communication with the client
handle_client(client_socket, client_address)

# Close the server socket after communication with the client is finished
server_socket.close()
