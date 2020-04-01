#  Given a list of reviews, a list of keywords and an integer k. Find the most popular k keywords in order of most to least frequently mentioned.

#  The comparison of strings is case-insensitive. If keywords are mentioned an equal number of times in reviews, sort alphabetically.

#  Example 1:

    #  Input:
        #  k = 2
        #  keywords = ["anacell", "cetracular", "betacellular"]
        #  reviews = [
          #  "Anacell provides the best services in the city",
          #  "betacellular has awesome services",
          #  "Best services provided by anacell, everyone should use anacell",
        #  ]

    #  Output:
        #  ["anacell", "betacellular"]

    #  Explanation:
        #  "anacell" is occuring in 2 different reviews and "betacellular" is only occuring in 1 review.

#  Example 2:

    #  Input:
        #  k = 2
        #  keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
        #  reviews = [
          #  "I love anacell Best services; Best services provided by anacell",
          #  "betacellular has great services",
          #  "deltacellular provides much better services than betacellular",
          #  "cetracular is worse than anacell",
          #  "Betacellular is better than deltacellular.",
        #  ]

    #  Output:
        #  ["betacellular", "anacell"]

    #  Explanation:
        #  "betacellular" is occuring in 3 different reviews. "anacell" and "deltacellular" are occuring in 2 reviews, but "anacell" is lexicographically smaller.

import collections
import heapq

#  def topKFrequentKeywords(k, keywords, reviews):
    #  d = defaultdict(int)
    #  key, rev = [k.lower() for k in keywords], [r.lower() for r in reviews]
    #  for review in rev:
        #  for keyword in key:
            #  if review.find(keyword) != -1:
                #  d[keyword] += 1
    #  freq = defaultdict(list)
    #  for key, val in d.items():
        #  freq[val].append(key)
    #  output, i = [], 0
    #  for _, words in sorted(freq.items(), reverse = True):
        #  for word in words:
            #  output.append(word)
            #  i += 1
            #  if i == k:
                #  return output

class Ele:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word < other.word
        return self.freq > other.freq

def topKFrequentKeywords(k, keywords, reviews):
    wordLists = []
    for review in reviews:
        wordLists += set(review.lower().split())
    count = collections.Counter(wordLists)
    hp = []
    for word, freq in count.items():
        if word in keywords:
            heapq.heappush(hp, Ele(word, freq))
            if len(hp) > k:
                heapq.heappop(hp)
    return [heapq.heappop(hp).word for _ in range(k)][::-1]

keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
"Anacell provides the best services in the city",
"betacellular has awesome services",
"Best services provided by anacell, everyone should use anacell",
]

#  keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
#  reviews = [
#  "I love anacell Best services; Best services provided by anacell",
#  "betacellular has great services",
#  "deltacellular provides much better services than betacellular",
#  "cetracular is worse than anacell",
#  "Betacellular is better than deltacellular.",
#  ]

print(topKFrequentKeywords(2, keywords, reviews))
