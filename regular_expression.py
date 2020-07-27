import re

def main():
    fh = open('regularExpression.txt')
    pattern = re.compile('(Len/Neverm)ore')
    for line in fh:
        if re.search(pattern,line):
            print(line,end='')

if __name__=="__main__":main()            