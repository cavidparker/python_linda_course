def main():
    a = 10
    b = "one"
    print(a)
    print(type(b), b)

if __name__=="__main__":main()


def main2():
    a, b = 0, 1
    a, b = b, a 
    print(a, b)

if __name__=="__main__":main2()    