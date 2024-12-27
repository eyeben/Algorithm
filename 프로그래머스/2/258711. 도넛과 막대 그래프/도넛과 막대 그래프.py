from collections import defaultdict
def solution(edges):
    nodes = set()
    indegree = defaultdict(list)
    outdegree = defaultdict(list)
    
    for a,b in edges:
        nodes.add(a)
        nodes.add(b)
        indegree[b].append(a)
        outdegree[a].append(b)
        
    # 가짜 색출
    startNodes = []
    for itm in nodes:
        if itm not in indegree:
            startNodes.append(itm)
    bad = -1
    for itm in startNodes:
        if len(outdegree[itm]) > 1:
            bad = itm
            break
    if bad == -1:
        bad = startNodes[0]
    
    # 색출 후 재구성 
    nodes = set()
    indegree = defaultdict(list)
    outdegree = defaultdict(list)
    
    for a,b in edges:
        nodes.add(b)
        if a == bad:
            continue
        nodes.add(a)

        indegree[b].append(a)
        outdegree[a].append(b)
    
    startNodes = []
    for itm in nodes:
        if itm not in indegree:
            startNodes.append(itm)
    
    visitedNode = set()
    visitedEdge = set()

    # stick
    stick = len(startNodes)
    for itm in startNodes:
        node = itm
        visitedNode.add(node)
        while len(outdegree[node]) != 0:
            node = outdegree[node][0]
            visitedNode.add(node)
    
    # 8
    core = []
    for itm in nodes:
        if itm in visitedNode:
            continue
        if len(indegree[itm]) > 1:
            core.append(itm)
    loop = len(core)
    for itm in core:
        visitedNode.add(itm)
        node = outdegree[itm][0]
        while node not in visitedNode:
            visitedNode.add(node)
            node = outdegree[node][0]
        
        node = outdegree[itm][1]
        while node not in visitedNode:
            visitedNode.add(node)
            node = outdegree[node][0]
            
    # o
    circle = 0
    for itm in nodes:
        if itm in visitedNode:
            continue
        circle += 1
        
        visitedNode.add(itm)
        node = outdegree[itm][0]
        while node not in visitedNode:
            visitedNode.add(node)
            node = outdegree[node][0]
        

    return [bad, circle, stick, loop]