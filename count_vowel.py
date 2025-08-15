def get_count(sentence):
    sentence = sentence.lower().strip()
    count = 0
    for i in sentence:
        if i in ["a","e","i","o","u"]:
            count += 1
        
    return count
