def is_reciprocal(graph, source, destination, k):
    if k == 0:
        if destination == source:
            return True
        return False
    if source in graph[destination]:
        return True
    for node in graph[destination]:
        if is_reciprocal(graph, source, node, k - 1):
            return True
    return False


def compute_ranks(graph):
    d = 0.8  # damping factor
    numloops = 10  # number of times through relaxation

    ranks = {}
    # Initialize ranks
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages

    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            rank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    if not is_reciprocal(graph, node, page, k):
                        rank += d * ranks[node] / len(graph[node])
            newranks[page] = rank
        ranks = newranks
    return ranks
