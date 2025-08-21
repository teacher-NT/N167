import os
os.system("cls")

class Person:
    def __init__(self,n,s,a):
        self.name = n
        self.surname = s
        self.age = a

    def __str__(self):
        return f"{self.name} {self.surname}"
    
    def __gt__(self, obj):
        return self.age > obj.age
    
    def __lt__(self, obj):
        return self.age < obj.age
    
    def __eq__(self, obj):
        return self.age == obj.age
    
    def __add__(self, obj):
        return self.age + obj
    
    def __sub__(self, obj):
        return self.age - obj
    
    def __mul__(self, obj):
        return self.age * obj
    
    def __truediv__(self, obj):
        return self.age / obj
    
    def __len__(self):
        return len(self.name+self.surname)
    
    def __getitem__(self, n):
        if n == 'name':
            return self.name
        elif n == 'surname':
            return self.surname
        elif n == 'age':
            return self.age
        else:
            return "KeyError"
        
    def __setitem__(self, n, m):
        if n == 'name':
            self.name = m
        elif n == 'surname':
            self.surname = m
        elif n == 'age':
            self.age = m
        else:
            return "KeyError"

    
p1 = Person("Ali", "Valiev", 19)
p2 = Person("Sherzod", "Ochilov", 22)

p1['name'] = "Dilshod"
print(p1)

# print(len(p1))



