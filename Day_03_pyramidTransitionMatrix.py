from typing import List
from collections import defaultdict
# this is my solution

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        trans = defaultdict(list)
        for rule in allowed:
            trans[rule[:2]].append(rule[2])

        def dfs(row):
            if len(row) == 1:
                return True
            def build_next(i, curr):
                if i == len(row) - 1:
                    return dfs(curr)

                pair = row[i:i+2]
                if pair not in trans:
                    return False

                for ch in trans[pair]:
                    if build_next(i + 1, curr + ch):
                        return True
                return False

            return build_next(0, "")

        return dfs(bottom)
    
