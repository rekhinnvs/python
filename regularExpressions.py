def read_file(file):
    with open(file, "r") as reader:
        ''' readline() will read an entire line'''
        return
        print(reader.readline(5))
        print(reader.readline(4))

#read_file("./zomato.csv")

def read_files(file):
    """ readlines() will read the entire file"""
    with open(file, "r") as reader:
            print(reader.readlines(1))

read_files("./zomato.csv")

def iterating_reverse():
        name = "Hello world"
        for i in range(-1,-len(name)-1,-1):
                print(name[i], end="")

#iterating_reverse()