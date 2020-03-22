class Solution:
    def validIPAddress(self, IP: str) -> str:
        def isIPv4(IP: str) -> bool:
            split = IP.split('.')
            if len(split) != 4: return False
            for digit in split:
                if not digit.isnumeric() or str(int(digit)) != digit or int(digit) < 0 or int(digit) > 255:
                    return False
            return True
        
        def isIPv6(IP: str) -> bool:
            split = IP.split(':')
            if len(split) != 8: return False
            for seg in split:
                if len(seg) > 4 or not seg.isalnum(): return False
                try:
                    int(seg, 16)
                except ValueError:
                    print(seg)
                    return False
            return True    
        if isIPv4(IP): return 'IPv4'
        elif isIPv6(IP): return 'IPv6'
        else: return 'Neither'