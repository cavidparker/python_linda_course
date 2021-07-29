def main():
    name = "hello world"
    for i,names in enumerate(name):
        if names == 'l':
            print("index {} as l".format(i))
        # print(i,names)

if __name__=="__main__":main()  



def main2():
    s = 'this is string'
    for i in s:
        if i=='i':continue
        print(i,end='')

if __name__=="__main__":main2()        