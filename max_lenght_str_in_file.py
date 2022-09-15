# task link: https://stepik.org/lesson/530408/step/9?unit=523223 (module 17.3, step 9)

def lenght_elem(elem):
    if len(elem) == maximum:
        return elem


with open('lines.txt', 'r', encoding='utf-8') as file:
    content = [line.rstrip() for line in file.readlines()]
    spis_lenght = []
    for elem in content:
        lenght = len(elem)
        spis_lenght.append(lenght)
    maximum = max(spis_lenght)
    max_lenght = list(filter(lenght_elem, content))
    # print(content)
    print(*max_lenght)
