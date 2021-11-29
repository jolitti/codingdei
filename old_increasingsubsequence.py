def insertBestSubSeq(seqs:list,newVal:int):
    if len(seqs)<=0: return [[newVal]]
    maxLen = max([len(x) for x in seqs])
    ans = []
    print(len(seqs))
    for s in seqs:
        if newVal > s[-1]:
            ans.append(s+[newVal])
        elif len(s)>1 and newVal > s[-2]:
            ans.append(s[:-1]+[newVal])
        elif newVal <= s[0]:
            ans.append([newVal])
            if len(s) > 1:
                ans.append(s)
        else:
            ans.append([x for x in s if x<newVal]+[newVal])
            ans.append(s)
    return ans

def findBestSubSeqs(l:list):
    arrayLen = len(l)
    ans = []
    for i,x in enumerate(l):
        #print(*ans)
        ans = insertBestSubSeq(ans,x)
    return ans

def filterMaxLen(l:list):
    lengths = [len(x) for x in l]
    maxLen = max(lengths)
    maxLengths = [x for x in l if len(x)==maxLen]
    #print(maxLengths)
    return maxLengths


""" while True:
    n = list(map(int,input().split()))
    if n[0]==0: break

    n=n[1:]
    #print(*findBestSubSeqs(n))
    minSeq = min(filterMaxLen(findBestSubSeqs(n)))
    minLen = len(minSeq)
    print(str(minLen)+ " " + " ".join(map(str,minSeq))) """


import random
randSeq = [random.randrange(0,x+1) for x in range(200)]
minS = min(filterMaxLen(findBestSubSeqs(randSeq)))
print(*minS)
    