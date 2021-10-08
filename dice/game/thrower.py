import random


# TODO: Define the Thrower class here.

class Thrower():
    def __init__(self):
        self.dices = 5
        self.missed_rolls = 0
        num_throws = 0
    def throw_dice(self):
        self.dices = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
        return(self.dices)
    def get_points(self):
        points_got = 0
        self.missed_rolls = 0
        for x in self.dices:
            if x == 1:
                points_got += 100
            elif x == 5:
                points_got += 50
            else:
                self.missed_rolls += 1

        return points_got
    def can_throw(self):
        if self.missed_rolls >= 5:
            return False
        else:
            return True
        

