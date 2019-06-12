class Solution:
    num_dic = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }    

    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        if len(digits) == 0 or digits.find('1') != -1:
            return output
        self.DFS(digits, "", output, 0)
        return output
    
    def DFS(self, nums:str, tmp:str, output: List[str], i: int) -> None:
        if i >= len(nums):
            output.append(tmp[:])
            return
        for letter in self.num_dic[nums[i]]:
            self.DFS(nums, tmp + letter, output, i + 1)