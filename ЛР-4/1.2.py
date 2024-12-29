def two_sum(lst, target):
    pairs = (len(lst), len(lst))
    for i in range(len(lst)):
        if ((target - lst[i]) in lst and (i, lst.index(target - lst[i])) < pairs):
                pairs = (i, lst.index(target - lst[i]))
    return pairs

lst = list(range(1,10))
target = 8
result = two_sum(lst, target)
print(result)