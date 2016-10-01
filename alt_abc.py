def get_edge(word1, word2):
    for c in xrange(min(len(word1), len(word2))):
        if word1[c] != word2[c]:
            return (word1[c], word2[c])
    return None


def get_graph(words):
    graph = dict()
    for i in xrange(len(words) - 1):
        edge = get_edge(words[i], words[i + 1])
        if edge:
            if edge[0] not in graph:
                graph[edge[0]] = set()
            if edge[1] not in graph:
                graph[edge[1]] = set()
            graph[edge[0]].add(edge[1])
    return graph


def answer(words):
    graph = get_graph(words)

    destinations = set()
    for e_set in graph.values():
        destinations = destinations.union(e_set)

    roots = set()
    for v in graph:
        if v not in destinations:
            roots.add(v)

    visited = set()
    result = []
    def dfs(vertex):
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            for dest in graph[vertex]:
                dfs(dest)

    return "".join(result)

print answer(["y", "z", "xy"])
