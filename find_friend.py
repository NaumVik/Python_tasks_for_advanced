from random import choice

n = int(input())
students = [input() for i in range(n)]
students2 = students.copy()

friend_spis = []

while len(students2) != 0:
    friend = choice(students2)
    i = 0
    while i != len(students):
        if friend == students[i] or [friend+" - "+students[i]] in friend_spis:
            i += 1
            continue
        else:
            friend_spis.append([students[i]+" - "+friend])
            students2.remove(friend)
            students.remove(students[i])
            i += 1
        break

print()

for elem in friend_spis:
    print(*elem, sep="\n")

