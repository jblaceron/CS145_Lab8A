import socket, sys
import time
from timeit import default_timer as timer

def main():
    if len(sys.argv) >= 2:

        # Get the value of the ping target from the command line arguments
        ADDR = str(sys.argv[1])
        PORT = 6789
        target = (ADDR,PORT)

        # Prepare the client socket
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # The socket will timeout after 2 seconds
        clientSocket.settimeout(2.0)

        for i in range(1,4):
            # Send the data (1, 2, 3) to the target server
            sent = clientSocket.sendto(str(i),target)

            # Get the current time
            start = timer()
            try:

                # Listen for the value that was sent (1, 2, 3)
                data = ""
                while not data:
                    data, server = clientSocket.recvfrom(1024)
                    print("hello world!")
                    # If the resent value is correct, print the elapsed time
                    if data == str(i):
                        end = timer()
                        print 'Packet %s: %.6fms'%(i,(end-start)*1000)
                    # Else, keep listening for the correct value
                    else:
                        data = ""
            # When the socket times out, assume the packet is lost
            except:
                print 'Packet %s: LOST'%i
    else:
        print "No target address."
        return

    return

if __name__ == '__main__':
    main()
