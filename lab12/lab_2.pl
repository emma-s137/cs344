/*
Exercise 2.1
1. bread  =  bread -yes
2. 'Bread' = bread -no
8. food(X)  =  food(bread) - yes, X = bread
9. food(bread,X)  =  food(Y,sausage) - yes, Y = bread, X = sausage
14. meal(food(bread),X)  =  meal(X,drink(beer)) - no

Exercise 2.2
*/
house_elf(dobby).
witch(hermione).
witch('McGonagall').
witch(rita_skeeter).
magic(X):-  house_elf(X).
magic(X):-  wizard(X).
magic(X):-  witch(X).

/*

Unfication works by taking the query and looking at the conditions for it to be true
the propositions will then be evaluated with the first correct atom and the rest of the propositions will
then be checked to see if this is right. The atom will return true or nnce an error has been found the program
will go back and pick another atom to test.
?-  magic(house_elf).  - false, because house_elf is not an atom.
?-  wizard(harry).     - false, because that attribute is never defined.
?-  magic(wizard).     - false, because the attribute is not defined and if it was still false because it would not be an atom
?-  magic(’McGonagall’).- true, (if you comment out magic(X):- wizrd(X) rule otherwise there is a syntax error)
?-  magic(Hermione).   - Hermione = dobby; Hermione = hermione ; Hermione = 'McGonagall'; Hermione = rita_skeeter
 as Hermione is a variable not an atom in this instance because it's capitalized

part b

Inference does use unification in propositional logic, as certain conditions will be identified together
as being true to arrive at a larger conclusion.

part c

Prolog does use resolution as the program finds several propositions to be true for an atom, and uses that
to make an inference.
*/