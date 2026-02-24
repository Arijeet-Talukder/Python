
def solve():
    n = int(input())
    tokens = input().strip().split()
    tokens = [int(t) for t in tokens]
    
    total= 0
    multi = 0
    mx = 0
    
    for i in range(n):
        p = int(tokens[i])
        t = (p+9)//10
        total += t
        if t>1:
            multi += t
        if t>mx:
            mx=t
    print(total,multi,mx)
if __name__ == "__main__":
    solve()
    