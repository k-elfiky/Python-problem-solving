def remove_char_from(word : str, c, C):
    word = word.replace(f"{c}" , "")
    word = word.replace(f"{C}" , "")
    return word.strip()

print(remove_char_from("ElddzeroDd webdd ddschool", "d","D"))
print(remove_char_from("ElxzeroX Web Sxchool", "x", "X"))


