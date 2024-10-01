import math
count = 1
each = ('test', '60', 15, '30', '1')

def output(each, count):
    count = str(count)
    print('_' * 65)
    s_1 = '|' + count + ' ' * (abs(len(count) - 4)) + '|'
    s_2 = each[0] + ' ' * abs(len(each[0]) - 30) + '|'
    output_array = f'{s_1}{s_2}'
    for i in range(1, len(each)):
        value = str(each[i])
        output_array += (value + ' ' * (abs(len(value) - 4)) + '|')

    for i in range(1, 10):
        print(output_array)
        if i == 1:
            print('_' * 65)
    print('_' * 65)

output(each, count)
