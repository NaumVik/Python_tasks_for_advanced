# task link: https://stepik.org/lesson/519126/step/12?unit=511575(module 17.4, step 12)
from functools import reduce

with open('goats.txt', 'r', encoding='utf-8') as file_in:
    content = [line.strip() for line in file_in.readlines()]
    del content[0]
    del content[6]
    colors = {}
    for elem in content:
        if elem not in colors.keys():
            colors.setdefault(elem, int(0))
        else:
            colors[elem] += 1
    answer_puzzle = []
    total = reduce(lambda x, value: x + value, colors.values(), 0)
    for key, value in colors.items():
        if value > total * 0.07:
            answer_puzzle.append(key + '\n')
    answer_puzzle.sort()

    with open('answer.txt', 'w', encoding='utf-8') as file_out:
        file_out.writelines(answer_puzzle)
