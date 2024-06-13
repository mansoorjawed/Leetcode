---
tags:
  - easy
  - accepted
  - leetcode75
---
# Problem Description
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.


Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.

# Solutions
### Loop solution: O(n)
```python
def mergeAlternately(self, word1, word2):
	"""
	The solution provided first adds letters from each word alternating
	between the two words iterating as much as the shortest word and then
	adds the rest of the longer word to the tail of the result once all 
	letters of the shorter word are done.
	e.g. if word1 = "abc", word2 = "123456"
	Iterate until word1: result -> a1b2c3
	Add rest of word2: a1b2c3456
	
	:type word1: str
	:type word2: str
	:rtype: str
	"""
	# Final variable for building the array
	final = "" 
	# Find the minimum length among the two words
	minLength = min(len(word1), len(word1))
	# Iterate through the words minLnegth times
	for i in range(minLength):
		final += word1[i:i+1] + word2[i:i+1]
		
	# Add rest of the longer word
	if(minLength == len(word1)):
		final += word2[minLength:]
		
	return final
```

### Recursion solution for Fun
Ended up being slower 
```python

def mergeAlternately(self, word1, word2):
	"""
	:type word1: str
	:type word2: str
	:rtype: str
	""" 
	return word1[:1] + word2[:1] + firstLetters(word1[1:], word2[1:])

def firstLetters(word1, word2):
	# If there are no letters left in word1, return rest of word2
	if(not word1):
		return word2
		
	# If there are no letters left in word2, return rest of word1
	if (not word2):
		return word1
		
	#Otherwise return first letters of both words + rest of the word
	return word1[:1] + word2[:1] + firstLetters(word1[1:], word2[1:])
```