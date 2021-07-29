def main():
    a, b = 1, 1
    if a < b:
        print("a is less than b")
    elif a > b:
        print("a is greater than b")    
    else:
        print("a equal to b")    
if __name__=="__main__":main()    


def main2():
    a, b = 0, 1
    s = "less than" if a < b else "nothing"
    print(s)
if __name__=="__main__":main2()    