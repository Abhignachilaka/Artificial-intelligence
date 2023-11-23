food(nuts, protein, high).
food(fish, omega3, high).
food(vegetables, fiber, high).
food(fruits, vitamins, high).
food(red_meat, saturated_fat, high).

% Rules to suggest a diet based on a specific disease
suggest_diet(Disease, Diet) :-
    (Disease == diabetes ->
        Diet = [vegetables, fruits]
    ; Disease == heart_disease ->
        Diet = [fish, vegetables, fruits]
    ; Disease == obesity ->
        Diet = [vegetables, fruits, nuts]
    ; % Default diet for unknown diseases
        Diet = [vegetables, fruits]
    ).
