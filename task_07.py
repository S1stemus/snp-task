def combine_anagrams(words_array):
    anagram_dict = {}   
    for word in words_array:
        sorted_word = sorted(word.lower())
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    
    return list(anagram_dict.values())

# Пример использования
words = ['listen', 'silent', 'enlist', 'hello', 'world']
anagrams = combine_anagrams(words)
print(anagrams)
