def connect_dicts(dict1, dict2):
    new_dict = {}
    
    keys1=list(dict1.keys())
    keys2=list(dict2.keys())
    
    for key in keys1:
        if key in keys2:
            if dict1[key]>dict2[key] and dict1[key]>=10:
                new_dict[key]=dict1[key]

            elif  dict2[key]>=10:
                new_dict[key]=dict2[key]
            keys2.remove(key)  
        else:
            if dict1[key]>=10:
                new_dict[key]=dict1[key]                         
    for key in keys2:
        if dict2[key]>=10:
            new_dict[key]=dict2[key]
    
    return dict(sorted(new_dict.items()))

# Пример использования
dict1 = {"a": 5, "b": 15, "c": 8}
dict2 = {"c": 10, "e": 12, "f": 20}
result = connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 })
print(result)