#MADE BY YOURS TRULY

import random

def sign(n):
    if n >= 0:
        return 1
    else:
        return -1

class Brain():
    def __init__(self):
        self.lr = 0.1
        self.weights = [round(random.uniform(-1,1),2)]
    
    def guess(self,inputs):
        the_sum = 0
        output = 0
        for i, thing in enumerate(self.weights):
            the_sum += float(inputs) * self.weights[i]

        output = sign(the_sum)
        return output

    def train(self, inputs, label):
        guess = self.guess(inputs)
        error = label - guess

        for i, thing in enumerate(self.weights):
            self.weights[i] += error * inputs * self.lr

class num():
    def __init__(self):
        self.number = random.randint(1,1000)
        if self.number%2 == 0:
            self.label = 1
        else:
            self.label = -1



def main():
    random_numbers = []
    numbers_labels = []

    for i in range(1000):
        n = num()
        random_numbers.append(n.number)
        numbers_labels.append(n.label)
    
    inputs = 4

    brain = Brain()
    
    for i, thing in enumerate(random_numbers):
        brain.train(random_numbers[i], numbers_labels[i])


    guess = brain.guess(inputs)
    print (guess)



main()
