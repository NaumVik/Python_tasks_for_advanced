# task link: https://stepik.org/lesson/519126/step/11?thread=solutions&unit=511575(module 17.4, step 11)

with open('class_scores.txt', 'r', encoding='utf-8') as file_in:
    content = [line.split() for line in file_in.readlines()]
    new_score = list(
        map(lambda elem: f'{elem[0]} {100}\n' if int(elem[1]) + 5 > 100 else f'{elem[0]} {int(elem[1]) + 5}\n',
            content))
    with open('new_scores.txt', 'w', encoding='utf-8') as file_out:
        file_out.writelines(new_score)
