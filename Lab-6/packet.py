# packet.py - Packet-related functions

# Creates a packet from a sequence number and byte data
def make(seq_num, data = b''):
    #seq_bytes = seq_num.to_bytes(4, byteorder = 'little', signed = True)
    return str(seq_num) + "," + data

# Creates an empty packet
def make_empty():
    return ''

# Extracts sequence number and data from a non-empty packet
def extract(packet):
    seq_num = int(packet.split(",")[0])
    data = packet.split(",")[1]
    return seq_num, data

