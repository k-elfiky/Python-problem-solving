#   return the sum of all even numbers in a given list

def sum_even(n):
    count = 0
    for i in n:
        if i % 2 == 0:
            count = count + i
    return count

print(sum_even([1,2,3,4,5,6,7,8]))