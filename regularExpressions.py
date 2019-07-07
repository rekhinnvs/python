import re
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

def regular_expressions():
    pattern = re.compile("[a-z]+")
    #print(pattern)
    m = pattern.match("hello world")

    # Returns the match
    print(m.group())

    # returns a tuple containing the strings for all the subgroups
    print(m.groups())

    # returns all the matches
    p = re.compile(r'\d+')
    _list = p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
    #print(_list)

    #Save the result as an iterator
    p = re.compile(r'\d+')
    iterator = p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
    for value in iterator:
        pass
        #print(value)

    

regular_expressions()
