m = int(input())

for j in range(m):
	n = int(input())
	maxLen = 1
	startIndex = 0
	s = {}

	for i in range(n):
		newNum = int(input())
		lastIndex = s.get(newNum)
		#print(f"last occ was {lastIndex}, current max is {maxLen}")
		s[newNum] = i
		if lastIndex and lastIndex >= startIndex:
			startIndex = lastIndex+1
		else:
			maxLen = max(maxLen,i-startIndex+1)

	print(maxLen)
