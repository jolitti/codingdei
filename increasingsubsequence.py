def insertBestSubSeq(seqs:list,newVal:int):
    if len(seqs)<=0: return [[newVal]]
    ans = []
    for s in seqs:
        if newVal > s[-1]:
            ans.append(s+[newVal])
        elif newVal < s[0]:
            ans.append([newVal])
            ans.append(s)
        else:
            ans.append([x for x in s if x<newVal]+[newVal])
            ans.append(s)
    return ans

def findBestSubSeqs(l:list):
    ans = []
    for x in l:
        ans = insertBestSubSeq(ans,x)
    return ans

def filterMaxLen(l:list):
    lengths = [len(x) for x in l]
    maxLen = max(lengths)
    maxLengths = [x for x in l if len(x)==maxLen]
    return maxLengths


while True:
    n = list(map(int,input().split()))
    if n[0]==0: break

    n=n[1:]
    #print(*findBestSubSeqs(n))
    minSeq = min(filterMaxLen(findBestSubSeqs(n)))
    minLen = len(minSeq)
    print(str(minLen)+ " " + " ".join(map(str,minSeq)))
    