

def countPebbles(board:str) -> int:
    i = 0
    for x in board: 
        if x=='o': i+=1
    return i

def move(board:str,pos:int,dir:int) -> str:
    if dir>0:
        return board[:pos]+"--o"+board[pos+3:]
    else:
        return board[:pos-2]+"o--"+board[pos+1:]

def nextMoves(board: str) -> list: #list of str
    ans = []
    for i,x in enumerate(board[:-2]):
        if board[i:i+3] == "-oo": ans.append(move(board,i+2,-1))
        elif board[i:i+3] == "oo-": ans.append(move(board,i,+1))
    return ans

def minPebsRemaining(board:str) -> int:
    nextM = nextMoves(board)
    if len(nextM)<=0: return countPebbles(board)
    return min([minPebsRemaining(x) for x in nextM])

n= int(input())

for i in range(n):
    print(minPebsRemaining(input()))