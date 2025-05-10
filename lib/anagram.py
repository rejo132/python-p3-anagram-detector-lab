# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Store word in lowercase for case-insensitive comparison
    
    def match(self, candidates):
        # Sort letters of the stored word
        sorted_word = ''.join(sorted(self.word))
        # Return candidates whose sorted letters match, excluding the original word
        return [cand for cand in candidates if ''.join(sorted(cand.lower())) == sorted_word and cand.lower() != self.word]