n = int(input())

my_dict = {}
for _ in range(n):
    s = input().split()
    if s[0] not in my_dict.keys():
        my_dict.setdefault(s[0], {s[1]: [int(s[2])]})
    else:
        my_dict[s[0]].setdefault(s[1], []).append(int(s[2]))
print()

for name in sorted(my_dict):
    print(name + ":")
    for key in sorted(my_dict[name]):
        print(key, sum(my_dict[name][key]))
print()
