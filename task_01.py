def is_palindrome(word):
    word=str(word).lower()
    filterword=""
    alphabet=" !?.,'\"-:;"   
    for char in word:
        if char not in alphabet:
            filterword+=char
    for i in range(len(filterword)//2):
        if filterword[i]!=filterword[len(filterword)-i-1]:
            return False
    return True
print(is_palindrome(None))
    