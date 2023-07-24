# cook your dish here
def is_good_turn(x,y):
    if(x+y)>6:
        return 'YES'
    else:
        return 'NO'
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    result=is_good_turn(x,y)
    print(result)
    