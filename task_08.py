def multiply_numbers(inputs=None):
    if inputs is None:
        return None
    res = 1
    count=0
    for element in str(inputs):
        if element.isdigit():
            res *= int(element)
            count+=1
    if count==0:
        return None
    return res
print(multiply_numbers("ss"))