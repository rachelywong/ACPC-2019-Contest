n = input()
c = n.split()

g = int(c[0]) # radius
e = int(c[0])

t_1 = 0
t_2 = 0

en = []

for _ in range(e):
    q = input()
    t = q.split()
    en.append([int(t[0]), int(t[1])])
    t_1 += int(t[0])
    t_2 += int(t[1])


g_x = 1/2 * t_1
g_y = 1/2 * t_2

isO = True
for each in en:
    dix = abs(abs(each[0]) - abs(orx))   # distance x
    diy = abs(abs(each[1]) - abs(ory))

    if dix != 0:
        dis = math.sqrt(diy*diy / dix*dix)
    else:
        dis = diy

    if r * 2 < dis:
        is0 = False
        break

if isO:
    print("possible")
else:
    print("impossible")

