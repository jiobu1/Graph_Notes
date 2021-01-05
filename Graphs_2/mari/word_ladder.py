"""
Given two words(begin_word and end_word), and a dictionary's word list,
return the shortest transformation sequence from begin_word to end_word, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not a transformed word.

Note:
Return [] if there is not such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assum begin_word and end_word are non-empty and are not the same.

Sample:
begin_word = "hit"
end_word = "cog"
return: ["hit", "hot", "cot", "cog"]

begin_word = "sail"
end_word = "boat"
return: ["sail", "bail", "boil", "bolt", "boat"]

beginWord = "hungry"
endWord = "happy"
[]

Plan
1. translate into graph terminology
nodes = beginWord, endWord
edges = path to words
weights = none
2. build your graph if needed
3. Traverse your graph
BFT
"""
from collections import deque

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def findLadder(beginWord, endWord, wordList):
    words = set(wordList)
    visited = set()
    queue = deque()
    queue.append([beginWord])
    while len(queue) > 0:
        currPath = queue.popleft()
        currWord  = currPath[-1]
        if currWord in visited:
            continue
        visited.add(currWord)
        if currWord == endWord:
            return currPath
        for i in range(len(currWord)):
            for letter in alphabet:
                transformedWord = currWord[:i] + letter + currWord[i + 1:]
                if transformedWord in words:
                    newPath = list(currPath)
                    newPath.append(transformedWord)
                    queue.append(newPath)

        return None


print(findLadder("hot", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) # ["hit", "hot", "dot", "dog", "cog"]
print(findLadder("hit", "cog", ["hot", "dot", "dog", "lot", "log"])) # []
