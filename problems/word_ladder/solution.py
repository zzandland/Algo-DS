class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        wordDic = {}
        for word in wordList:
            for i in range(len(word)):
                tmp = word[:i] + "*" + word[i+1:]
                if tmp not in wordDic:
                    wordDic[tmp] = []
                wordDic[tmp].append(word)
        q = (collections.deque(), collections.deque())        
        q[0].append(beginWord)
        q[1].append(endWord)    
        wordSet.remove(endWord)
        l = [0, 1]
        while len(q[0]) > 0 or len(q[1]) > 0:
            for i in range(2):
                l[i] += 1
                for j in range(len(q[i])):
                    word = q[i].popleft()
                    for k in range(len(word)):
                        tmp = word[:k] + "*" + word[k+1:]
                        if tmp in wordDic:
                            for match in wordDic[tmp]:
                                if match in q[(i + 1) % 2]:
                                    return l[0] + l[1]
                                if match in wordSet:
                                    q[i].append(match)
                                    wordSet.remove(match)
                        wordDic.pop(tmp, None)            
        return 0                