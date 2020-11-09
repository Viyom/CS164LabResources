# receiver.py - The receiver in the reliable data transer protocol
import packet
import socket
import sys

RECEIVER_ADDR = ('localhost', 8080)

# Receive packets from the sender
def receive(sock):
    expected_num = 0
    while True:
        # TODO: Get the next packet from the sender
        pkt, addr = 
        if not pkt:
            break
        seq_num, data = packet.extract(pkt)
        print('Got packet', seq_num)
        
        # TODO: Make and send back an ACK for both conditions accordingly
        if seq_num == expected_num:
            print('Data received:', data)
        else:
            print('Sending ACK', expected_num - 1)

# Main function
if __name__ == '__main__':
        
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(RECEIVER_ADDR) 
    receive(sock)
    sock.close()
