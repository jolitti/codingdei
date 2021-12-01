# Debug su standard error, ignorato da kattis
import sys
def eprint(*args):
    for a in args:
        sys.stderr.write(str(a))
        sys.stderr.write(" ")
    sys.stderr.write("\n")


from queue import PriorityQueue

# Aggiungi b alla lista dei contatti di a nel dizionario list
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

# Originariamente scritto per l'implementazione
# con frozenset
def getWeight(a,b,weigths):
    if a==b: return 0
    return weigths[(a,b)]

# Main
while True:
    n,m,queries,start = map(int,input().split())
    if n<=0: break

    distances = [-1]*n
    distances[start] = 0

    links = {}
    weigths = {}
    visited = set() # Nodi già visitati nell'algoritmo

    #Inserimento collegamenti
    for i in range(m):
        a,b,w = map(int,input().split())
        link(a,b,links)
        weigths[(a,b)] = w

    # Iterazione algoritmo di dijkstra
    q = PriorityQueue()
    q.put((0,start))
    while not q.empty():
        # Visualizzazione stato attuale della queue
        eprint(q.queue)
        weigth, index = q.get()
        linkList = links.get(index,None)
        if linkList is not None:
            for x in linkList:
                if x not in visited:
                    visited.add(x)
                    newWeigth = weigth+getWeight(index,x,weigths)
                    q.put((newWeigth,x))
        if distances[index]<0:
            distances[index]=weigth
    
    # Ora che le distanze sono state precomputate,
    # rispondiamo alle query
    eprint(*distances)

    for i in range(queries):
        d = distances[int(input())]
        if d<=-1: d="Impossible"
        print(d)