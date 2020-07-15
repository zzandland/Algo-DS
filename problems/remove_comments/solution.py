class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        bb = False
        res, tmp = [], []
        for line in source:
            i = 0
            while i < len(line):
                if bb:
                    k = line.find('*/', i)
                    if k != -1:
                        i = k+2
                        bb = False
                    else:    
                        i = len(line)
                else:
                    j, k = line.find('//', i), line.find('/*', i)
                    if j != -1 and k != -1:
                        if j < k:
                            tmp.append(line[i:j])
                            i = len(line)
                            break
                        else:
                            tmp.append(line[i:k])
                            i = k+2
                            bb = True
                    elif j != -1:
                        tmp.append(line[i:j])
                        i = len(line)
                        break
                    elif k != -1:
                        tmp.append(line[i:k])
                        i = k+2
                        bb = True
                    else:
                        tmp.append(line[i:])
                        i = len(line)
            if not bb and tmp:
                after = ''.join(tmp)
                if after: res.append(after)
                tmp = []
        return res