
from math import *
no_cars=int(input())
lis_t=[]
l_list=[]
count_list=[]
total=0

def hc(a,b): 
    if(b==0): 
        return a 
    else: 
        return hc(b,a%b) 
  
for i in range(no_cars):
	data=list(input().split())
	distance=((eval(data[0])*2)+(eval(data[1])*2))
	speed=(eval(data[2])**2)
	g=hc(distance,speed)
	distance=distance/g
	speed=speed/g
	l_list.append((distance,speed))
l_list.sort()
total=[]
cnt = 0
total1=0
pre = l_list[0]
for i in l_list:
	if pre==i:
		cnt+=1
	else:
		total.append(cnt)
		cnt=1	
	pre = i	

total.append(cnt)

for i in t:
	if i>1:
		total1=total1+((i*(i-1))/2)
print(int(total1))