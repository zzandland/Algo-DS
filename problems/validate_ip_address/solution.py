class Solution:
    def validIPAddress(self, IP: str) -> str:
        def ipv4(ip: str) -> bool:
            s = ip.split('.')
            if len(s) != 4:
                return False
            for i in s:
                if not i.isdigit() or len(i) != len(str(int(i))) or not (0 <= int(i) < 256):
                    return False
            return True
        def ipv6(ip: str) -> bool:
            s = ip.split(':')
            if len(s) != 8:
                return False
            for i in s:
                if not (1 <= len(i) < 5) or not all([c in string.hexdigits for c in i]):
                    return False
            return True    
        if ipv4(IP):
            return 'IPv4'
        if ipv6(IP):
            return 'IPv6'
        return 'Neither'