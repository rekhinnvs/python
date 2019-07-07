import re
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