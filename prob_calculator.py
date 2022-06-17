import copy
import random
# Consider using the modules imported above.

class Hat:
    # initialisation
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            for i in range(v):
                self.contents.append(k)

    # taking balls from hat
    def draw(self, n):
        n = min(n, len(self.contents))
        s = []
        for i in range(n):
            s.append(self.contents.pop(random.randrange(len(self.contents))))
        return s

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    # in the beginning we take 0 ball from hat
    balls = 0
    for i in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        balls_drawn = new_hat.draw(num_balls_drawn)
        flag = True
    
        # check if we draw the ball out of the hat 
        for k, v in expected_balls.items():
            if balls_drawn.count(k) < v:
                flag = False
                break
    
        # if we could draw the ball out of the hat
        if flag:
            balls += 1
    
    # how many times we were able to draw the ball out of the hat from all attempts
    probability = balls / num_experiments
    return probability