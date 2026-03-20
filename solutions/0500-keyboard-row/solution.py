class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        # Define the three keyboard rows as sets
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        result = []
        
        for word in words:
            # Convert word to lowercase set for comparison
            word_set = set(word.lower())
            
            # Check if the word's characters are a subset of any single row
            if word_set <= row1 or word_set <= row2 or word_set <= row3:
                result.append(word)
                
        return result

