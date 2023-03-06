f = open("data", 'r')
f = f.read()

dict = {}

f = f.split("\n")

for i in f:
    a = i.split(" ")

    try:
        dict[a[2]] += int(a[1])
    except KeyError:
        dict[a[2]] = 0
        dict[a[2]] += int(a[1])

amounts = list(dict.values())
a = 0
for i in amounts:
    amounts[a] = i % 100
    a += 1

finished = 0
for i in amounts:
    if finished == 0:
        finished = i
    else:
        finished *= i
print(finished)
