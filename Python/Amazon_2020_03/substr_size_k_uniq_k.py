#  Example 1:

#  Input:
#  s = "abcabc"
#  k = 3
#  Output: ["abc", "bca", "cab"]
#  Example 2:

#  Input:
#  s = "abacab"
#  k = 3
#  Output: ["bac", "cab"]
#  Example 3:

#  Input:
s = "awaglknagawunagwkwagl"
k = 4
#  Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
#  Explanation:
#  Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag", "wagl"
#  "wagl" is repeated twice, but is included in the output once.
#  Constraints:

#  The input string consists of only lowercase English letters [a-z]
#  0 <= k <= 26

def substrSizeKUniqK(s, k):
    l, r, cnt, seen, output = 0, k, {}, set(), []
    for i in range(r-1):
        if s[i] not in cnt:
            cnt[s[i]] = 0
        cnt[s[i]] += 1
    while r <= len(s):
        print(l, r)
        sl, sr = s[l], s[r-1]
        if sr not in cnt:
            cnt[sr] = 0
        cnt[sr] += 1
        if len(cnt.keys()) == k:
            if s[l:r] not in seen:
                seen.add(s[l:r])
                output.append(s[l:r])
        cnt[sl] -= 1
        if cnt[sl] == 0: del cnt[sl]
        l += 1
        r += 1
    return output

print(substrSizeKUniqK(s, k))
