/* Exercise 12.1
 part a.4

These first three are rules that require a simple statement.
1 butch is a killer
2 Mia and Marsellus are married
3 Zed is dead
These 3 are rules that a bit more complicated as the actions are often done to someone or something and conditional
on other preconditions.
4 Marsellus kills everyone who gives Mia a footmassage
5 Mia loves everyone who is a good dancer
6 Jules eats anything that is nutritious or tasty
*/

killer(butch).
married(mia, marsellus).
dead(zed).
kills(marsellus, Person):- footmassage(mia, Person).
loves(mia, Dancer):- gooddancer(Dancer).
ats(jules, Food):- tasty(Food) ;  nutritious(Food).

/* part a.5
Prolog looks through it's facts and rules to determine if the query given is true or false.
An attribute returns an undefined procdure if the program has never seen it before like witch.

1. true.
2. ERROR: undefined procedure
3. false.
4. ERROR: undefined procedure
5. true.
6. Y = ron ; Y = harry.
7. ERROR: undefined procedure

*/

/*
part b

Yes, prolog uses propositional logic to implement modulus ponens (inference rule).
One demonstration would be that it if you tell prolog
If it's raining it must be cloudy.
It's raining.
Then the program will infer that it is cloudy out.

part c
Propositional logic works where a statement is either true or false.
A horn clause represents an implication where either a set of conditions and then what we can infer from that
will be true or they will both be false.

part d
The TELL and the ASK are sperated as the things that are told are within the prolog file while the queries
made are what is asked using the rules and facts in the file.

*/
