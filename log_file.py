# task link: https://stepik.org/lesson/519126/step/14?unit=511575(module 17.4, step 14)
def minutes(elem):
    new_elem = []
    name = f'{elem[0]} {elem[1].rstrip(",")}'
    time_in = [int(i.rstrip(',')) for i in elem[2].split(':')]
    time_out = [int(i) for i in elem[3].split(':')]
    result = (time_out[0] * 60 + time_out[1]) - (time_in[0] * 60 + time_in[1])
    new_elem.append(name)
    new_elem.append(result)
    return new_elem


with open('logfile.txt', 'r', encoding='utf-8') as file_in:
    content = [line.split() for line in file_in.readlines()]
    total = list(map(minutes, content))
    result = list(map(lambda elem: elem[0] + '\n', filter(lambda item: item if item[1] >= 60 else False, total)))

    with open('output.txt', 'w', encoding='utf-8') as file_out:
        file_out.writelines(result)
