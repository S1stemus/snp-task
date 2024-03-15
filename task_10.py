import re 
from collections import Counter
def count_words(string):
    string = string.lower()
    list_words = re.split(r'[,-;:,.?!" ]', string)
    list_words = list(filter(lambda x: x != '', list_words))
    result=Counter(list_words)

    return dict(result)
print(count_words("A man, a plan, a canal -- Panama"))