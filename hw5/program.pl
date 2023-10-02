sum_list([], 0).
sum_list([C|T], Sum) :-
    sum_list(T, Sum1), Sum is Sum1 + C.

:- initialization(write('Сумма элементов списка: ')).
