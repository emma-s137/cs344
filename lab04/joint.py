'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

Added the joint probability distribution for 2 coin flips.

@author: kvlinden
@edited: ees32
@date: 02-28-20
@version Jan 1, 2013
'''

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

'''
b.
Hand calculation:

P(cavity | catch) = P(cavity & catch) / P(catch)

= (0.108 + 0.072) / (0.108 + 0.072 + 0.016 + 0.144) = 0.18/0.34 

= 0.529

'''

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print(PC.show_approx())


# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
# Probability distribution for 2 coins flips
P = JointProbDist(['Coin1', 'Coin2'])
T, F = True, False
P[T, T] = 0.25
P[F, T] = 0.25
P[T, F] = 0.25
P[F, F] = 0.25

PC = enumerate_joint_ask('Coin2', {'Coin1': T}, P)
print(PC.show_approx())

''' 
c. The answer does confirm what should be true about what will happen when two coins are flipped.

But you would not want to use full joint system for probability questions as the tables get very large very quickly.

'''