l = int(input())
m = input()
w = int(input())
P = [0]*26
answer = [0]*l
k = 0
while k<l:
	P[ord(m[k]) - ord('a')]=P[ord(m[k]) -ord( 'a')]+1
	answer[k]=P[ord(m[k] )-ord( 'a')]
	k = k+1

j = 0
while j<w:
	u=int(input())
	t = answer[u-1]-1
	print(t)
	j = j+1