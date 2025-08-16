Description:
What if we need the length of the words separated by a space to be added at the end of that same word and have it returned as an array?

Example(Input --> Output)

"apple ban" --> ["apple 5", "ban 3"]
"you will win" -->["you 3", "will 4", "win 3"]

----Solution----

def add_length(str_):
    str_ = str_.split()
    return [f"{i} {len(i)}" for i in str_]
