
# l = {}

n = int(input())

interests = []
names = []

for _ in range(n):
    a = input()
    b = a.split()
    
    name = b[0]

    if name not in l:
        l[name] = []
    l[name].append(b[1])


n = int(input())

ans = ''

for _ in range(n):
    r = input()
    re = r.split()
    
    a = l[re[0]]
    b = l[re[1]]

    c = a + b
    d = set(c)

    if len(c) != len(d):
        ans += "Yes\n"
    else:
        ans += 'No\n'


print(ans.strip('\n'))