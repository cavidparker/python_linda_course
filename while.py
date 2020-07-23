def main():
    a,b = 0,1
    while b < 50:
        a,b = b, a+b
        print(a,b)


if __name__=="__main__":main()    