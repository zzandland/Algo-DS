class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for path in paths:
            dir, files = path.split(' ', 1)
            for file in files.split(' '):
                name, content = file.split('(', 1)
                dic[content].append(dir + '/' + name)
        return [lst for lst in dic.values() if len(lst) > 1]