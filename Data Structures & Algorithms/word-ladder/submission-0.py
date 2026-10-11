from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        elif beginWord == endWord:
            return 1

        expandedWordList = list(wordList)
        expandedWordList.append(beginWord)
        
        adjacencyList = defaultdict(list)
        for start in expandedWordList:
            for end in expandedWordList:
                n = 0
                for i in range(len(start)):
                    if start[i] != end[i]:
                        n += 1
                if n == 1:
                    adjacencyList[start].append(end)

        result = 0
        added = set()
        todo = deque()
        added.add(start)
        todo.append(start)
        while len(todo) > 0:
            result += 1
            for i in range(len(todo)):
                cur = todo.popleft()
                if cur == endWord:
                        return result
                for neighbor in adjacencyList[cur]:
                    if neighbor not in added:
                        todo.append(neighbor)
                        added.add(neighbor)
        return 0

        