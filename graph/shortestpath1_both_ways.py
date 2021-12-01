from queue import PriorityQueue

def link(a,b,links):
    if a not in links:
        links[a]=[b]
    else:
        links[a].append(b)
    if b not in links:
        links[b]=[a]
    else:
        links[b].append(a)

def getWeight(a,b,weigths):
    if a==b: return 0
    return weigths[frozenset([a,b])]

while True:
    n,m,queries,start = map(int,input().split())
    if n<=0: break

    distances = [-1]*n
    distances[start] = 0

    links = {}
    weigths = {}

    for i in range(m):
        a,b,w = map(int,input().split())
        link(a,b,links)
        weigths[frozenset([a,b])] = w

    q = PriorityQueue()
    q.put((0,start))
    while not q.empty():
        weigth, index = q.get()
        for x in links[index]:
            if distances[x]<0:
                newWeigth = weigth+getWeight(index,x,weigths)
                q.put((newWeigth,x))
        if distances[index]<0:
            distances[index]=weigth
    
    #print(*distances)

    for i in range(queries):
        print(distances[int(input())])