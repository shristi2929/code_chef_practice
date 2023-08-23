# cook your dish here
t = int(input())

for i in range(t):
    X, N = map(int, input().split())
    Y = (X * N) // 10   #//10 is done because there is total 10 test cases
    print(Y)



