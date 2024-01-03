reverse_list(Xs, Ys) :-
reverse_list(Xs, [], Ys).

reverse_list([], A, A).
reverse_list([H|T], R, A) :-
reverse_list(T, [H|R], A).

main:- 
read(Std_in),
  reverse_list(Std_in, Std_out),
  write(Std_out).
