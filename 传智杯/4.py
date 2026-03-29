import sys
import heapq
data=sys.stdin.read().split()
idx=0
n=int(data[idx])
idx+=1
events=[]

for _ in range(n):
    a=int(data[idx])
    b=int(data[idx+1])
    events.append((a,b,0))
    idx+=2
q=int(data[idx])
idx+=1

query_results=[0]*q
for i in range(q):
    x=int(data[idx])
    events.append((x,i,1))
    idx+=1
events.sort(key=lambda item:(item[0],item[2]))

max_heap=[]
for items in events:
    if items[2]==0:
        b=items[1]
        heapq.heappush(max_heap,-b)
    else:
        idxxx=items[1]
        if max_heap:
            query_results[idxxx]=-max_heap[0]
        else:
            query_results[idxxx]=-1
sys.stdout.write('\n'.join(map(str,query_results))+'\n')

