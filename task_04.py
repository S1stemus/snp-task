def sort_list(lst):
    if len(lst)==0:
        return []
    maxnum=max(lst)
    minnum=min(lst)
    lst.remove(max(lst))
    lst.remove(min(lst))
    res=[]
    res.append(maxnum)
    for element in lst:
        res.append(element)
    res.append(minnum)
    res.append(minnum)
    return res
print(sort_list([]))


