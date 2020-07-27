def main():
    try:
        for files in readfile('xlines.doc'):
            print(files.strip())
    except IOError as e:
        print("din't find the file", e) 
    except ValueError as e:
        print("bad file name",e)          

def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else: raise ValueError('Filename must end with .txt')            




if __name__=="__main__":main()        