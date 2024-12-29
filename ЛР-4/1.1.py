def two_sum(lst, target):
    pairs = (len(lst), len(lst))
    for i in range(len(lst)):
        for j in range(len(lst)):
            if (lst[i] + lst[j] == target and (i, j) < pairs):
                pairs = (i, j)
    return pairs

lst = list(range(1,10))
target = 8
result = two_sum(lst, target)
print(result)