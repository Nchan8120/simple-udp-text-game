import socket

# constant socket number for the discovery service

disc_port = 4444

# Dictionary where keys are the names of a room and the values is the port number that it's on

Dict = {}

# Discovery Socket

disc_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Process incoming message

def process_message(message, addr, disc_socket):
    global Dict
    words = message.split()

    if (words[0] == "REGISTER"):
        for key in Dict:
            if key == words[1]:
                message = "NOTOK port number already in use"
                return message
        Dict[words[2]] = words[1]
        message = "OK"
        s = words[1]+" registered"
        print(s)
        return message
    elif (words[0] == "DEREGISTER"):
        try:
            Dict.pop(words[1])
            s = words[1]+" successfully deregistered"
            print(s)
            return "OK"
        except:
            return "NOTOK"
    elif (words[0] == "LOOKUP"):
        room_addr = Dict.get(words[1])
        print("looking up "+words[1])
        try:
            room_addr = Dict.get(words[1])
            message = "OK "+room_addr
            print(room_addr)
            return message
        except:
            return "NOTOK"


def main():
    global disc_socket
    disc_socket.bind(('', disc_port))
    print('\nDiscovery service will wait for rooms at port: ' + str(disc_socket.getsockname()[1]))

    # Loop forever waiting for messages from clients or rooms.

    while True:

        # Receive a packet from a client and process it.

        message, addr = disc_socket.recvfrom(1024)

        # Process the message and retrieve a response.

        response = process_message(message.decode(), addr, disc_socket)

        # Send the response message back to the client.

        disc_socket.sendto(response.encode(),addr)

if __name__ == '__main__':
    main()