parent(john, jim).
parent(john, ann).
parent(susan, jim).
parent(susan, ann).
parent(jim, tom).
parent(ann, lisa).

% Rules to define different relationships
father(Father, Child) :-
    parent(Father, Child),
    male(Father).

mother(Mother, Child) :-
    parent(Mother, Child),
    female(Mother).

sibling(Sibling1, Sibling2) :-
    parent(Parent, Sibling1),
    parent(Parent, Sibling2),
    Sibling1 \= Sibling2.
