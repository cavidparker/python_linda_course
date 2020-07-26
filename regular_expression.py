import re

def main():
    file = open('regularExpression.txt')
    for files in file:
        if re.search('(Len/Neverm)ore',files):

            print(files, end ='')


if __name__=="__main__":main()        