def main():

    x = [1, 2, 3]
    x.append(4)
    x.insert(0, 8)
    print(type(x), x)

if __name__=="__main__":main()    



def main2():
    name = "hello cavid"
    print(type(name), name[2:4])

if __name__=="__main__":main2() 



def main3():
    num = (1,2,3,4,5)
    for i in num:
        print(type(i), i)

if __name__=="__main__":main3()