#You are given a list of n integers that can be positive, negative, or 0. 
#Find a subset of the elements that maximizes the product of the elements of the subset. 
#For example, when given the list [0,-2,4,1], there are 2 possible optimal solutions: 
#[4,1] and [4] (either is fine).

def max_subset(list):
    total = 0
    for item in list:
        if item > 0:
            total += item
    return total

print(max_subset(range(-10,5)))