% Exercise 3.2
inside(katarina, olga).
inside(olga, natasha).
inside(natasha, irina).

in(X, Y):- inside(X,Y).
in(X,Y):- inside(X,Z), in(X,Z).

% Exercise 4.5

   tran(eins,one).
   tran(zwei,two).
   tran(drei,three).
   tran(vier,four).
   tran(fuenf,five).
   tran(sechs,six).
   tran(sieben,seven).
   tran(acht,eight).
   tran(neun,nine).

listtran([], []).
listtran([X|T1], [Y|T2]) :-
    tran(X, Y),
    listtran(T1, T2).

/*
Yes, prolog uses a verision of modus ponens.
It relies on rules of inference where P impplies Q, so if P is true then Q must be true.
This can be seen in prior examples where we saw that harry had a wand and a broom and someone who
has a wand and a broom is a wizard. Therefore we were able to know through inference that harry is a wizard.
*/