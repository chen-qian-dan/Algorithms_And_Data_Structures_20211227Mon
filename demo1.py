# def create_graph(projects, dependencies):
#    project_graph = {}
#    for project in projects:
#        project_graph[project] = []
#    for pairs in dependencies:
#        project_graph[pairs[0]].extend(pairs[1])
#    return project_graph
# graph = create_graph(['A', 'B', 'C', 'D', 'E', 'F'], [('A','D'), ('F', 'B'), ('B','D'), ('F','A'), ('D','C')])
# print(graph)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        if len(s) <= 1:
            return len(s)
        
        arr = list(s)
        maxArr = list()
        
        j = -1
        visited = list()
        for i in range(len(arr)):
            if arr[i] not in visited:
                visited.append(arr[i])
            else:
                maxArr = visited[:] if len(visited) > len(maxArr) else maxArr
                j = visited.index(arr[i])
                if j == len(visited) - 1:
                    visited = list(arr[i])
                else:
                    visited = visited[j+1:]
                    visited.append(arr[i])
        maxArr = visited[:] if len(visited) > len(maxArr) else maxArr
        return len(maxArr)
                

print(Solution().lengthOfLongestSubstring(s = "dvdf"))