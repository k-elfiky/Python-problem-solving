sen = "hello its nice to meet youuuuuu"
count = 0
def longest_word(sentence):
    count = 0
    sentence = sentence.split(" ")
    for word in sentence:
        if len(word) > count:
            count = len(word)
            longest = word
    return longest
    

print(longest_word(sen))