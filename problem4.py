def remove_duplicate_words_from(sentence):
    sentence = sentence.split()
    new_sen = list(dict.fromkeys(sentence))
    return new_sen
print(remove_duplicate_words_from("hello iam hello kareem elfiky"))
