
bottel_no=int(input())
lis_t=list(input().split())
lis_t.sort()
counter=[]
j=0
i=0
while i<bottel_no:
	if i==0:
		counter.append(1)
	else:
		if lis_t[i]==lis_t[i-1]:
			counter[j]+=1
		else:
			counter.append(1)
			j+=1
	i+=1		
solution=counter[-1]
total=counter[-1]

for i in counter[::-1][1:]:
	static=i-total
	if static>0:
		solution+=static
	if i>total:
		total=i

print(solution)