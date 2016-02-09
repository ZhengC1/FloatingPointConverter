#! usr/bin/python

def convert():
    number = "10101010101010101010101010101011"
    print number[:1]

    print number[1:9]
    print int(number[1:9], 2)
    print number[9:31]

convert()
