edge(a, b, 2).
edge(a, c, 1).
edge(b, d, 3).
edge(c, e, 4).
edge(d, goal, 5).
edge(e, goal, 2).

% Best-First Search algorithm
best_first_search(Start, Goal, Path) :-
    best_first_search_helper([node(Start, 0, heuristic(Start, Goal))], Goal, [Start], Path).

best_first_search_helper([node(Goal, Cost, _)|_], Goal, Path, [Goal|Path]) :-
    reverse([Goal|Path], FinalPath),
    write('Path found: '), write(FinalPath), nl,
    write('Cost: '), write(Cost), nl.

best_first_search_helper([node(Current, CurrentCost, _)|Rest], Goal, Path, FinalPath) :-
    findall(node(Next, NewCost, heuristic(Next, Goal)),
            (edge(Current, Next, StepCost), \+ member(Next, Path),
            NewCost is CurrentCost + StepCost),
            NextNodes),
    append(NextNodes, Rest, UpdatedQueue),
    sort_queue(UpdatedQueue, SortedQueue),
    best_first_search_helper(SortedQueue, Goal, [Current|Path], FinalPath).

% Utility predicate to sort the queue based on heuristic values
sort_queue(Queue, SortedQueue) :-
    predsort(compare_nodes, Queue, SortedQueue).

% Utility predicate to compare nodes based on heuristic values
compare_nodes(Order, node(_, _, H1), node(_, _, H2)) :-
    compare(Order, H1, H2).
