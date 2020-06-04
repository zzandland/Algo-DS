class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        [fc.sort() for fc in favoriteCompanies]
        distincts, res, index = [], [], {tuple(fc): i for i, fc in enumerate(favoriteCompanies)}
        for fc in sorted(favoriteCompanies, key=len, reverse=True):
            distinct, sfc = True, set(fc)
            for s in distincts:
                if s & sfc == sfc:
                    distinct = False
                    break
            if distinct:
                res.append(index[tuple(fc)])
                distincts.append(sfc)
        return sorted(res)