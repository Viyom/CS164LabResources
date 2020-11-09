# sender.py - The sender in the reliable data transfer protocol
import packet
import socket
import sys
import _thread
import time

from timer import Timer

##TODO: Initialize the following variables
RECEIVER_ADDR = 
SENDER_ADDR = 
SLEEP_INTERVAL = 
TIMEOUT_INTERVAL = 
WINDOW_SIZE = 

# Shared resources across threads
base = 0
mutex = _thread.allocate_lock()
send_timer = Timer(TIMEOUT_INTERVAL)

# Sets the window size
def set_window_size(num_packets):
    global base
    return min(WINDOW_SIZE, num_packets - base)
# Send thread
def send(sock):
    global mutex
    global base
    global send_timer

    ## TODO: Add all the packets and corresponding seq_num to packets
    packets = []
    seq_num = 0

    ##TODO: Initialize window_size, next_to_send and base values
    window_size =
    next_to_send = 
    base =

    # Start the receiver thread
    _thread.start_new_thread(receive, (sock,))

    while base < num_packets:
        mutex.acquire()
        # Send all the packets in the window
        while next_to_send < base + window_size:
            # TODO: Send the packet and increase next_to_send counter
            print('Sending packet', next_to_send)

        # Start the timer
        if not send_timer.running():
            print('Starting timer')
            send_timer.start()

        # Wait until a timer goes off or we get an ACK
        while send_timer.running() and not send_timer.timeout():
            mutex.release()
            print('Sleeping')
            time.sleep(SLEEP_INTERVAL)
            mutex.acquire()

        if send_timer.timeout():
            # Looks like we timed out
            print('Timeout')
            send_timer.stop();
            ## TODO: Set appropriate value of next_to_send
            next_to_send = 
        else:
            print('Shifting window')
            ## TODO:  Set the correct window_size
            window_size =
        mutex.release()

    # TODO: Send empty packet as an indicator to close the connection
    
# Receive thread
def receive(sock):
    global mutex
    global base
    global send_timer

    while True:
        # TODO: Reveive packet and extract data and ack

        # If we get an ACK for the first in-flight packet
        print('Got ACK', ack)
        ack = int(ack)
        if (ack >= base):
            mutex.acquire()
            ## TODO: Set the correct value of base
            base = 
            print('Base updated', base)
            send_timer.stop()
            mutex.release()

# Main function
if __name__ == '__main__':

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(SENDER_ADDR)

    send(sock)
    sock.close()
