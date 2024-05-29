class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        #  Length less than three
        if (len(word) < 3):
            return False

        isVowel = False
        isConsonant = False
        digits = str([num for num in range(0, 10)])
        letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        vowels = ['a', 'e', 'i', 'o', 'u']
        for char in word:
            char = char.lower()
            if (not (char in digits) and not (char in letters)):
                return False

            if char.lower() in vowels:
                isVowel = True
            elif char.lower() in letters:
                isConsonant = True

        if (isVowel and isConsonant):
            return True

        return False
