"""
This module implements local search on a simple sine function variant.
(see the sine function variant in graphs.py).
@edited: ees32
@author: kvlinden
@version 6feb2013
"""
import math
import time
from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange


class Sine(Problem):
    """
    State: x value for the sin function variant f(x)
    Move: a new x value delta steps from the current x (in both directions)
    """

    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta

    def actions(self, state):
        return [state + self.delta, state - self.delta]

    def result(self, stateIgnored, x):
        return x

    def value(self, x):
        result = abs(x * math.sin(x))
        return result



if __name__ == '__main__':
    # Formulate a problem with a 2D hill function.
    maximum = 30

    for x in range (0,100):
        initial = randrange(0, maximum)
        time1 = time.time()

        p = Sine(initial, maximum, delta=1)
        time2 = time.time()
        print('Initial                      x: ' + str(p.initial)
              + '\t\tvalue: ' + str(p.value(initial))
              + "\t\ttime: %0.3f seconds" % (time2 - time1)
              )

        # Solve the problem using hill-climbing.
        time1 = time.time()
        hill_solution = hill_climbing(p)
        time2 = time.time()
        print('Hill-climbing solution       x: ' + str(hill_solution)
              + '\tvalue: ' + str(p.value(hill_solution))
              + "\t\ttime: %0.3f seconds" % (time2 - time1)
              )

        # Solve the problem using simulated annealing.
        time1 = time.time()
        annealing_solution = simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=1000)
        )
        time2 = time.time()
        print('Simulated annealing solution x: ' + str(annealing_solution)
              + '\tvalue: ' + str(p.value(annealing_solution))
              + "\t\ttime: %0.3f seconds" % (time2 - time1) + "\n "
              )
