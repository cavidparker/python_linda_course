def main():
    testFunc(22, 23, 24, 100,200,300,400,one = 1, two = 2, three =3)
    for j in ret():
        print(j, end = ' ')



def testFunc(rahim,karim,babu,*args,**kwargs):
    print("all list: ",rahim,karim,babu,args,kwargs['one'],kwargs['two'],kwargs['three'])


def ret():
    return range(0, 25)

    

if __name__=="__main__":main()