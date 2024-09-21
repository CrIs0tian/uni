def flat(a):
    res = []
    for x in a:
        if type(x) in (int, float, str, bool):
            res.append(x)
        else:
            temp = flat(x)
            res.extend(temp)
    return res


prova = [0, 2, [2, 4, [4, 4], 3, 5], [5, 7], 5, 4]
a = 0


res = flat(prova)
print(res)
