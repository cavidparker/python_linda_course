def main():
    test(42,61)


def test(number ,another = None, onemore=82):
    if another is None:
        another = 121 
    print("testing function : ",number,another,onemore)




if __name__=="__main__":main()        