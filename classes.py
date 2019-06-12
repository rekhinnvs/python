
def outside_class(self, x, y) :
    return x + y

class MyClass :
    i = 10
    sum = outside_class

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def fun(self):
        print("From class member function")
        #print(self.x, self.y)

class DerivedClass(MyClass):
    name = "rekhin"
    def __init__(self, a, b):
        self.a = a
        self.b = b


def main():
    x = MyClass(5, 10)
    x.fun()
    print(x.sum(4,8))

    dc_obj = DerivedClass(4, 3)
    print(f"I am from base class accessed by sub class {dc_obj.fun()}")
    print(f"Accessing base class member by using sub class object, value of i  {dc_obj.i}")


if __name__ == "__main__":
    main()
    #pass
