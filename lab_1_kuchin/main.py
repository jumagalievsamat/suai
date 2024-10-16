from conftest import *


# output value
cpu = ''
done = ''
tasks_list = [('count', 'tasks', 'time complited', 'time start', 'interval', 'prio')]


menu = True
while menu:
    action = input('1 - Запуск и ввод задачи\n2 - Показать очередь и выполненные задачи\n3 - autotest\n0 - выход\nВведите значение: ')
    match action:
        case '1':
            input_tasks(tasks_list)
        case '2':
            for each in tasks_list:
                output_tasks(each)
        case '3':
            print('еще не готово')
        case '0':
            break


