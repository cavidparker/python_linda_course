def main():
    a,b = 0,1
    while b < 50:
        a,b = b, a+b
        print(a,b)


if __name__=="__main__":main()  



def main2():
    a = 'this is string'
    i = 0
    while(i < len(a)):
        print(a[i], end='')
        i = i+1


if __name__=="__main__":main2()        