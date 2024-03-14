a = [1,2,3]
b = [1,2,3]

a = 123
b = 123

class A:
    def __init__(self):
        self.x = 1
        
a = A()
b = A()

print(a is b)