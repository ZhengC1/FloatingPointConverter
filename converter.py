#! usr/bin/python

#this is the init function that will take in the input from the command line
def converting():
    print "hello, this is a 16 bit floating point converter it will convert from binary to decimal."
    #cat = raw_input("what is are your binary digits?: ")
    cat = "123456789ABCDEFG"
    print "first digit"
    first_bit = cat[:1:]
    print first_bit
    print "charateristic"
    charateristic = cat[1:6]
    print charateristic
    print "mantissa"
    mantissa = cat[6:16]
    print mantissa

    result = []

    if(first_bit == "1"):
        result.append("-")
    result.append(



converting()
