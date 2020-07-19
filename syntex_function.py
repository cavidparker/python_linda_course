def main():
    func()
    func()
    


def func():
    for i in range(10):
        print(i, end = " ")
    print()    

if __name__=="__main__":main()  



def main2():
    func2(2)
    func2(4)
    func2()


def func2(a =5):
    for j in range(a, 10):
        print(j, end = " ")
    print()

if __name__=="__main__":main2()            