fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(blueberry, blue).

% Predicate to find the color of a fruit using backtracking
fruit_color_backtrack(Fruit, Color) :-
    fruit_color(Fruit, Color).

fruit_color_backtrack(Fruit, Color) :-
    \+ fruit_color(Fruit, _),
    write('Color of '), write(Fruit), write(' is unknown.'), nl,
    Color = unknown.
