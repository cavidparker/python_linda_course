def main():
    testFun(42,43,44,80,81,82,84)


def testFun(this, that, what, *args):
    print(this,that,what)
    for i in args:
        print(i, end = ' ')
        # print("This is test function :", this,that,what,args) 


if __name__=="__main__":main()       