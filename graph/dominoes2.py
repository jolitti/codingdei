cases = int(input())
tiles = []
chained = {}

def knock(i:int):
    tiles[i] = True
    if i in chained:
        for t in chained[i]:
            if not tiles[t]:
                knock(t)


for case in range(cases):
    n, m, l = map(int,input().split())
    tiles = [False]*n
    chained = {}
    
    for i in range(m):
        a,b = map(int,input().split())
        a,b = a-1,b-1

        if a not in chained:
            chained[a] = [b]
        else:
            chained[a].append(b)
    
    for j in range(l):
        knock(int(input())-1)

    print(tiles.count(True))

        

