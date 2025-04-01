import random

class Star:
    init_status = False
    def __init__(self,genSeed):
        self.star_class = "undefined"
        self.star_size = -1
        self.star_weight = -1
        self.star_temp = -1
        self.star_location = [-1] * 3
        self.genSeed = genSeed
    def classGen(self):
        random.seed(self.genSeed)
        generation_value = random.randint(0,10000000)
        return generation_value


star1 = Star(1)
print(star1.star_class)
aaa = star1.classGen()
print(aaa)