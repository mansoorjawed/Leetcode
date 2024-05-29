---
tags:
  - easy
---

## Problem:
https://leetcode.com/problems/valid-word/description/

A word is considered **valid** if:

- It contains a **minimum** of 3 characters.
- It contains only digits (0-9), and English letters (uppercase and lowercase).
- It includes **at least** one **vowel**.
- It includes **at least** one **consonant**.

You are given a string `word`.

Return `true` if `word` is valid, otherwise, return `false`.

**Notes:**

- `'a'`, `'e'`, `'i'`, `'o'`, `'u'`, and their uppercases are **vowels**.
- A **consonant** is an English letter that is not a vowel.

**Example 1:**

**Input:** word = "234Adas"

**Output:** true

**Explanation:**

This word satisfies the conditions.

**Example 2:**

**Input:** word = "b3"

**Output:** false

**Explanation:**

The length of this word is fewer than 3, and does not have a vowel.

**Example 3:**

**Input:** word = "a3$e"

**Output:** false

**Explanation:**

This word contains a `'$'` character and does not have a consonant.

**Constraints:**

- `1 <= word.length <= 20`
- `word` consists of English uppercase and lowercase letters, digits, `'@'`, `'#'`, and `'$'`.

```python
class Solution(object):  
    def isValid(self, word):  
        """  
        :type word: str        
        :rtype: bool  
        """        
        # Return False when length less than three  
        if (len(word) < 3):  
            return False  
  
        # Declare what is a letter or a digit as that is all that is allowed  
        digits = str([num for num in range(0, 10)])  
        letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]  
        vowels = ['a', 'e', 'i', 'o', 'u']  
        for char in word:  
            # make all characters lowercase
            char = char.lower()  

			# if not digit or letter, then special so return false
            if (not (char in digits) and not (char in letters)):  
                return False  

			# Check if its a vowel otherwise check if its a consonant
            if char in vowels:  
                isVowel = True  
            elif char in letters:  
                isConsonant = True  
		# If we saw vowels and consonants, return true as we already made sure no letters are special
        if (isVowel and isConsonant):  
            return True  
		# otherwise return false
        return False
```