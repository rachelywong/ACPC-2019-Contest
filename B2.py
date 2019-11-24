

import math

n = input()
c = n.split()
r = int(c[1])


en = []

tox = 0
toy = 0

enx_sm = 0 # smallest enemy x
eny_sm = 0 # smallest enemy y


for _ in range(int(c[0])):
    i = input().split()
    enx = int(i[0]) # enemy x
    eny = int(i[1]) # enemy y
    en.append([enx, eny])

    tox, toy = tox + abs(enx), toy + abs(eny)

    enx_sm, eny_sm = min(enx_sm, enx), min(eny_sm, eny)

orx = tox / 2 + enx_sm
ory = toy / 2 + eny_sm


pos = True

for each in en:
    dix = abs(abs(each[0]) - abs(orx))   # distance x
    diy = abs(abs(each[1]) - abs(ory))

    if dix != 0:
        dis = math.sqrt(diy*diy / dix*dix)
    else:
        dis = diy


    if r * 2 < dis:
        pos = False
        break

if pos:
    print("possible")
else:
    print("impossible")