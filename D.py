
# p = int(input())


p = int(input())

to = 0

b = [] # bought

for _ in range(p):
    i = input().split()
    name = i[0]

    if name in b:
        continue

    n = int(name[-3]) + int(name[-2]) + int(name[-1])
    # print(n)

    price = int(i[1])

    if n % 5 == 0 and n != 0:
        to += int(price * 1/2)
        b.append(name)


print(to)