# task link: https://stepik.org/lesson/519126/step/10?thread=solutions&unit=511575(module 17.4, step 10)

with open('input.txt', 'r', encoding='utf-8') as file_in:
    content = [line for line in file_in.readlines()]
    spis_with_num = list(enumerate(content, 1))
    spis_with_num2 = list(map(lambda elem: f'{str(elem[0])}) {elem[1]}', spis_with_num))
    with open('output.txt', 'w', encoding='utf-8') as file_out:
        file_out.writelines(spis_with_num2)
