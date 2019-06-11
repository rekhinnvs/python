class MyClass :
    i = 10
    def fun(self):
        print("From class member function")


def main():
    print("hello world")
    print(MyClass.i)

if __name__ == "__main__":
    main()