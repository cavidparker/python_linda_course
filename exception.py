def main():
    try:
        file = open('xlines.txt')
    except:
        print("did not found the file")
    else:        
        for files in file:
            print(files.strip())


if __name__=="__main__":main()     



def main2():
    try:
        file = open('xlines.txt')
    except IOError as e:
        print("did not found the file", e)
    else:
        for files in file:
            print(files.strip())   

if __name__=="__main__":main2()      



def main3():
    file = open('lines.txt')
    try:
        for files in file:
            print(files.strip())
    except:
        print("did not found the file")        

if __name__=="__main__":main3()