class Person:
    def __init__(self, n, s, q = 1):
        self.name = n
        self.surname = s
        self.qualification = q
        
    def info(self):
        print ("{}, {}, {}".format(self.name, self.surname, self.qualification))
    
    def __del__(self):
            print ("До свидания мистер", self.name, self.surname, self.qualification)
        
employer_1 = Person("Irina", "Fisenko", 2)
employer_2 = Person("Kirill", "Svistunov", 2)
employer_3 = Person("Loser", "Chmo",)

list_employers = list(employer_1, employer_2, employer_3)

#list_employers = [employer_1, employer_2, employer_3]

employer_1.info()
employer_2.info()
employer_3.info()
print (list_employers)

while True:
    a = int(input("Enter employer's number for delit object "))
    if a == 1:
        del employer_1
        #employer_1.__del__()
        #print (list_employers)
        #input()
        break
    elif a == 2:
        del employer_2
        #employer_2.__del__()
        #print (list_employers)
        #input()
        break
    elif a == 3:
        #employer_3.__del__()
        del employer_3
        #employer_3.__del__()
        #print (list_employers)
        #input()
        break
    else:
        continue
#print (list_employers)
input()
