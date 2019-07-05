class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        cut = S.replace('-', '').upper()
        counter = 1
        for i in range(len(cut))[::-1]:
            if i > 0 and counter == K:
                cut = cut[:i] + '-' + cut[i:]
                counter = 0
            counter += 1    
        return cut    