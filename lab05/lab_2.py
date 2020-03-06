'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@edited by ees32
@date 03-06-20

@author: kvlinden
@version Jan 2, 2013
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.90, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.90, F: 0.2})
    ])


#Compute probability of cancer given you have two postive test

print(" \nProbability of cancer given two positive tests")
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())

print(" \nProbability of cancer given one positive and one negative test")
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())

''' Hand Calculations

a. P(C | t2 ^ t1) = < P(C) * P(t1 | C) * P(t2| C), P(-C) * P(t1 | -C) * P(t2 | -C)>
                  = < 0.01 * 0.9 * 0.9, 0.99 * 0.2 * 0.2>
                  = < 0.0081, 0.0396>
                  0.0081 + 0.0396 = 0.0477
                  < 0.0081, 0.0396> / 0.0477
                  = <0.17, 0.83>
                  
b. P(C | t2 ^ -t1) = < P(C) * P(-t1 | C) * P(t2| C), P(-C) * P(-t1 | -C) * P(t2 | -C)>
                  = < 0.01 * 0.1 * 0.9, 0.99 * 0.8 * 0.2>
                  = < 0.0009, 0.1584>
                  0.0009 + 0.1584 = 0.1593
                  < 0.0009, 0.1584> / 0.1593
                  = <0.0056, 0.994>

'''

''' These results do make sense even though they are surprising because the probability of having cancer is
    just so low that even when you have two positive tests your probability of having cancer is still only
    17 %
    
    The effect of having one failed tests is huge. As your probability of having cancer went from 17% to 0.56%
    '''
