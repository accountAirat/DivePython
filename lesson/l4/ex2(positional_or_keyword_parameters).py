def func(positional_only_parameters, /, positional_or_keyword_parameters, *, keyword_only_parameters):
    pass

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)  # Принт внутри функции не использовать


combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
