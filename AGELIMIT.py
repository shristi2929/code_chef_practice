# cook your dish here
t=int(input())
for x in range(t):
    a,b,c=map(int,input().split())
    if(c>=a and c<b):
        print("YES")
    else:
        print("NO")
    
    
    