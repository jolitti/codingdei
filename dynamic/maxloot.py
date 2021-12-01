resultCache = {}

def maxKnap(index:int,capacity:int) -> int:
    cached = resultCache.get((index,capacity),None)
    if cached is not None: 
        #print("Cache hit")
        return cached

    if index<=0 or capacity<=0: ans = 0
    elif weigths[index]>capacity: ans = maxKnap(index-1,capacity)
    else: ans = max(maxKnap(index-1,capacity),maxKnap(index-1,capacity-weigths[index])+values[index])
    
    resultCache[(index,capacity)]=ans
    return ans

""" cases = int(input())
for i in range(cases):
    objNum, cap = map(int,input().split())
    values = list(map(int,input().split()))
    weigths = list(map(int,input().split()))
    
    print(maxKnap(objNum-1,cap))
    resultCache = {} """

from random import randrange
maxCap = 2000000000
for i in range(20):
    values = [randrange(1,100000000) for x in range(20)]
    weigths = [randrange(1,100000000) for x in range(20)]
    cap = randrange(1,maxCap)

    for i in range(19):
        maxKnap(i,cap)
    print(maxKnap(19,randrange(1,cap)))

    resultCache = {}

values = [5,2,4,1,1,4,5,2,3]
weigths = [6,2,1,2,4,2,1,3,1]
print(maxKnap(3,6))

resultCache = {}

values = [1,3,2,3,1,1,3,2,4,2]
weigths = [1,2,2,1,1,2,3,1,2,2]
print(maxKnap(9,5))