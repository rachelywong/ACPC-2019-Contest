
n = input()
c = n.split()
length = int(c[0])
num_p = int(c[1])


string = input()

for _ in range(num_p):
    i = input().split()

    pri[int(i[1])] = int(i[0])

sorted(pri.keys())

print(pri)