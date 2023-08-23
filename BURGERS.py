# cook your dish here
t=int(input())  # first line of input format
for i in range(t):
    A,B=map(int,input().split()) #second line of input format
    if A==B or A<B: # conditions based on test cases
        print(A)
    else:
        print(B)
