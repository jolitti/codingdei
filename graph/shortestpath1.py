import sys
def eprint(*args):
    for a in args:
        sys.stderr.write(str(a))
        sys.stderr.write(" ")
    sys.stderr.write("\n")

#eprint(*[1,2,3,4])


from queue import PriorityQueue

def link(a,b,links):
    linkList = links.get(a,None)

    if linkList is None:
        links[a]=[b]
    else:
        links[a].append(b)
    """ if b not in links:
        links[b]=[a]
    else:
        links[b].append(a) """

def getWeight(a,b,weigths):
    if a==b: return 0
    return weigths[(a,b)]

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
        weigths[(a,b)] = w

    q = PriorityQueue()
    q.put((0,start))
    while not q.empty():
        eprint(q.queue)
        weigth, index = q.get()
        linkList = links.get(index,None)
        if linkList is not None:
            for x in linkList:
                if distances[x]<0:
                    newWeigth = weigth+getWeight(index,x,weigths)
                    q.put((newWeigth,x))
        if distances[index]<0:
            distances[index]=weigth
    
    #print(*distances)

    for i in range(queries):
        d = distances[int(input())]
        if d<=-1: d="Impossible"
        print(d)