import copy
import random

class Hat:
    
    def __init__(self, **args):
        if len(args) < 1:
            raise TypeError("Specify more arguments")
        self.contents = []
        for color,number in args.items():
            self.contents.extend([color]*number)
        print(self.contents)

    def draw(self, numberToDraw):
        drawnBalls = []
        if numberToDraw > len(self.contents):
            drawnBalls = self.contents.copy()
            print(drawnBalls)
            self.contents.clear()
            return drawnBalls

        drawnBalls = random.sample(self.contents, numberToDraw)

        for i in drawnBalls:
            self.contents.remove(i)
        return drawnBalls



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    counter = 0
   
    for experiment in range(num_experiments):
        copied = copy.deepcopy(hat)
        drawn = copied.draw(num_balls_drawn)

        expected_list = []
        for color, number in expected_balls.items():
            expected_list.extend([color]*number)
        
        success = True
        for color,number in expected_balls.items():
            if drawn.count(color)<number:
                success = False
                break

        
        if success:
            counter+=1
    result = counter/num_experiments
    return result



hat1 = Hat(yellow=3, blue=2, green=6)
#print(hat1.draw(5))

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(probability)