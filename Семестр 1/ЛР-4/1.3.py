from random import shuffle

def two_sum(lst, target):
    pairs = (len(lst), len(lst))
    for i in range(len(lst)):
        if ((target - lst[i]) in lst and (i, lst.index(target - lst[i])) < pairs):
                pairs = (i, lst.index(target - lst[i]))
    return pairs

def two_sum_hashed_all(lst, target):
    pairs = []
    for i in range(int(len(lst)/2)):
        if ((target - lst[i]) in lst and i != lst.index(target - lst[i]) and (lst.index(target - lst[i]), i) not in pairs):
                pairs.append((i, lst.index(target - lst[i])))
    return pairs

lst = list(range(1,100))
target = 8
result = two_sum_hashed_all(lst, target)
print(result)