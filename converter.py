#! usr/bin/python

class floating_point(object):

    def __init__(self):
        print "hello, this is a 16 bit floating point converter,
        it will convert from binary to decimal."
        cat = raw_input("what is are your binary digits?: ")
        first_bit = cat[1:]
        print first_bit
        charateristic = cat[2:10]
        print charateristic

    def convert():
        hex_number = raw_input("whats your number in hex?: ")

        h_size = len(hex_number) * 4

        binary_number = ( bin(int(hex_number, 16))[2:] ).zfill(h_size)

        print binary_number[:1]

        print binary_number[1:9]
        print int(binary_number[1:9], 2)
        print binary_number[9:31]

squirrel = new floating_point()

