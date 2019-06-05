class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        q = collections.deque()
        q.append(beginWord)
        word_dic = collections.defaultdict(list)  
        for word in wordList:
            for i in range(len(word)):
                word_dic[word[:i] + "*" + word[i+1:]].append(word)
        output = 0
        while len(q) > 0:
            output += 1
            k = len(q)
            for i in range(k):
                curr = q.popleft()
                for j in range(len(curr)):
                    tmp = curr[:j] + "*" + curr[j+1:]
                    for match in word_dic[tmp]:
                        if match == endWord:
                            return output + 1
                        if match in word_set:
                            q.append(match)
                            word_set.remove(match)
                    word_dic[tmp] = []
        return 0                