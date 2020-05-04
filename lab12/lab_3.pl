witch(X) :- burns(X).
burns(X) :- wood(X).
wood(X) :- floats(X).
floats(X) :- same_weight(duck, X).
same_weight(duck, lady).

% ? - witch(lady).
% true.

