# task link: https://stepik.org/lesson/530408/step/15?thread=solutions&unit=523223 (module 17.3, step 15)

def read_csv():
    with open('data.csv', 'r', encoding='utf-8') as file:
        keys = file.readline().strip().split(',')
        content = [line.strip().split(',') for line in file.readlines()]
        spis_dict = []
        for elem in content:
            my_dict = dict(zip(keys, elem))
            spis_dict.append(my_dict)
    return spis_dict
