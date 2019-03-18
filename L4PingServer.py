import socket, sys

def main():
    # Prepare the server socket
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind(('',6789))


    while True:
        # Wait for a packet to arrive
        data, address = serverSocket.recvfrom(1024)
        print "Received %s bytes from %s:%s"%(len(data),address[0],address[1])
        print "    Data: %s"%data

        # Once a packet is received, resend the payload to the sender
        if data:
                serverSocket.sendto(data,address)
    return

if __name__ == '__main__':
    main()
