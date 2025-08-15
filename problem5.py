def convert(n):
    n = str(n)
    num_list = []
    for i in n:
        i = int(i)
        num_list.append(i)
    num_list.reverse()
    return num_list
print(convert(1234567))
