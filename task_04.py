def sort_list(lst):
    if len(lst)==0:
        return []
    maxnum=max(lst)
    minnum=min(lst)
    minindex=[i for i, j in enumerate(lst) if j == minnum]
    maxindex=[i for i, j in enumerate(lst) if j == maxnum]
    for i in minindex:
        lst[i]=maxnum
    for i in maxindex:
        lst[i]=minnum
    lst.append(minnum)
    return lst
list=[1, 2, 1, 3]
print(sort_list([1]))


