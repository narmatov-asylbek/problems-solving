# [List-of String] Integer -> [List-of String]
# Returns the top Frequent words from String
def top_k_words(words: list[str], k: int) -> list[str]:
    mapper = dict()
    
    for word in words:
        mapper[word] = mapper.get(word, 0) + 1
    
    
    frequents = [(word, val) for word, val in mapper.items()]
    frequents.sort(key=Comparator, reverse=True)
    return list(map(lambda x: x[0], frequents[:k]))


print(top_k_words(["i","love","leetcode","i","love","coding"], 2))
print(top_k_words(["the","day","is","sunny","the","the","the","sunny","is","is"], 4))
print(top_k_words(["the","day","is","sunny","the","the","the","sunny","is","is"], 4))