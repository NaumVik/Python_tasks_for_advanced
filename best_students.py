#task link: https://stepik.org/lesson/511854/step/14?unit=504046(module 15.9 step 14)
n = int(input())
students = {}
for i in range(1, n + 1):
    m = int(input())
    classroom = {}
    for j in range(m):
        s = input().split()
        classroom.setdefault(s[1], []).append(s[0])
    students.setdefault(i, classroom)

best = []
for key, value in students.items():
    result = any(map(lambda elem: elem == "5", value))
    best.append(result)
total = all(best)
if total:
    print("YES")
else:
    print("NO")
