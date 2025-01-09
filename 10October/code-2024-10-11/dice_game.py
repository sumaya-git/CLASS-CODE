from typing import Type
from copy import deepcopy
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



d8 = D8()
d8.face

d8.roll()
d8.face

d4 = D4()
d6 = D6()
d8 = D8()
d10 = D10()

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
    
    class D11():
        pass
    
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

d4 = D4()
d6 = D6()
d8 = D8()
d10 = D10()

print(d4)
print(d6)
print(d8)
print(d10)

from abc import ABC, abstractmethod
class Die:
    def __init__(self):
        self.face: int
        self.roll()
    @abstractmethod   
    def roll(self):
        ...

    def __str__(self) -> str:
        return f'{self.face}'
    
    def __repr__(self, ) -> str:
        return f'{self.face}'
        

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
        
class D11(Die):
    pass


d4 = D4()
d6 = D6()
d8 = D8()
d10 = D10()
d11 = D11()


from typing import Type

class DiceBoard:
    def __init__(self, *die_classes: Type[Die]):
        self.dice: list[Die] = [die() for die in die_classes]

    def roll_all_dice(self):
        for die in self.dice:
            die.roll()
        
@property
def dice(self):
    return self.__dice

@dice.setter
def dice(self, value):
    raise NotImplementedError


@property 
def total(self):
    return sum(die.face for die in self.dice)

dice_board = DiceBoard(D4, D8, D10)
dice_board.total()

dice_board.roll_all_dice()
dice_board.total()




#today

from abc import ABC, abstractmethod
from typing import Type

class DiceGameBase(ABC):
    def __init__(self):
        self._dice_board: DiceBoard
        self._player_name: str
        self._roll_trials: int
            
    @abstractmethod
    def check_winner(self):
        ...
        
    @abstractmethod
    def roll(self):
        ...
        
    @abstractmethod
    def add_dice(self, die_class: Type[Die]):
        ...
    
    @property
    @abstractmethod
    def total_points(self):
        ...




class DummyDiceGame(DiceGameBase):
    def __init__(self, dice_board: DiceBoard, player_name: str):
        self._dice_board = dice_board
        self._player_name = player_name
        self.roll_trials = 5
        
    def check_winner(self):
        return self._dice_board.is_winner()
    
    def roll(self, pos: list[int]):
        if self.roll_trials <= 0:
            raise OperationalError('You have exhausted your roll trials')
        
        if pos:
            self._dice_board.to_be_rolled(pos).roll_all_die()
        else:
            self._dice_board.roll_all_die()
        
        # reduce roll trials
        self.roll_trials -= 1
        
    def add_dice(self, dice_class: Type[Die]):
        self._dice_board = self._dice_board + dice_class
        
    @property
    def total_points(self):
        return self._dice_board.total
    
    @property
    def dice(self):
        return self._dice_board.dice


def main():
    player_name = 'Eyong' # input('Player, please state your name: ')
    dice_board = DiceBoard(D4, D6, D8)
    game = DummyDiceGame(dice_board, player_name)
    
    # since we had a free initial roll,
    if game.check_winner():
        print(f'{player_name} Wins with dice {game.dice}')
    else:
        print(f'{player_name} Loss with dice {game.dice}')



