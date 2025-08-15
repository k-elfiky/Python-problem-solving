import string


def find_missing_letter(givenValue):
    alpha = string.ascii_lowercase
    start = alpha.index(givenValue[0])
    stop = alpha.index(givenValue[-1])
    for letter in alpha[start:stop]:
          if letter not in givenValue:
               return letter
          
    return  "no missing values"
        
print(find_missing_letter("abcdeghi"))
print(find_missing_letter("defgi"))
print(find_missing_letter("xyz"))

