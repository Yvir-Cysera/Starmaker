import random

class Star:
    init_status = False
    def __init__(self):
        self.star_class = "undefined"
        self.star_size = -1
        self.star_weight = -1
        self.star_temp = -1
        self.star_location = [-1] * 3

star1 = Star()
print(star1.star_class)