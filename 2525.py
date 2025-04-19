H,M = map(int, input().split())
T = input()

if M<=T:
    print(H,M+T)
else:
    if H==0:
        H=24
    H = H - 1
    M = M + 60 - 45
    print(H,M)