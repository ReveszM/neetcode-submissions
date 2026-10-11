from collections import deque



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
        noCycle = set()
        visited = set()

        def dfs(curNode):
            if curNode in visited:
                return False
            if curNode in noCycle:
                return True

            visited.add(curNode)
            for neighbor in graph[curNode]:
                if not dfs(neighbor):
                    return False
            visited.remove(curNode)
            noCycle.add(curNode)
            return True

        for i in range(numCourses):
            if i not in noCycle:
                if not dfs(i):
                    return False

        return True