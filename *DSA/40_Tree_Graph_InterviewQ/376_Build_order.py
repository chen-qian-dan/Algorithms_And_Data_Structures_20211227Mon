"""
projects = ["a", "b", "c", "d", "e", "f"]
dependencies: [("a", "b"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]
"""

projects = ["a", "b", "c", "d", "e", "f"]
dependencies = [("a", "b"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]

def getDependencies(dependencies):
    s = set()
    for t in dependencies:
        s.add(t[1])
    return list(s)

def getInDependencies(projects, dependNodes):
    projectSet = set(projects)
    dependNodeSet = set(dependNodes)
    return list(projectSet - dependNodeSet)


def buildOrder(projects, dependencies): # expect ['e', 'f', 'a', 'b', 'd', 'c']
    """
    suppose m projects, n dependencies
    """
    orders = list()

    while projects:

        dependNodes = getDependencies(dependencies) # O(n)

        indepenNodes = getInDependencies(projects, dependNodes) # O(m)
        if len(indepenNodes) == 0:
            raise ValueError("The is a cycle")
        orders.extend(indepenNodes) # O(m - n)
        newProjects = list(set(projects) - set(indepenNodes)) # O(m - n)
        for t in dependencies:     # O(n * (m - n))
            if t[0] in indepenNodes:
                dependencies.remove(t)
        projects = newProjects

    return orders


print(buildOrder(projects, dependencies))

