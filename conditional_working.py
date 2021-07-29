def main():
    a, b = 0, 1
    if False:
        print("this is true man")
    elif a == b:
        print("It's equal")   
    else:
        print("this is false")  

if __name__=="__main__":main()   



def main2():
    a,b = 0, 1
    v = "this is good" if a < b else "this is bad"
    print(v)


if __name__=="__main__":main2()