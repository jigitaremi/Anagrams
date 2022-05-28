# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    # [assignment] Add your code here    
   
    word = word.upper()
    anagram = anagram.upper()
    
    if (sorted(word.upper())) != (sorted(anagram.upper())): 
        return False
        
    else: 
        return True
        
    
print(find_anagram("bore", "robe"))

print(find_anagram("mane", "name"))

print(find_anagram("love", "loaf"))

print(find_anagram("Lord", "Dorl"))

print(find_anagram("Conversationalists", "conservationalists"))


