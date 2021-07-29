# class  Egg:
#     # def __init__(self, kind = "fride"): 
#         # self.kind = kind

#     def whatKind(self):
#         return self.kind    
 
 
# def main():
#     fried = Egg()
#     # scramble = Egg('scrambled')
#     # print(fried.whatKind())
#     fried.kind = "somekind"
#     print(fried.kind)

class Person:
    def __init__(self,name = "no_name"):
        self.name = name

if __name__=="__main__": 
    person = Person("tariqul")
    
    print(person.name) 

   

    # fried = Egg()
    # # scramble = Egg('scrambled')
    # # print(fried.whatKind())
    # fried.kind = "somekind"
    # print(fried.kind)


