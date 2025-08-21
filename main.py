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

    
p1 = Person("Ali", "Valiev", 19)
p2 = Person("Sherzod", "Ochilov", 22)
davlatbek = Person("Davlatbek", "Zokirov", 22)

print(p1 + 10)
print(p1 - 5)
print(p1 * 2)
print(p1 / 9)

