# def main():
#     print("This is the syntexfile.")
    


# def egg():
#     print(" hello eggie") 
      
# # main()
# # egg()
# if __name__=="__main__":egg()

# # if __name__=="__main__":main()
## Prime number 
def main2():
    for n in primes():
        if n > 100: break
        print(n)

def isprime(n):
    if n==1: # one is not prime number
        return False 
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True 

def primes(n = 1):
    while(True):
        if isprime(n): yield n 
        n +=1

if __name__=="__main__":main2()        


