class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        nums = ["0", "1", "6", "8", "9"]
        output = []
        buf = collections.deque()
        self.helper(buf, nums, n, output)
        return output
        
    def helper(self, buf: List, nums: List[str], n: int, output: List[str]) -> None:
        if len(buf) >= n:
            if n == 1 or buf[0] != "0":
                output.append(''.join(buf))
            return    
        for num in nums:
            if len(buf) == 0 and n % 2 == 1:
                if num != '6' and num != '9':
                    buf.append(num)
                    self.helper(buf, nums, n, output)
                    buf.pop()
            else:
                buf.appendleft(num)
                if num == '6':
                    buf.append('9')
                elif num == '9':
                    buf.append('6')
                else:    
                    buf.append(num)
                self.helper(buf, nums, n, output)
                buf.popleft()
                buf.pop()