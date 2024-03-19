def combine_anagrams(words_array):
    anagram_dict = {}   
    for word in words_array:
        sorted_word = str(sorted(word.lower()))
        if sorted_word in list(anagram_dict.keys()):
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    
    return list(anagram_dict.values())

# Пример использования
anagrams = combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
"creams", "scream"])
print(anagrams)
