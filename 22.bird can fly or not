can_fly(crow).
can_fly(sparrow).
can_fly(eagle).
cannot_fly(penguin).
cannot_fly(ostrich).

% Predicate to check if a bird can fly
fly_ability(Bird) :-
    can_fly(Bird),
    write(Bird), write(' can fly!').

fly_ability(Bird) :-
    cannot_fly(Bird),
    write(Bird), write(' cannot fly.').
