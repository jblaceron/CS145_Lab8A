import socket, sys
from threading import Thread, Event
import time
from timeit import default_timer as timer

def main():
    if len(sys.argv) >= 2:
        ADDR = str(sys.argv[1])
        PORT = 6789
        target = (ADDR,PORT)

        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        clientSocket.settimeout(1.0)
        for i in range(1,4):
            sent = clientSocket.sendto(str(i),target)
            start = timer()
            try:
                data = ""
                while not data:
                    data, server = clientSocket.recvfrom(1024)
                    if data == str(i):
                        end = timer()
                        print 'Packet %s: %f'%(i,end-start)
                    else:
                        data = ""
            except:
                print 'Packet %s: LOST'%i
    else:
        print "No target address."
        return

    return

if __name__ == '__main__':
    main()
