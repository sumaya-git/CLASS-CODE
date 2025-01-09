
class Bottle:
    def __init__(self, price: float, size: float, id:int, content: list)-> None:
        self.price= price
        self.size= size
        self.id = id
        self.content= content

    def add(self, juice):
        self.contend.append(juice)
    
    
        
    

class Barrel:
    def __init__(self, id:int, size:float, price:float, apples:list) -> None:
        self.id= id
        self.size= size
        self.price= price
        self.apples= apples

    def add(self, apple:list):
        self.apples.append(apple)

   
class Basket:
    def __init__(self, id:int, size:float, price:float, oranges:list) -> None:
        self.id = id
        self.size= size
        self.prize= price
        self.oranges= oranges

    def add(self,orange:list):
        if len(self.oranges) < self.size:
            self.oranges.append(orange)
            return True
        else:
            return False

              

