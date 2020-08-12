from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for path in paths:
            dir_, files = path.split(' ', 1)
            for file in files.split(' '):
                name, content = file.split('(')
                dic[content[:-1]].append(dir_ + '/' + name)
        return filter(lambda x: len(x) > 1, dic.values())