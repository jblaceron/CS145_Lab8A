# The server-side code, named L4PingServer.py receives UDP segments
# from clients, copies the payload, and then sends back a UDP segment
# to the client with the same payload.

import socket, sys

def main():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind(('',6789))

    while True:
        data, address = serverSocket.recvfrom(1024)
        print "Received %s bytes from %s:%s"%(len(data),address[0],address[1])
        if data:
                serverSocket.sendto(data,address)
    return

if __name__ == '__main__':
    main()
