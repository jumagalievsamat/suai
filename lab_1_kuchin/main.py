import time
from conftest import *


count = ''

# output value
cpu = ''
done = ''
tasks_list = [('test', '60', 15, '30', '1')]


menu = True
while menu:
    action = input('1 - Запуск и ввод задачи\n2 - Показать очередь и выполненные задачи\nВведите значение: ')
    match action:
        case '1':
            # print('Введите входные данные')
            # title_tasks = input('1 - Имя задачи: ')
            time_complited = input('2 - время на выполнение этой задачи: ')
            time_start = int(input('3 - время начала выполнения эт2ой задачи: '))
            interval = input('4 - интервал выполнения задачи: ')
            prio = input('5 - Приоритет (1-5): ')
            tasks_list.append((time_complited, time_start, interval, prio))
        case '2':
            count = 1
            for each in tasks_list:
                output(each, count)

                # print(f'{count} Tasks title: \nTime_complited: {each[0]}\nTime_start: {each[1]}\nInterval: {each[2]}\nPrio: {each[3]}')
                # print('-' * 50)

