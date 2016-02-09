#! usr/bin/python

def convert():

    hex_number = raw_input("whats your number in hex?: ")

    h_size = len(hex_number) * 4

    binary_number = ( bin(int(hex_number, 16))[2:] ).zfill(h_size)

    print binary_number[:1]

    print binary_number[1:9]
    print int(binary_number[1:9], 2)
    print binary_number[9:31]

convert()
