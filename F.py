i = input().split()

health = int(i[0])
damage = int(i[1])
num = int(i[2]) #num of mag

mag = []

i = input()
mag = i.split()

# mag = int(mag)

for each in range(len(mag)):
    mag[each] = int(mag[each])

mag.sort(reverse=True)
# print(mag)

to = 0

while health > 0:
    to += int(mag.pop(0))
    health -= damage

print(to)