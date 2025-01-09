
class Die:
    def __init__(self):
        self.face: int
        self.roll()
        
    def roll(self):
        ...

  
    

from random import randint

class D4(Die):
    def roll(self):
        self.face = randint(1, 4)

class D6(Die):
    def roll(self):
        self.face = randint(1, 6)
        

class D8(Die):
    def roll(self):
        self.face = randint(1, 8)


class D10(Die):
    def roll(self):
        self.face = randint(1, 10)

d4 = D4
d6 = D6
d8 = D8
d10 = D10

d8 = D8()
d8.face

d8.roll()
d8.face

print(d4)
d4.face


class Die:
    def __init__(self):
        self.face: int
        self.roll()
        
    def roll(self):
        ...

    def __str__(self) -> str:
        return f'{self.face}'
    


d4 = D4
d6 = D6
d8 = D8
d10 = D10

print(d4)
print(d6)
print(d8)
print(d10)