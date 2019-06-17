import re
def regular_expressions():
    pattern = re.compile("[a-z]+ *")
    #print(pattern)
    m = pattern.match("hello worlab")

    # Returns the match
    #print(m.group())

    # returns all the matches
    p = re.compile(r'\d+')
    _list = p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
    #print(_list)

    #Save the result as an iterator
    p = re.compile(r'\d+')
    iterator = p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
    for value in iterator:
        print(value)

    

regular_expressions()