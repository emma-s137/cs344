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
happy = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
])

# Compute probability of raise given it's sunny

print(" \nProbability of raise given sunny")
print(enumeration_ask('Raise', dict(Sunny=T), happy).show_approx())

print(" \nProbability of raise given happy and sunny")
print(enumeration_ask('Raise', dict(Sunny=T, Happy=T), happy).show_approx())

print(" \nProbability of raise given happy")
print(enumeration_ask('Raise', dict(Happy=T), happy).show_approx())

print(" \nProbability of raise given happy and not sunny")
print(enumeration_ask('Raise', dict(Sunny=F, Happy=T), happy).show_approx())

''' Hand Calculations

a. 

i. P(Raise | Sunny) = P(Raise) * P(Sunny | Raise) / P(Sunny) 
                 = <0.01 * 0.7 / 0.7, 0.99 * 0.7 / 0.7>
                 Sunny is not dependent on Raise
                 Raise is not dependent on Sunny
                 = <0.01, 0.99>
                 
ii. P(Raise | Happy ^ Sunny) = P(Raise) * P(Happy | Raise ^ Sunny) * P(Sunny| Raise ^ Happy), P(-Raise) * P(Happy | -Raise ^ Sunny) * P(Sunny | -Raise ^ Happy)
                             = <0.01 * 1.0 * 0.7, 0.99 * 0.7 *0.7>
                             = <0.007, 0.4851>
                             = 0.007 + 0.4851 = 0.4921
                             <0.007, 0.4851> / 0.4921
                             = <0.014 , 0.986>
'''

'''' 
The Probability of a raise given happy is still low at 1.42% because thr probability of a raise is so low. 
The probability of a raise then goes up to 8% when we are given that it is not sunny because even though sunniness 
doesn't cause quite as much happiness it is much more likely then a raise. Therefore the probability of a raise then
goes up, as we are still happy.
'''