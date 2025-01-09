

class A:
    def __init__(self, item: int):
        self._item = item

    def __add__(self, x):
        if isinstance(x, int):
            return self._item + x
        
        else:
            return self._item + x._item
        
    def __repr__(self):
        return f'{self._item}'
    
    def __sub__(self, x):
        if isinstance(x, int):
            return self._item - x
        else:
            return self._item - x._item

        
    def __isub__(self, x):
        if isinstance(x, int):
            self._item -= x
        else:
            self._item -= x._item
        return self


    def __rsub__(self, x):
        if isinstance(x, int):
            return x - self._item
        else:
            return x._item - self._item


# Multipication

    def __mul__(self, x):
        if isinstance(x, int):
            return self._item * x
        else:
            return self._item * x._item
        
        

    def __rmul_(self, x):
        return self.__rmul_(x)
    
    def __imul__(self, x):
        if isinstance(x, int):
            self._item *= x

        else:
            self._item *= x._item

        return self

# Division

    def __truediv__(self, x):
        if isinstance(x, int):
            self._item / x
        else:
            return self._item / x._item
        
        return self
    
    def __itruediv__(self, x):
        if isinstance(x, int):
            self._item /= x

        else:
            self._item /= x._item

        return self


# Comparition
    def __eq__(self, x):
        if isinstance(x, int):
            self._item == x

        else:
            self._item == x._item
        
    def __gt__(self, x):
        if isinstance(x, int):
            self._item > x
        else:
            self._item > x._item

        return self

    def __lt__(self, x):
        if isinstance(x, int):
            self._item < x
        else:
            self._item < x._item

        return self

    def __ne__(self, x):
        if isinstance(x, int):
            
            return self._item != x
        else:
            return self._item != x._item


        
        

a1 = A(12)
a2 = A(6)
print(a1 -a2) 

a1 -= 3      
print(a1) 

print(4-a1)

a1 = 3
a2 = 6
print(a1 * a2)
print(a1 * 3)

print(3 * a1)
a1 *= 5
print(a1)


print(a1 / a2 )
print(a1 / 4)

a1 /= a2
print(a1)


print(a1 == a2)
print(a1 > a2)

print(a1 < 5)

print(a1 != a2)
