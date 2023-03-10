"""Coding Game: Challange 1"""


f = open("Challenge 1/data", 'r', encoding="utf-8")
f = f.read()

dictionary = {}

f = f.split("\n")

for i in f:
    A = i.split(" ")

    try:
        dictionary[A[2]] += int(A[1])
    except KeyError:
        dictionary[A[2]] = 0
        dictionary[A[2]] += int(A[1])

amounts = list(dictionary.values())
A = 0
for i in amounts:
    amounts[A] = i % 100
    A += 1

FINISHED = 0
for i in amounts:
    if FINISHED == 0:
        FINISHED = i
    else:
        FINISHED *= i
print(FINISHED)
