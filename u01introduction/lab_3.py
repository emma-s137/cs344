"""
    CS344
    This module implements the simple cat jumping into lake problem using PAIP GPS.
    A cat is trying to jump into the middle of the lake, but it must first be picked up
    on one of the ports.
    The current problem cannot be solved by the GPS, but if the preconditions for cat
    jumps over board are switched, so that cat on board is first then the GPS can solve the
    problem.
"""
from gps import gps
import logging

# Formulate the problem states and actions.
problem = {

    'initial': ['boat at North port', 'no cat on board'],
    'goal': ['cat in lake' , 'no cat on board', 'boat in lake'],

    'actions': [
        {
            'action': 'boat moves to middle of lake',
            'preconds': [
                'boat at North port'
            ],
            'add': [
                'boat in lake',
            ],
            'delete': [
                'boat at North port'
            ]
        },
        {
            'action': 'boat moves to middle of lake',
            'preconds': [
                'boat at South port'
            ],
            'add': [
                'boat in lake',
            ],
            'delete': [
                'boat at South port'
            ]
        },

        {
            'action': 'boat moves to South port',
            'preconds': [
                'boat in lake'
            ],
            'add': [
                'boat at South port',
            ],
            'delete': [
                'boat in lake'
            ]
        },
        {
            'action': 'boat moves to North port',
            'preconds': [
                'boat in lake'
            ],
            'add': [
                'boat at North port',
            ],
            'delete': [
                'boat in lake'
            ]
        },
        {
            'action': 'cat boards boat',
            'preconds': [
                'boat at North port'
            ],
            'add': [
                'cat on board',
            ],
            'delete': [
                'no cat on board'
            ]
        },

        {
            'action': 'cat boards boat',
            'preconds': [
                'boat at South port'
            ],
            'add': [
                'cat on board',
            ],
            'delete': [
                'no cat on board'
            ]
        },
        {
            'action': 'cat jumps over board',
            'preconds': [
                #switch order of these two preconditions and the problem can be solved
                'boat in lake', 'cat on board'
            ],
            'add': [
                'no cat on board', 'cat in lake'
            ],
            'delete': [
                'cat on board'
            ]
        },
    ]
}


if __name__ == '__main__':

    # This turns on detailed logging for the GPS "thought" process.
    logging.basicConfig(level=logging.DEBUG)

    # Use GPS to solve the problem formulated above.
    actionSequence = gps(
        problem['initial'],
        problem['goal'],
        problem['actions']
    )

    # Print the solution, if there is one.
    if actionSequence is not None:
        for action in actionSequence:
            print(action)
    else:
        print('plan failure...')
