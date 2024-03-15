def coincidence(lst=None, r=None):
    if lst is None or r is None:
        return []
    res=[]
    for element in lst:
        if element in r:
            res.append(element)
    return res
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))