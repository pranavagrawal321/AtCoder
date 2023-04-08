a, b = map(int, input().split())
l = list(map(int, input().split()))
s = set()
if b == 0:
    print("Yes")
else:
    for i in l:
        if i + b in s or i - b in s:
            print("Yes")
            exit()
        s.add(i)
    print("No")