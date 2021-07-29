def main():
    name = open('lines.txt')
    for text in name.readlines():
        print(text, end='')

if __name__=="__main__":main()   


def enmrt():
    text = open('lines.txt')
    for index, texts in enumerate(text):
        print(index,texts, end='')



if __name__=="__main__":enmrt()        