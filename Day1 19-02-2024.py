#problem satement 1
a,b=map(int,input().split())
if a>b:
    print(a)
else:
    print(b)

#problem statement 2
a,b,c=map(int,input().split())
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    print(b)

#problem statement 3
a,b,c=map(in,input().split())
if a>b and a>c:
    if b>c:
        print(b)
    else:
        print(c)
elif b>c and b>a:
    if c>a:
        print(c)
    else:
        print(a)
elif c>a and c>b:
    if b>a:
        print(b)
    else:
        print(a)       

#problem statement 4
a,b,c=map(int,input().split())
if a>b and a>c:
    a=0
elif b>c:
    b=0
else:
    c=0
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)

#problem statement 5
print("Hello World\n"*1000)

#problem statement 6
a,b=map(int,input().split())
if a>b:
    print("a > b")
elif a<b:
    print("a < b")
else:
    print("a == b")

#problem staatement 7
a,b,c=map(int,input().split())
if a+b>c and b+c>a and c+a>b:
    print("Yes")
else:
    print("No")

#problem statement 8
n,k=map(int,input().split())
while k>=n:
    k-=n
print(k)

#problem statement 9
a=int(input())
t=-a if a<0 else a
tem=0
while t!=0:
    temp=t%10
    tem=tem*10+temp
    t//-10
if a<0:
    print(-tem)
else:
    print(tem)

#problem statement 10
a=int(input())
if a>2 and a%2==0:
    print("Yes")
else:
    print("No")

#problem statement 11
t=int(input())
while t:
    a=int(input())
    if a>98:
        print("YES")
    else:
        print("NO")
    t-=1

#problem statement 12
t=int(input())
while t:
    a=int(input())
    print(100-a)
    t-=1

#problem statement 13
t=int(input())
while t:
    a,b,c,d=map(int,input().split())
    a=a-(c*a//100)
    b=b-(d*b//100)
    if a<b:
        print("First")
    elif a>b:
        print("Second")
    else:
        print("Any")
    t-=1

#problem statement 14
t=int(input())
while t:
    a,b=map(int,input().split())
    if b>=a:
        print(0)
    else:
        if (a-b)%4==0:
            print((a-b)//4)
        else:
            print((a-b)//4+1)
    t-=1

#problem statement 15
t=int(input())
while t:
    a,b=map(int,input().split())
    if(a*b)%4==0:
        print((a*b)//4)
    else:
        print((a*b)//4+1)
    t-=1

#problem statement 16
t=int(input())
while t:
    a,b=map(int,input().split())
    k=a*b
    i=0
    while k>=4:
        k-=4
        i+=1
    if k==0:
        print(i)
    else:
        print(i+1)
    t-=1
    
    
                
