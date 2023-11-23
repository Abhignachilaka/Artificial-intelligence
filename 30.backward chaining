bird(canary).
bird(robin).
mammal(dog).
mammal(cat).
flies(canary).
flies(robin).

% Rules
can_fly(X) :- bird(X), flies(X).
can_fly(X) :- pegasus(X).  % Assuming there's a mythical creature named pegasus.

% Backward Chaining Rules
is_bird(X) :- bird(X).
is_mammal(X) :- mammal(X).
is_bird_that_flies(X) :- is_bird(X), can_fly(X).
is_mammal_that_flies(X) :- is_mammal(X), can_fly(X).
