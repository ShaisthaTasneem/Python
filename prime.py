n=int(input())
count=0
for i in range(2,n//2):
    if n%i==0:
        count=1
        break
if count==0:
    print("yes")
else:
    print("not")
