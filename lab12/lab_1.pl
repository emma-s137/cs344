-- Exercise 12.1
-- part a.4

-- 1 butch is a killer
killer(butch).

-- 2 Mia and Marsellus are married
married(mia, marsellus).

-- 3 Zed is dead
dead(zed).

-- 4 Marsellus kills everyone who gives Mia a footmassage

kills(marsellus, Person):- footmassage(mia, Person).

-- 5 Mia loves everyone who is a good dancer

loves(mia, Dancer):- gooddancer(Dancer).

-- 6. Jules eats anything that is nutritious or tasty

eats(jules, Food):- tasty(Food) ;  nutritious(Food).

/* part a.5


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



*/
