def insertBestSubSeq(seqs:list, newVal:int):
    if len(seqs)<=0: return [[newVal]]
    for i,s in reversed(list(enumerate(seqs))):
        if newVal>s[-1]:
            if i+1>=len(seqs):
                seqs.append(s+[newVal])
            else:
                if newVal<seqs[i+1][-1]:
                    seqs[i+1]=s+[newVal]
            return seqs
    seqs[0]=[newVal]
    return seqs
        


def findBestSubSeqs(l:list):
    arrayLen = len(l)
    ans = []
    for x in l:
        #print(*ans)
        ans = insertBestSubSeq(ans,x)
        #for a in ans:
        #    print(*a)
        #print("-----")
    return ans

def filterMaxLen(l:list):
    lengths = [len(x) for x in l]
    maxLen = max(lengths)
    maxLengths = [x for x in l if len(x)==maxLen]
    #print(maxLengths)
    return maxLengths

while True:
    n = list(map(int,input().split()))
    if n[0]==0: break

    n=n[1:]
    #print(*findBestSubSeqs(n))
    minSeq = min(filterMaxLen(findBestSubSeqs(n)))
    minLen = len(minSeq)
    print(str(minLen)+ " " + " ".join(map(str,minSeq)))


""" import random
randSeq = [random.randrange(0,x+1) for x in range(200)]
minS = min(filterMaxLen(findBestSubSeqs(randSeq)))
print(*minS) """