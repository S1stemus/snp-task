import sys
def max_odd(arr=[]):
    max=-sys.maxsize-1
    for element in arr:
        if isinstance(element,(int,float)) and element>max:
            max=element
    if max==-sys.maxsize-1:
        return None
    else:
        return max
print(max_odd(['ololo', 'fufufu']))