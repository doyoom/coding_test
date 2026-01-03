def solution(edges):
    from collections import defaultdict
    in_deg = defaultdict(int)
    out_deg = defaultdict(int)
    nodes = set()
    for a, b in edges:
        out_deg[a] += 1
        in_deg[b] += 1
        nodes.add(a)
        nodes.add(b)
    created = 0
    stick = 0
    eight = 0
    for node in nodes:
        if in_deg[node] == 0 and out_deg[node] >= 2:
            created = node
            break
    for node in nodes:
        if node == created:
            continue
        if out_deg[node] == 0:
            stick += 1
        elif in_deg[node] >= 2 and out_deg[node] >= 2:
            eight += 1
    donut = out_deg[created] - stick - eight
    return [created, donut, stick, eight]
