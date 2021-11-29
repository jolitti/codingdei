import sys
from functools import cache

dirs = [(0,-1),(-1,0),(-1,1),(0,1),(1,0),(1,-1)]

def addVec(a,b):
	return (a[0]+b[0],a[1]+b[1])

# n=steps left, pos = tuple
@cache
def paths(n,pos=(0,0)) -> int:
	if n==0:
		if pos==(0,0): return 1
		else: return 0
	return sum([paths(n-1,addVec(pos,x)) for x in dirs])

print(paths(int(sys.argv[1]),(0,0)))

#print("ans = { ",end="")
#for x in range(2,15,1):
#	print(x,end="")
#	print(": ",end="")
#	print(paths(x),end="")
#	print(", ",end="")
#print("}")

