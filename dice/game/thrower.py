import random

# TODO: Define the Thrower class here.

class Thrower():
    def __init__(self) -> None:
        dice = 5
        num_throws = 0
    def throw_dice(self):
        return([random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)])