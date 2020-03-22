from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dic = collections.defaultdict(list)
        for to,fro in sorted(tickets)[::-1]:
            dic[to].append(fro)
        print(dic)    
        route = []
        def visit(airport):
            while dic[airport]:
                visit(dic[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]