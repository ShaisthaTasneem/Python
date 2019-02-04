N,k=map(int,input().split())
if N>0:
    res=1
    for i in range(0,k):
        res=res*N;
    print(res)
else:
    print(0)

