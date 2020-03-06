'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@edited by ees32
@date 03-06-20

@author: kvlinden
@version Jan 2, 2013
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask, rejection_sampling, likelihood_weighting

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

# Compute P(Burglary | John and Mary both call).
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# elimination_ask() is a dynamic programming version of enumeration_ask().
print(elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# gibbs_ask() is an approximation algorithm helps Bayesian Networks scale up.
print(gibbs_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# See the explanation of the algorithms in AIMA Section 14.4.

print(rejection_sampling('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary, 10000).show_approx())

print(likelihood_weighting('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary, 10000).show_approx())



print(" \n P(Alarm | Burglary & not Earthquake)")
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())

print(" \n P(JohnCalls | Burglary & not Earthquake)")
print(enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())

print("\n P(Burglary | Alarm)")
print(enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())

print("\n P(Alarm | JohnCalls & MaryCalls)")
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())

'''
The rejection sampling and likelihood weighting solutions are both often very off of the enumeration
solution. This is because they are determined from direct sampling. 

The gibbs meanwhile is much more accurate as it produces samples following a Markov Chain. This leads to better
posterior (diagnostic) probability approximations which fits with the specific question asked in this instance.
'''