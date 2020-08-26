class Solution:
    def simplifyPath(self, path: str) -> str:
        commands = list(filter(bool, path.split('/')))
        st = []
        for c in commands:
            if c == '..':
                if st: st.pop()
            elif c != '.': st.append(c)
        return '/' + '/'.join(st)