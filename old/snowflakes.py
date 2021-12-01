m = int(input())

for j in range(m):
	n = int(input())
	maxLen = 0
	startIndex = 0
	s = {}

	for i in range(n):
		newNum = int(input())
		lastIndex = s.get(newNum)
		s[newNum] = i
		if lastIndex is not None and (lastIndex >= startIndex):
			#print(f"Duplicate of {newNum} found")
			startIndex = lastIndex+1
		maxLen = max(maxLen,i-startIndex+1)
		#print(f"last occ was {lastIndex}, current max is {maxLen}")
	print(maxLen)
